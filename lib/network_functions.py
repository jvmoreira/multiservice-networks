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