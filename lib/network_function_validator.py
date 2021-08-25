class NetworkFunctionValidator:
    POSSIBLE_COLOR_AWARE = ["one-rate-three-color", "two-rate-three-color"]

    @classmethod
    def validate(cls, network_function, parameters):
        function_category = parameters['category']
        function = parameters['function']
        if function in NetworkFunctionValidator.POSSIBLE_COLOR_AWARE:
            color_aware_value = parameters['color_aware']
            if any(key not in parameters.keys() for key in network_function.getParameters(function_category, color_aware_value)):
                raise Exception('Missing parameters for {} network function'.format(network_function.getName()))
        else:
            if any(key not in parameters.keys() for key in network_function.getParameters(function_category)):
                raise Exception('Missing parameters for {} network function'.format(network_function.getName()))
