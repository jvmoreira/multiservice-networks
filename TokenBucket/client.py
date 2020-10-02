import time
import socket
import random

MAX_REQUESTS = 10000
TIME_BETWEEN_REQUESTS = .001
RATE = 7
RANDOM_SEED = 1601327277
random.seed(RANDOM_SEED)

Socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

currentTime = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())
outputFile = open('log-' + currentTime + '.txt', 'w')
outputBuffer = ''

Socket.bind(('192.168.122.1', 8005))

serverAddress = ('192.168.122.40', 8005)

wordsToSend = []

requestsSent = 0
requestsSucceed = 0

Socket.sendto('_reset _rate={}'.format(RATE), serverAddress)

startTimestap = time.time()
while(requestsSent < MAX_REQUESTS):
    contentToSend = 'a' * random.randint(1,15)
    Socket.sendto(contentToSend, serverAddress)
    contentTimestamp = int( 1e+3 * (time.time() - startTimestap) )

    [contentReceived, originAddress] = Socket.recvfrom(65000)

    requestSucceed = 'OK' in contentReceived
    if requestSucceed:
        requestsSucceed = requestsSucceed + 1
        color = '1;32m'
    else:
        color = '1;31m'

    padding = ' ' * ((15-len(contentToSend)) if requestSucceed else 7)
    #print('\x1b[{}Sent = {:02d} bytes | Received = [ {} ]{} | From = {}\x1b[0m'.format(color, len(contentToSend), contentReceived, padding, originAddress))
    packageStatus = 'OK' if requestSucceed else 'DROPPED'
    outputBuffer += ('[{:d}] Sent = {:02d} bytes | Result = {}\n'.format(contentTimestamp, len(contentToSend), packageStatus))

    requestsSent = requestsSent + 1

requestsDropped = MAX_REQUESTS - requestsSucceed
outputFile.write('Requests Succeed = {} | Requests Dropped = {} | Total Requests = {}\n\n'.format(requestsSucceed, requestsDropped, MAX_REQUESTS))
outputFile.write('Bucket size = 50 | Rate = {}\n\n'.format(RATE))
outputFile.write('Randomized with seed {}\n\n'.format(RANDOM_SEED))
outputFile.write(outputBuffer)

Socket.close()
