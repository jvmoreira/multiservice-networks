import threading #thread module imported
import time #time module
import socket

def consumeBucket():
    global bucket, packets_to_release, Socket
    if (len(bucket) == 0):
        return
    while (len(bucket)) and (packets_to_release > 0):
        print("Transmitindo pacote " + str(bucket.pop(0)))
        packets_to_release -= 1

def thread_Time(thread_name, interval):
    global semaphore, packets_to_release
    while 1: #Ver condicao do while
        semaphore.acquire()
        packets_to_release = 3
        consumeBucket()
        semaphore.release()
        time.sleep(interval)

def thread_LeakyBucket():
#Funcao que quando chega pacote e nao tem pacotes na fila entao envia ou adiciona na fila
    global Socket, packets_to_release, bucket, semaphore, bucket_max_size
    while 1:
        message = Socket.recvfrom(65000)
        [contentReceived, originAddress] = message
        if len(bucket):
            if len(bucket) < bucket_max_size:
                bucket.append(message)
                '''#Talvez consumir a fila, evitando dropar pacotes
                semaphore.aquire()
                consumeBucket()
                semaphore.release()'''
            else:
                print("Mensagem dropada: " + str(message))
        else:
            semaphore.acquire()
            if packets_to_release > 0:
                print("Transmitindo pacote " + str(message))
                packets_to_release -= 1
            else:
                bucket.append(message)
            semaphore.release()

bucket = []

# packets_to_release = 3
# bucket_max_size = 30
# interval = 0.3
# host_address = '127.0.0.1'
# target_address = 0

#__PARAMETERS__

Socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
Socket.bind((host_address, 8005))

semaphore = threading.Semaphore(1)
timer = threading.Thread(target=thread_Time, args=('timer', interval))
leaky_bucket = threading.Thread(target=thread_LeakyBucket, args=())

timer.start()
leaky_bucket.start()

for i in range(0, 10):
    message = ("Mensagem: " + str(i)).encode()
    Socket.sendto(message, (host_address, 8005))
