def buildParametersDefinitionString(network_function, function_category, parameters):
    parameters_definition = ''
    
    function = parameters['function']
    if function in NetworkFunctionScriptResolver.POSSIBLE_COLOR_AWARE:
        color_aware_value = parameters['color_aware']
        for parameter_name in network_function.getParameters(function_category, color_aware_value):
            parameter_value = parameters[parameter_name]
            parameters_definition += '{} = {}\n'.format(parameter_name, parameter_value)
    else:
        for parameter_name in network_function.getParameters(function_category):
            parameter_value = parameters[parameter_name]
            parameters_definition += '{} = {}\n'.format(parameter_name, parameter_value)

    return parameters_definition.rstrip()

class NetworkFunctionScriptResolver:
    POSSIBLE_COLOR_AWARE = ["one-rate-three-color", "two-rate-three-color"]

    @classmethod
    def resolve(cls, network_function, parameters):
        function_category = parameters['category']
        filename = '{}/{}'.format(function_category, network_function.getScript())

        with open(filename, 'r') as script_file:
            script = script_file.read()
            parameters_definition = buildParametersDefinitionString(network_function, function_category, parameters)

            return script.replace('#__PARAMETERS__', parameters_definition)
