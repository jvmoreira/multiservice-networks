import threading #thread module imported
import time #time module
import socket
import lib.packetProcessing as pp

def thread_Time(thread_name, interval):
    global semaphore, rate, bucket_size, bucket_max_size
    while 1:
        semaphore.acquire()
        bucket_size += rate if bucket_size + rate <= bucket_max_size else bucket_max_size
        semaphore.release()
        time.sleep(interval)
        
def thread_TokenBucket():
#Funcao que quando chega pacote e nao tem pacotes na fila entao envia ou adiciona na fila
    global Socket, bucket_size, semaphore, bucket_max_size, dropped, debug
    while 1:
        message = Socket.recvfrom(65000)
        [contentReceived, originAddress] = message
        packet_size = pp.ipPacketSize(contentReceived)
        semaphore.acquire()
        if bucket_size < packet_size:
            dropped.append(message)
            if debug: print("Mensagem dropada")
        else:
            if debug: print("Transmitindo pacote")
            bucket_size -= packet_size
        semaphore.release()

dropped = []

#rate = 50
#bucket_size = 100
#bucket_max_size = 200
#interval = 0.5
#interface = 'wlp0s20f3'
#debug = 1

#__PARAMETERS__

Socket = pp.socketStart(interface)

semaphore = threading.Semaphore(1)
timer = threading.Thread(target=thread_Time, args=('timer', interval))
token_bucket = threading.Thread(target=thread_TokenBucket, args=())

timer.start()
token_bucket.start()