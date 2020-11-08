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
    INVERT_WEIGHTS = 1

    HIGH = 10
    HIGH_WEIGHT = 4
    HIGH_WEIGHT_INVERTED = 1

    MEDIUM = 5
    MEDIUM_WEIGHT = 2
    MEDIUM_WEIGHT_INVERTED = 2

    LOW = 0
    LOW_WEIGHT = 1
    LOW_WEIGHT_INVERTED = 4

    PRIORITIES_LIST = [HIGH, MEDIUM, LOW]

    @classmethod
    def getWeight(cls, priority):
        if priority == cls.HIGH:
            return cls.HIGH_WEIGHT_INVERTED if cls.INVERT_WEIGHTS else cls.HIGH_WEIGHT
        elif priority == cls.MEDIUM:
            return cls.MEDIUM_WEIGHT_INVERTED if cls.INVERT_WEIGHTS else cls.MEDIUM_WEIGHT
        elif priority == cls.LOW:
            return cls.LOW_WEIGHT_INVERTED if cls.INVERT_WEIGHTS else cls.LOW_WEIGHT

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

class WeightedFairQueuing:

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
        [contentReceived, requestNumber] = WeightedFairQueuing.parseRequest(request)
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
        self.__requestsToReceive = requestsToReceive if requestsToReceive >= 0 else self.__requestsToReceive
        self.ROUND_NUM_HIGH = 0
        self.ROUND_NUM_MEDIUM = 0
        self.ROUND_NUM_LOW = 0
        print('Reset! Requests to Receive = {}'.format(self.__requestsToReceive))

    def __resetQueues(self):
        for priority in Priority.PRIORITIES_LIST:
            del self.__queues[priority][:]

    def printQueues(self):
        for priority in Priority.PRIORITIES_LIST:
            queueSize = len( self.__queues[priority] )
            print('Priority={} | Queue Size={}'.format(priority, queueSize))

    def getRoundNumber(self, priority):
        if priority == Priority.HIGH: return self.ROUND_NUM_HIGH
        if priority == Priority.MEDIUM: return self.ROUND_NUM_MEDIUM
        if priority == Priority.LOW: return self.ROUND_NUM_LOW

    def setRoundNumber(self, priority, value):
        if priority == Priority.HIGH: self.ROUND_NUM_HIGH = value
        if priority == Priority.MEDIUM: self.ROUND_NUM_MEDIUM = value
        if priority == Priority.LOW: self.ROUND_NUM_LOW = value

    def hasRequestsToProcess(self):
        highQueueSize = len( self.__queues[Priority.HIGH] )
        mediumQueueSize = len( self.__queues[Priority.MEDIUM] )
        lowQueueSize = len( self.__queues[Priority.LOW] )
        return highQueueSize or mediumQueueSize or lowQueueSize

    def calculateRoundNumbers(self):
        self.ROUND_NUM_HIGH += Priority.HIGH_WEIGHT_INVERTED * 13
        self.ROUND_NUM_MEDIUM += Priority.MEDIUM_WEIGHT_INVERTED * 8
        self.ROUND_NUM_LOW += Priority.LOW_WEIGHT_INVERTED * 3

    def processEnqueuedRequests(self):
        self.calculateRoundNumbers()
        while self.hasRequestsToProcess():
            self.processRequests()

    def nextReadPriority(self):
        if ((self.ROUND_NUM_HIGH <= self.ROUND_NUM_MEDIUM) and (self.ROUND_NUM_HIGH <= self.ROUND_NUM_LOW)):
            return Priority.HIGH
        if ((self.ROUND_NUM_MEDIUM <= self.ROUND_NUM_HIGH) and (self.ROUND_NUM_MEDIUM <= self.ROUND_NUM_LOW)):
            return Priority.MEDIUM
        return Priority.LOW

    def processRequests(self):
        queuePriority = self.nextReadPriority()
        queue = self.__queues[queuePriority]
        priorityNumber = queuePriority / 5

        request = queue.pop(0)
        [content, requestNumber] = WeightedFairQueuing.parseRequest(request)
        contentSize = len(content)
        requestNumber = int(requestNumber)
        self.outputBuffer += '{};{};{}\n'.format(requestNumber, contentSize, priorityNumber)

        self.updateRoundNumber(queue, queuePriority)

    def updateRoundNumber(self, queue, queuePriority):
        if len(queue) == 0:
            self.setRoundNumber(queuePriority, 160001)
        else:
            currentRoundNumber = self.getRoundNumber(queuePriority)
            queueAveragePacketSize = queuePriority + 3
            newRoundNumber = currentRoundNumber + Priority.getWeight(queuePriority) * queueAveragePacketSize
            self.setRoundNumber(queuePriority, newRoundNumber)


def nf_main(token):
    print('Server Started')

    Socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    Socket.bind(('192.168.122.40', 8005))

    wrr = WeightedFairQueuing()

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
                # wrr.reset()
