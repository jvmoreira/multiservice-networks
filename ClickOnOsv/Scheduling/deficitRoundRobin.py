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
    QUANTA_FACTOR = 3

    HIGH = 10
    HIGH_WEIGHT = 4
    HIGH_QUANTA = HIGH_WEIGHT * QUANTA_FACTOR

    MEDIUM = 5
    MEDIUM_WEIGHT = 2
    MEDIUM_QUANTA = MEDIUM_WEIGHT * QUANTA_FACTOR

    LOW = 0
    LOW_WEIGHT = 1
    LOW_QUANTA = LOW_WEIGHT * QUANTA_FACTOR

    PRIORITIES_LIST = [HIGH, MEDIUM, LOW]

    @classmethod
    def getWeight(cls, priority):
        if priority == cls.HIGH:
            return cls.HIGH_WEIGHT
        elif priority == cls.MEDIUM:
            return cls.MEDIUM_WEIGHT
        elif priority == cls.LOW:
            return cls.LOW_WEIGHT

    @classmethod
    def getQuanta(cls, priority):
        if priority == cls.HIGH:
            return cls.HIGH_QUANTA
        elif priority == cls.MEDIUM:
            return cls.MEDIUM_QUANTA
        elif priority == cls.LOW:
            return cls.LOW_QUANTA

    @classmethod
    def updateQuanta(cls, value, priority):
        if priority == cls.HIGH:
            cls.HIGH_QUANTA = value + cls.HIGH_WEIGHT * cls.QUANTA_FACTOR
        elif priority == cls.MEDIUM:
            cls.MEDIUM_QUANTA = value + cls.MEDIUM_WEIGHT * cls.QUANTA_FACTOR
        elif priority == cls.LOW:
            cls.LOW_QUANTA = value + cls.LOW_WEIGHT * cls.QUANTA_FACTOR

    @classmethod
    def resetQuanta(cls):
        cls.HIGH_QUANTA = cls.HIGH_WEIGHT * cls.QUANTA_FACTOR
        cls.MEDIUM_QUANTA = cls.MEDIUM_WEIGHT * cls.QUANTA_FACTOR
        cls.LOW_QUANTA = cls.LOW_WEIGHT * cls.QUANTA_FACTOR

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

class DeficitRoundRobin:
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
        [contentReceived, requestNumber] = DeficitRoundRobin.parseRequest(request)
        requestPriority = Priority.evaluate(contentReceived)

        self.insertRequestWithPriority(request, requestPriority)

        self.__requestsReceived += 1

    def insertRequestWithPriority(self, request, priority):
        self.__queues[priority].append(request)

    def receivedAllRequests(self):
        return self.__requestsReceived >= self.__requestsToReceive

    def reset(self, requestsToReceive = 0):
        self.outputBuffer = ''
        self.__resetQueues()
        self.__requestsReceived = 0
        Priority.resetQuanta()
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

        quanta = Priority.getQuanta(priority)

        while len(queue):
            request = queue[0]
            [content, requestNumber] = DeficitRoundRobin.parseRequest(request)
            contentSize = len(content)

            if quanta < contentSize:
                break

            priorityNumber = priority / 5
            self.outputBuffer += '{};{};{}\n'.format(int(requestNumber), contentSize, priorityNumber)

            queue.pop(0)
            quanta -= contentSize

        Priority.updateQuanta(quanta, priority)

def nf_main(token):
    print('Server Started')

    Socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    Socket.bind(('192.168.122.40', 8005))

    wrr = DeficitRoundRobin()

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
                chunkSize = 9125
                outputBufferChunks = [ wrr.outputBuffer[i:i+chunkSize] for i in range(0, len(wrr.outputBuffer), chunkSize) ]
                for chunk in outputBufferChunks:
                    Socket.sendto(chunk, originAddress)
                Socket.sendto("_EOF", originAddress)
                # wrr.reset(-1)
