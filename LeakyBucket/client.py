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

elapsedTime = 0
def incrementElapsedTime():
    packetTime = random.uniform(0.0001, 0.5)
    elapsedTime += packetTime


Socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
Socket.bind(('192.168.122.1', 8005))
SERVER_ADDRESS = ('192.168.122.40', 8005)

requestsSent = 0

arquivoSaida = open('lb-{}.csv'.format(MAX_REQUESTS), 'w')
Socket.sendto('_reset', SERVER_ADDRESS)

startTimestap = time.time()
while(requestsSent < MAX_REQUESTS):
    contentSize = random.randint(1,100)

    request = '{}__{:.4f}'.format(contentSize, elapsedTime)
    incrementElapsedTime()

    Socket.sendto(request, SERVER_ADDRESS)

    printLog(contentSize)

    requestsSent += 1

    if SLEEP_ENABLED: time.sleep(TIME_BETWEEN_REQUESTS)

Socket.sendto('_end', SERVER_ADDRESS)

[outputBuffer, _] = Socket.recvfrom(65000)
while '_EOF' not in outputBuffer:
    arquivoSaida.write(outputBuffer.decode())
    [outputBuffer, _] = Socket.recvfrom(65000)

arquivoSaida.close()
Socket.close()
