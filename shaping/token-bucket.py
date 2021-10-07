import threading #thread module imported
import time #time module
import socket
import lib.packet_processing as pp

def consumeQueue():
    global queue, serverSocket, bucket_size, debug
    sentQueue = 0
    if (len(queue) == 0):
        return
    while sentQueue == 0:
        [contentReceived, originAddress] = queue[0]
        packet_size = pp.ipPacketSize(contentReceived)
        if packet_size <= bucket_size:
            if debug: print("Transmitindo pacote da fila")
            serverSocket.send(contentReceived)
            bucket_size -= packet_size
            if (len(queue) == 0):
                sentQueue = 1
        else:
            sentQueue = 1

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
    global clientSocket, serverSocket, bucket_size, semaphore, bucket_max_size, queue, queue_max_size, debug
    while 1:
        message = clientSocket.recvfrom(65000)
        if (pp.packetAnalysis(message) == 1):
            [contentReceived, originAddress] = message
            packet_size = pp.ipPacketSize(contentReceived)
            semaphore.acquire()
            if bucket_size < packet_size:
                consumeQueue()
                if len(queue) < queue_max_size:
                    queue.append(message)
                else:
                    if debug: print("Mensagem dropada")
            else:
                if debug: print("Transmitindo pacote")
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

clientSocket = pp.socketStart(client_interface)
serverSocket = pp.socketStart(server_interface)

semaphore = threading.Semaphore(1)
timer = threading.Thread(target=thread_Time, args=('timer', interval))
token_bucket = threading.Thread(target=thread_TokenBucket, args=())

timer.start()
token_bucket.start()
