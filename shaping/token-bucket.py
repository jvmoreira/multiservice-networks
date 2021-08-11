import threading #thread module imported
import time #time module
import socket

def consumeQueue():
    global queue, Socket, bucket_size
    sentQueue = 0
    if (len(queue) == 0):
        return
    while sentQueue == 0:
        [contentReceived, originAddress] = queue[0]
        packet_size = int(contentReceived.decode())
        if packet_size <= bucket_size:
            print("Transmitindo pacote " + str(queue.pop(0)))
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
    global Socket, bucket_size, semaphore, bucket_max_size, queue, queue_max_size
    while 1:
        message = Socket.recvfrom(65000)
        [contentReceived, originAddress] = message
        packet_size = int(contentReceived.decode())
        semaphore.acquire()
        if bucket_size < packet_size:
            consumeQueue()
            if len(queue) < queue_max_size:
                queue.append(message)
            else:
                print("Mensagem dropada: " + str(message))
        else:
            print("Transmitindo pacote " + str(message))
            bucket_size -= packet_size
            consumeQueue()
        semaphore.release()

queue = []

# rate = 2
# bucket_size = 20
# bucket_max_size = 30
# interval = 1.0
# queue_max_size = 20
# host_address = '127.0.0.1'
# target_address = 0

#__PARAMETERS__

Socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
Socket.bind((host_address, 8005))

semaphore = threading.Semaphore(1)
timer = threading.Thread(target=thread_Time, args=('timer', interval))
token_bucket = threading.Thread(target=thread_TokenBucket, args=())

timer.start()
token_bucket.start()

for i in range(1, 11):
    message = str(i).encode()
    Socket.sendto(message, (host_address, 8005))