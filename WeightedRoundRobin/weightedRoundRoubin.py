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

HIGH_PRIORITY = 10
MEDIUM_PRIORITY = 5
LOW_PRIORITY = 0

PRIORITIES = [HIGH_PRIORITY, MEDIUM_PRIORITY, LOW_PRIORITY]

QUEUES = { HIGH_PRIORITY: [], MEDIUM_PRIORITY: [], LOW_PRIORITY: [] }

def resetQueues():
    for priority in PRIORITIES:
        del QUEUES[priority][:]

def insertRequestWithPriority(request, priority):
    QUEUES[priority].append(request)

def getPriority(content):
    for priority in PRIORITIES:
        if len(content) > priority:
            return priority

    return LOW_PRIORITY

def parseRequest(request):
    return request.split('__')

def nf_main(token):
    print('Server Started')

    requestsToReceive = 0
    requestsReceived = 0
    outputBuffer = ''

    Socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    Socket.bind(('192.168.122.40', 8005))

    while(token[0]):

        [requestReceived, originAddress] = Socket.recvfrom(65000)

        if(requestReceived == 'end_main'):
            Socket.close()
            print('Received: STOP!')

        elif '_reset' in requestReceived[0:6]:
            options = requestReceived.split(' ')[1:]
            outputBuffer = ''
            resetQueues()
            requestsReceived = 0
            requestsToReceive = int( options[0].split('=')[1] )
            print('Reset! Requests to Receive = {}'.format(requestsToReceive))

        else:
            [contentReceived, requestNumber] = parseRequest(requestReceived)
            requestPriority = getPriority(contentReceived)

            insertRequestWithPriority(requestReceived, requestPriority)

            requestsReceived += 1

            if requestsReceived >= requestsToReceive:
                for priority in PRIORITIES:
                    print('Priority = {} | Queue Size = {}'.format(priority, len(QUEUES[priority])))

            #print('Received = {}{} | Size = {:02d} | Bucket = {:02d} | From = {}'.format(contentReceived, padding, bytesReceived, bucket, originAddress))

            #Socket.sendto(outputBuffer, originAddress)
