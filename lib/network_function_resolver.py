from .network_functions import LeakyBucket, TokenBucket, OneRateThreeColor, TwoRateThreeColor

class NetworkFunctionResolver:
    @classmethod
    def resolve(cls, network_function_name):
        if network_function_name == 'leaky-bucket': return LeakyBucket
        if network_function_name == 'token-bucket': return TokenBucket
        if network_function_name == 'one-rate-three-color': return OneRateThreeColor
        if network_function_name == 'two-color-three-color': return TwoRateThreeColor

        raise Exception('Network function not supported: "{}"'.format(network_function_name))
