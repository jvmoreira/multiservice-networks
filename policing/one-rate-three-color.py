import threading #thread module imported
import time #time module
import socket

def thread_Time(thread_name, interval):
    global semaphore, rate, bucketF_size, bucketF_max_size, bucketS_size, bucketS_max_size
    while 1: #Ver condicao do while
        semaphore.acquire()
        bucketF_size += rate if bucketF_size + rate <= bucketF_max_size else bucketF_max_size
        bucketS_size += rate if bucketS_size + rate <= bucketS_max_size else bucketS_max_size
        semaphore.release()
        time.sleep(interval)

def thread_TokenBucket():
#Funcao que quando chega pacote e nao tem pacotes na fila entao envia ou adiciona na fila
    global Socket, bucketF_size, semaphore, bucketF_max_size, bucketS_size, bucketS_max_size, dropped
    while 1:
        message = Socket.recvfrom(65000)
        [contentReceived, originAddress] = message
        packet_size = int(contentReceived.decode())
        semaphore.acquire()
        if bucketF_size < packet_size:
            if bucketS_size < packet_size:
                dropped.append(message)
                print("Mensagem dropada(Red): " + str(message))
            else:
                print("Transmitindo pacote(Yellow): " + str(message))
                bucketS_size -= packet_size
        else:
            print("Transmitindo pacote(Green):" + str(message))
            bucketF_size -= packet_size
        semaphore.release()

dropped = []

# rate = 2
# bucketF_size = 20
# bucketF_max_size = 30
# bucketS_size = 20
# bucketS_max_size = 30
# interval = 1.0
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