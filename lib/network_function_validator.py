class NetworkFunctionValidator:
    @classmethod
    def validate(cls, network_function, parameters):
        function_category = parameters['category']

        if any(key not in parameters.keys() for key in network_function.getParameters(function_category)):
            raise Exception('Missing parameters for {} network function'.format(network_function.getName()))
