import time
import socket
import random

LOG_ENABLED = 0
LOG_TO_FILE_ENABLED = 1
SLEEP_ENABLED = 0
MAX_REQUESTS = 100
TIME_BETWEEN_REQUESTS = .001
RATE = 3
RANDOM_SEED = 1601327277 # int( time.time() )
random.seed(RANDOM_SEED)

def printLog(requestSucceed, contentSentSize, contentReceived, originAddress):
    if not LOG_ENABLED: return

    color = '1;32m' if requestSucceed else '1;31m'
    padding = ' ' * ((15-contentSentSize) if requestSucceed else 7)
    print('\x1b[{}Sent = {:02d} bytes | Received = [ {} ]{} | From = {}\x1b[0m'.format(color, contentSentSize, contentReceived, padding, originAddress))

outputBuffer = ''

Socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
Socket.bind(('192.168.122.1', 8005))
SERVER_ADDRESS = ('192.168.122.40', 8005)

requestsSent = 0
requestsSucceed = 0

Socket.sendto('_reset _rate={}'.format(RATE), SERVER_ADDRESS)

startTimestap = time.time()
while(requestsSent < MAX_REQUESTS):
    contentSize = random.randint(1,15)
    contentToSend = 'a' * contentSize

    Socket.sendto(contentToSend, SERVER_ADDRESS)
    contentTimestamp = int( 1e+3 * (time.time() - startTimestap) )

    [contentReceived, originAddress] = Socket.recvfrom(65000)

    requestSucceed = 'OK' in contentReceived
    if requestSucceed:
        requestsSucceed = requestsSucceed + 1

    outputBuffer += ('[{:d}] Sent = {:02d} bytes | Result = {}\n'.format(contentTimestamp, contentSize, 'OK' if requestSucceed else 'DROPPED'))
    printLog(requestSucceed, contentSize, contentReceived, originAddress)

    requestsSent = requestsSent + 1

    if SLEEP_ENABLED: time.sleep(TIME_BETWEEN_REQUESTS)

requestsDropped = MAX_REQUESTS - requestsSucceed

if LOG_TO_FILE_ENABLED:
    currentDatetime = time.strftime("%Y%m%d-%H%M%S", time.localtime())
    outputFile = open('log-rate-{}-{}.txt'.format(RATE, currentDatetime), 'w')

    outputFile.write('Requests Succeed = {} | Requests Dropped = {} | Total Requests = {}\n\n'.format(requestsSucceed, requestsDropped, MAX_REQUESTS))
    outputFile.write('Bucket size = 50 | Rate = {}\n\n'.format(RATE))
    outputFile.write('Randomized with seed {}\n\n'.format(RANDOM_SEED))
    outputFile.write(outputBuffer)

Socket.close()
