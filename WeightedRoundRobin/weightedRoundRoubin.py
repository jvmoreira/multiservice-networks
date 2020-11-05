//VNF_HEADER
//VNF_VERSION: 1.0
//VNF_ID: 979eaf94-ad8c-4aef-90fa-c29189b42fde
//VNF_PROVIDER: UFPR
//VNF_NAME: Content Find
//VNF_RELEASE_DATE: 2020-11-08 11-45-45
//VNF_RELEASE_VERSION: 1.0
//VNF_RELEASE_LIFESPAN: 2020-11-09 11-45-45
//VNF_DESCRIPTION: Find a required content in a CDN pool
//VNF_FRAMEWORK: Python2
//VNF_NETWORK: VirtIO
import socket

def nf_stop(token):
    Socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    Socket.sendto('end_main', ('192.168.122.40', 8005))

    print('Sent: STOP!')
    Socket.close()
    return

class Priority:
    NORMALIZE_WEIGHTS = 0

    HIGH = 10
    HIGH_WEIGHT = 4
    HIGH_WEIGHT_NORMALIZED = int(10 * HIGH_WEIGHT / 13)

    MEDIUM = 5
    MEDIUM_WEIGHT = 2
    MEDIUM_WEIGHT_NORMALIZED = int(10 * MEDIUM_WEIGHT / 8)

    LOW = 0
    LOW_WEIGHT = 1
    LOW_WEIGHT_NORMALIZED = int(10 * LOW_WEIGHT / 3)

    PRIORITIES_LIST = [HIGH, MEDIUM, LOW]

    @classmethod
    def getWeight(cls, priority):
        if priority == cls.HIGH:
            return cls.HIGH_WEIGHT_NORMALIZED if cls.NORMALIZE_WEIGHTS else cls.HIGH_WEIGHT
        elif priority == cls.MEDIUM:
            return cls.MEDIUM_WEIGHT_NORMALIZED if cls.NORMALIZE_WEIGHTS else cls.MEDIUM_WEIGHT
        elif priority == cls.LOW:
            return cls.LOW_WEIGHT_NORMALIZED if cls.NORMALIZE_WEIGHTS else cls.LOW_WEIGHT

    @classmethod
    def getPriorityAsString(cls, priority):
        if priority == cls.HIGH:
            return 'HIGH'
        elif priority == cls.MEDIUM:
            return 'MEDIUM'
        elif priority == cls.LOW:
            return 'LOW'

    @classmethod
    def evaluate(cls, content):
        for priority in cls.PRIORITIES_LIST:
            if len(content) > priority:
                return priority

        return LOW

class WeightedRoundRobin:
    def __init__(self):
        self.__queues = {
            Priority.HIGH: [],
            Priority.MEDIUM: [],
            Priority.LOW: [],
        }
        self.reset()

    @staticmethod
    def parseRequest(request):
        return request.split('__')

    def handleNewRequest(self, request):
        [contentReceived, requestNumber] = WeightedRoundRobin.parseRequest(request)
        requestPriority = Priority.evaluate(contentReceived)

        self.insertRequestWithPriority(request, requestPriority)

        self.__requestsReceived += 1

    def insertRequestWithPriority(self, request, priority):
        self.__queues[priority].append(request)

    def receivedAllRequests(self):
        return self.__requestsReceived >= self.__requestsToReceive

    def received500Req(self):
        return self.__requestsReceived >= 500

    def reset(self, requestsToReceive = 0):
        self.outputBuffer = ''
        self.__resetQueues()
        self.__requestsReceived = 0
        self.__requestsToReceive = requestsToReceive if requestsToReceive >= 0 else self.__requestsToReceive
        print('Reset! Requests to Receive = {}'.format(self.__requestsToReceive))

    def __resetQueues(self):
        for priority in Priority.PRIORITIES_LIST:
            del self.__queues[priority][:]

    def printQueues(self):
        for priority in Priority.PRIORITIES_LIST:
            queueSize = len( self.__queues[priority] )
            print('Priority={} | Queue Size={}'.format(priority, queueSize))

    def hasRequestsToProcess(self):
        highQueueSize = len( self.__queues[Priority.HIGH] )
        mediumQueueSize = len( self.__queues[Priority.MEDIUM] )
        lowQueueSize = len( self.__queues[Priority.LOW] )
        return highQueueSize or mediumQueueSize or lowQueueSize

    def processEnqueuedRequests(self):
        while self.hasRequestsToProcess():
            for priority in Priority.PRIORITIES_LIST:
                queue = self.__queues[priority]
                self.processRequestsFromQueue(queue, priority)

    def processRequestsFromQueue(self, queue, priority):
        if not len(queue): return

        queueWeight = Priority.getWeight(priority)
        priorityName = Priority.getPriorityAsString(priority)
        priorityNumber = priority / 5

        requestsToProcess = queueWeight if len(queue) >= queueWeight else len(queue)
        for _ in range(requestsToProcess):
            request = queue.pop(0)
            [content, requestNumber] = WeightedRoundRobin.parseRequest(request)
            contentSize = len(content)
            requestNumber = int(requestNumber)

            self.outputBuffer += '{};{};{}\n'.format(requestNumber, contentSize, priorityNumber)


def nf_main(token):
    print('Server Started')

    Socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    Socket.bind(('192.168.122.40', 8005))

    wrr = WeightedRoundRobin()

    while(token[0]):

        [requestReceived, originAddress] = Socket.recvfrom(65000)

        if(requestReceived == 'end_main'):
            Socket.close()
            print('Received: STOP!')

        elif '_reset' in requestReceived[0:6]:
            requestsToReceiveOption = requestReceived.split(' ')[1]
            requestsToReceive = int( requestsToReceiveOption.split('=')[1] )

            wrr.reset(requestsToReceive = requestsToReceive)

        else:
            wrr.handleNewRequest(requestReceived)

            if wrr.receivedAllRequests():
                wrr.printQueues()
                wrr.processEnqueuedRequests()
                Socket.sendto(wrr.outputBuffer, originAddress)
                # wrr.reset(-1)
