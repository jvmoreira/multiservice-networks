def buildParametersDefinitionString(network_function, function_category, parameters):
    parameters_definition = ''

    for parameter_name in network_function.getParameters(function_category):
        parameter_value = parameters[parameter_name]
        parameters_definition += '{} = {}\n'.format(parameter_name, parameter_value)

    return parameters_definition.rstrip()

class NetworkFunctionScriptResolver:
    @classmethod
    def resolve(cls, network_function, parameters):
        function_category = parameters['category']
        filename = '{}/{}'.format(function_category, network_function.getScript())

        with open(filename, 'r') as script_file:
            script = script_file.read()
            parameters_definition = buildParametersDefinitionString(network_function, function_category, parameters)

            return script.replace('#__PARAMETERS__', parameters_definition)
