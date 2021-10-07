import threading #thread module imported
import time #time module
import socket
import lib.packet_processing as pp

def colorAware(message, color):
    global ca_bucketF_size, ca_bucketS_size, ca_dropped, serverSocket
    [contentReceived, originAddress] = message
    packet_size = pp.ipPacketSize(contentReceived)
    if color == "Green":
        if ca_bucketF_size < packet_size:
            ca_dropped.append(contentReceived)
            if debug: print("ColorAware: Red")
        else:
            ca_bucketF_size -= packet_size
            serverSocket.send(contentReceived)
            if debug: print("ColorAware: Green")
    elif color == "Yellow":
        if ca_bucketS_size < packet_size:
            ca_dropped.append(contentReceived)
            if debug: print("ColorAware: Red")
        else:
            serverSocket.send(contentReceived)
            ca_bucketS_size -= packet_size
            if debug: print("ColorAware: Yellow")
    else:
        ca_dropped.append(message)
        if debug: print("ColorAware: Red")


def colorAwareBucketRate():
    global ca_bucketF_size, ca_bucketS_size, ca_rate, ca_bucketF_max_size, ca_bucketS_max_size
    ca_bucketF_size += ca_rate if ca_bucketF_size + ca_rate <= ca_bucketF_max_size else ca_bucketF_max_size
    ca_bucketS_size += ca_rate if ca_bucketS_size + ca_rate <= ca_bucketS_max_size else ca_bucketS_max_size

def thread_Time(thread_name, interval):
    global semaphore, rate, bucketF_size, bucketF_max_size, bucketS_size, bucketS_max_size
    while 1: #Ver condicao do while
        semaphore.acquire()
        bucketF_size += rate if bucketF_size + rate <= bucketF_max_size else bucketF_max_size
        bucketS_size += rate if bucketS_size + rate <= bucketS_max_size else bucketS_max_size
        if color_aware: colorAwareBucketRate()
        semaphore.release()
        time.sleep(interval)

def thread_OneRateThreeColor():
#Funcao que quando chega pacote e nao tem pacotes na fila entao envia ou adiciona na fila
    global clientSocket, serverSocket, bucketF_size, semaphore, bucketS_size, dropped, debug
    while 1:
        message = clientSocket.recvfrom(65000)
        if (pp.packetAnalysis(message) == 1):
            [contentReceived, originAddress] = message
            packet_size = pp.ipPacketSize(contentReceived)
            semaphore.acquire()
            if bucketF_size < packet_size:
                if bucketS_size < packet_size:
                    if color_aware:
                        if debug: print("Mensagem marcada: Red")
                        colorAware(message, "Red")
                    else:
                        if debug: print("Red Action")
                        dropped.append(contentReceived)
                else:
                    if color_aware:
                        if debug: print("Mensagem marcada: Yellow")
                        colorAware(message, "Yellow")
                    else:
                        serverSocket.send(contentReceived)
                        if debug: print("Yellow Action")
                    bucketS_size -= packet_size
            else:
                if color_aware:
                    if debug: print("Mensagem marcada: Green")
                    colorAware(message, "Green")
                else:
                    serverSocket.send(contentReceived)
                    if debug: print("Green Action")
                bucketF_size -= packet_size
            semaphore.release()

dropped = []

#rate = 100
#bucketF_size = 1000
#bucketF_max_size = 2000
#bucketS_size = 2000
#bucketS_max_size = 4000
#interval = 1
#interface = 'wlp0s20f3'
#debug = 1
#color_aware = 1
#ca_bucketF_size = 500
#ca_bucketF_max_size = 1000
#ca_bucketS_size = 800
#ca_bucketS_max_size = 1200
#ca_rate = 100

#__PARAMETERS__

if color_aware:
    ca_dropped = []
else:
    ca_bucketF_size = 0
    ca_bucketF_max_size = 0
    ca_bucketS_size = 0
    ca_bucketS_max_size = 0
    ca_rate = 0
    ca_dropped = []

clientSocket = pp.socketStart(client_interface)
serverSocket = pp.socketStart(server_interface)

semaphore = threading.Semaphore(1)
timer = threading.Thread(target=thread_Time, args=('timer', interval))
one_rate_three_color = threading.Thread(target=thread_OneRateThreeColor, args=())

timer.start()
one_rate_three_color.start()
