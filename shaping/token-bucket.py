import threading #thread module imported
import time #time module
import socket
import lib.packet_processing as pp

def saveInfos():
    global n_dropped, n_transmitted, arquivoSaida, n_delay

    saida = '{}__{}__{}'.format(n_transmitted, n_dropped, n_delay)
    arquivoSaida.write(saida)
    arquivoSaida.close()
    semaphore.release()
    exit() 

def consumeQueue():
    global queue, serverSocket, bucket_size, debug,  n_transmitted, n_delay, sum_delay, queue_transmissions
    sentQueue = 0
    if (len(queue) == 0):
        return
    while sentQueue == 0:
        contentReceived = queue[0]
        packet_size = pp.ipPacketSize(contentReceived)
        if packet_size <= bucket_size:
            serverSocket.send(queue.pop(0))
            bucket_size -= packet_size
            if debug: 
                queue_time_out = time.time()
                print("Transmitindo pacote da fila")
                n_transmitted += 1
                queue_transmissions += 1
                queue_time_in = times_queue.pop(0)
                sum_delay += queue_time_out - queue_time_in
                n_delay = sum_delay/queue_transmissions
                if pp.numberPacketsProcessed(n_transmitted, n_dropped, 500): saveInfos()
            if (len(queue) == 0):
                sentQueue = 1
        else:
            sentQueue = 1

def thread_Time(thread_name, interval):
    global semaphore, rate, bucket_size, bucket_max_size
    while 1: #Ver condicao do while
        semaphore.acquire()
        consumeQueue()
        bucket_size = bucket_size + rate if bucket_size + rate <= bucket_max_size else bucket_max_size
        if debug:
            if pp.numberPacketsProcessed(n_transmitted, n_dropped, 500): exit()
        semaphore.release()
        time.sleep(interval)

def thread_TokenBucket():
#Funcao que quando chega pacote e nao tem pacotes na fila entao envia ou adiciona na fila
    global clientSocket, serverSocket, bucket_size, semaphore, bucket_max_size, queue, queue_max_size, debug, n_transmitted, n_dropped, n_received

    while 1:
        if debug:
            if n_received == 500: exit()
        contentReceived = clientSocket.recv(65535)
        if (pp.packetAnalysis(contentReceived, serverSocket) == 1):
            n_received += 1
            packet_size = pp.ipPacketSize(contentReceived)
            semaphore.acquire()
            if bucket_size < packet_size:
                consumeQueue()
                if len(queue) < queue_max_size:
                    queue.append(contentReceived)
                    if debug:
                        time_in = time.time()
                        print("Mensagem adicionada na fila")
                        times_queue.append(time_in)
                else:
                    if debug: 
                        print("Mensagem dropada")
                        n_dropped += 1
                        if pp.numberPacketsProcessed(n_transmitted, n_dropped, 500): saveInfos()
            else:
                if debug: 
                    print("Transmitindo pacote")
                    n_transmitted += 1
                    if pp.numberPacketsProcessed(n_transmitted, n_dropped, 500): saveInfos()
                serverSocket.send(contentReceived)
                bucket_size -= packet_size
                consumeQueue()
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
    n_received = 0
    queue_transmissions = 0
    n_dropped = 0
    n_delay = 0
    sum_delay = 0
    times_queue = []
    arquivoSaida = open('tokenBucketS-{}-{}.csv'.format(rate, bucket_max_size), 'w')

clientSocket = pp.socketStart(client_interface)
serverSocket = pp.socketStart(server_interface)

semaphore = threading.Semaphore(1)
timer = threading.Thread(target=thread_Time, args=('timer', interval))
token_bucket = threading.Thread(target=thread_TokenBucket, args=())

timer.start()
token_bucket.start()
