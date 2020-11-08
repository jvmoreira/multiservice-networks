import time
import socket
import random

LOG_ENABLED = 0
LOG_TO_FILE_ENABLED = 0
SLEEP_ENABLED = 1
MAX_REQUESTS = 500
TIME_BETWEEN_REQUESTS = .0001
RANDOM_SEED = int( time.time() )
random.seed(RANDOM_SEED)

def printLog(contentSentSize):
    if not LOG_ENABLED: return

    print('Sent = {:02d} bytes'.format(contentSentSize))

Socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
Socket.bind(('192.168.122.1', 8005))
SERVER_ADDRESS = ('192.168.122.40', 8005)

requestsSent = 0

arquivoSaida = open('wrr-{}.csv'.format(MAX_REQUESTS), 'w')
Socket.sendto('_reset _requests={}'.format(MAX_REQUESTS), SERVER_ADDRESS)

startTimestap = time.time()
while(requestsSent < MAX_REQUESTS):
    contentSize = random.randint(1,15)
    contentToSend = 'a' * contentSize

    request = '{}__{}'.format(contentToSend, requestsSent)

    Socket.sendto(request, SERVER_ADDRESS)
    requestTimestamp = int( 1e+3 * (time.time() - startTimestap) )

    printLog(contentSize)

    requestsSent += 1

    if SLEEP_ENABLED: time.sleep(TIME_BETWEEN_REQUESTS)

[outputBuffer, _] = Socket.recvfrom(65000)
arquivoSaida.write(outputBuffer.decode())

arquivoSaida.close()
Socket.close()
