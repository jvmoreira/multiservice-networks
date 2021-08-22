class NetworkFunction:
    SHAPING_CATEGORY = 'shaping'
    POLICING_CATEGORY = 'policing'

    @classmethod
    def getName(cls):
        raise Exception('getName - Method not implemented')

    @classmethod
    def getParameters(cls, network_category):
        raise Exception('getParameters - Method not implemented for {}'.format(cls.getName()))

    @classmethod
    def getScript(cls):
        raise Exception('getScript - Method not implemented')

    @classmethod
    def raiseInvalidNetworkCategoryError(cls, network_category):
        raise Exception('Invalid network_category "{}" for {}'.format(network_category, cls.getName()))

class LeakyBucket(NetworkFunction):
    @classmethod
    def getName(cls):
        return 'Leaky Bucket'

    @classmethod
    def getParameters(cls, network_category):
        if network_category == NetworkFunction.SHAPING_CATEGORY:
            return ['packets_to_release', 'bucket_max_size', 'interval', 'interface', 'debug']

        cls.raiseInvalidNetworkCategoryError(network_category)

    @classmethod
    def getScript(cls):
        return 'leaky-bucket.py'

class TokenBucket(NetworkFunction):
    @classmethod
    def getName(cls):
        return 'Token Bucket'

    @classmethod
    def getParameters(cls, network_category):
        if network_category == NetworkFunction.SHAPING_CATEGORY:
            return ['rate', 'bucket_size', 'bucket_max_size', 'interval', 'queue_max_size', 'interface', 'debug']
        if network_category == NetworkFunction.POLICING_CATEGORY:
            return ['rate', 'bucket_size', 'bucket_max_size', 'interval', 'interface', 'debug']

        cls.raiseInvalidNetworkCategoryError(network_category)

    @classmethod
    def getScript(cls):
        return 'token-bucket.py'

class OneRateThreeColor(NetworkFunction):
    @classmethod
    def getName(cls):
        return 'One Rate Three Color'

    @classmethod
    def getParameters(cls, network_category):
        if network_category == NetworkFunction.POLICING_CATEGORY:
            return ['rate', 'bucketF_size', 'bucketF_max_size', 'bucketS_size', 'bucketS_max_size', 'interval', 'host_address', 'target_address']

        cls.raiseInvalidNetworkCategoryError(network_category)

    @classmethod
    def getScript(cls):
        return 'one-rate-three-color.py'

class TwoRateThreeColor(NetworkFunction):
    @classmethod
    def getName(cls):
        return 'Two Rate Three Color'

    @classmethod
    def getParameters(cls, network_category):
        if network_category == NetworkFunction.POLICING_CATEGORY:
            return ['rateF', 'rateS', 'bucketF_size', 'bucketF_max_size', 'bucketS_size', 'bucketS_max_size', 'interval', 'host_address', 'target_address']

        cls.raiseInvalidNetworkCategoryError(network_category)

    @classmethod
    def getScript(cls):
        return 'two-rate-three-color.py'
