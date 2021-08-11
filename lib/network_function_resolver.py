from .network_functions import LeakyBucket, TokenBucket

class NetworkFunctionResolver:
    @classmethod
    def resolve(cls, network_function_name):
        if network_function_name == 'leaky-bucket': return LeakyBucket
        if network_function_name == 'token-bucket': return TokenBucket

        raise Exception('Network function not supported: "{}"'.format(network_function_name))
