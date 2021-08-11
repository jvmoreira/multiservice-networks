class NetworkFunctionValidator:
    @classmethod
    def validate(cls, network_function, parameters):
        if any(key not in parameters.keys() for key in network_function.getParameters()):
            raise Exception('Missing parameters for {} network function'.format(network_function.getName()))