import threading #thread module imported
import time #time module
import socket
import lib.packet_processing as pp

def saveInfos():
    global n_dropped, n_transmitted, arquivoSaida, done, n_delay

    total = n_dropped + n_transmitted
    if ((total >= 500) and (done == 0)):
        saida = '{}__{}__{}'.format(n_transmitted, n_dropped, n_delay)
        arquivoSaida.write(saida)
        done = 1
        arquivoSaida.close() 

def consumeQueue():
    global queue, serverSocket, bucket_size, debug,  n_transmitted, last_number_message_transmitted, n_delay, sum_delay
    sentQueue = 0
    if (len(queue) == 0):
        return
    while sentQueue == 0:
        [contentReceived, originAddress] = queue[0]
        packet_size = pp.ipPacketSize(contentReceived)
        if packet_size <= bucket_size:
            if debug: 
                print("Transmitindo pacote da fila")
                n_transmitted += 1
                message_number = position.pop(0)
                sum_delay += pp.packetDelay(last_number_message_transmitted, message_number) - 1
                n_delay = soma_delay/n_transmitted
            serverSocket.send(contentReceived)
            bucket_size -= packet_size
            if (len(queue) == 0):
                sentQueue = 1
        else:
            sentQueue = 1
    saveInfos()

def thread_Time(thread_name, interval):
    global semaphore, rate, bucket_size, bucket_max_size
    while 1: #Ver condicao do while
        semaphore.acquire()
        bucket_size += rate if bucket_size + rate <= bucket_max_size else bucket_max_size
        consumeQueue()
        semaphore.release()
        time.sleep(interval)

def thread_TokenBucket():
#Funcao que quando chega pacote e nao tem pacotes na fila entao envia ou adiciona na fila
    global clientSocket, serverSocket, bucket_size, semaphore, bucket_max_size, queue, queue_max_size, debug, n_transmitted

    n_message = 0
    while 1:
        message = clientSocket.recvfrom(65000)
        [contentReceived, originAddress] = message
        if (pp.packetAnalysis(contentReceived) == 1):
            n_message += 1
            packet_size = pp.ipPacketSize(contentReceived)
            semaphore.acquire()
            if bucket_size < packet_size:
                consumeQueue()
                if len(queue) < queue_max_size:
                    queue.append(message)
                    if debug:
                        position.append(n_message)
                else:
                    if debug: 
                        print("Mensagem dropada")
                        n_dropped += 1
            else:
                if debug: 
                    print("Transmitindo pacote")
                    n_transmitted += 1
                    last_number_message_transmitted = n_message
                serverSocket.send(contentReceived)
                bucket_size -= packet_size
                consumeQueue()
        saveInfos()
        semaphore.release()

queue = []

#rate = 50
#bucket_size = 100
#bucket_max_size = 200
#interval = 0.5
#queue_max_size = 25
#interface = 'wlp0s20f3'
#debug = 1

#__PARAMETERS__

if debug:
    n_transmitted = 0
    n_dropped = 0
    n_delay = 0
    sum_delay = 0
    position = []
    last_number_message_transmitted = 0
    arquivoSaida = open('tokenBucketS-{}-{}.csv'.format(rate, bucket_max_size), 'w')

clientSocket = pp.socketStart(client_interface)
serverSocket = pp.socketStart(server_interface)

semaphore = threading.Semaphore(1)
timer = threading.Thread(target=thread_Time, args=('timer', interval))
token_bucket = threading.Thread(target=thread_TokenBucket, args=())

timer.start()
token_bucket.start()
