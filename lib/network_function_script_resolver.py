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
