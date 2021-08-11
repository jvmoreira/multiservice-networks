import json

class NetworkFunction:
    @classmethod
    def getName(cls):
        raise Exception('getName - Method not implemented')

    @classmethod
    def getParameters(cls):
        raise Exception('getParameters - Method not implemented')

    @classmethod
    def getScript(cls):
        raise Exception('getScript - Method not implemented')

class LeakyBucket(NetworkFunction):
    @classmethod
    def getName(cls):
        return 'Leaky Bucket'

    @classmethod
    def getParameters(cls):
        return ['packets_to_release', 'bucket_max_size', 'interval', 'host_address', 'target_address']

    @classmethod
    def getScript(cls):
        return 'leaky-bucket.py'

class TokenBucket(NetworkFunction):
    @classmethod
    def getName(cls):
        return 'Token Bucket'

    @classmethod
    def getParameters(cls):
        return ['rate', 'bucket_size', 'bucket_max_size', 'interval', 'queue_max_size', 'host_address', 'target_address']

    @classmethod
    def getScript(cls):
        return 'token-bucket.py'

class NetworkFunctionResolver:
    @classmethod
    def resolve(cls, network_function_name):
        if network_function_name == 'leaky-bucket': return LeakyBucket
        if network_function_name == 'token-bucket': return TokenBucket

        raise Exception('Network function not supported: "{}"'.format(network_function_name))

class NetworkFunctionValidator:
    @classmethod
    def validate(cls, network_function, parameters):
        if any(key not in parameters.keys() for key in network_function.getParameters()):
            raise Exception('Missing parameters for {} network function'.format(network_function.getName()))

def buildParametersDefinitionString(network_function, parameters):
    parameters_definition = ''

    for parameter_name in network_function.getParameters():
        parameter_value = parameters[parameter_name]
        parameters_definition += '{} = {}\n'.format(parameter_name, parameter_value)

    return parameters_definition.rstrip()

class NetworkFunctionScriptResolver:
    @classmethod
    def resolve(cls, network_category, network_function, parameters):
        filename = '{}/{}'.format(network_category, network_function.getScript())
        with open(filename, 'r') as script_file:
            script = script_file.read()
            parameters_definition = buildParametersDefinitionString(network_function, parameters)
            return script.replace('#__PARAMETERS__', parameters_definition)

with open('framework.config.json', 'r') as config_file:
    config = json.load(config_file)

    try:
        network_category = config['category']
        network_function = NetworkFunctionResolver.resolve(config['function'])

        NetworkFunctionValidator.validate(network_function, config)

        script = NetworkFunctionScriptResolver.resolve(network_category, network_function, config)

        output_file = open('{}-nf.py'.format(config['function']), 'w')
        output_file.write(script)
        output_file.close()

    except Exception as err:
        print(err)
