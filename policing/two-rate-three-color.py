import threading #thread module imported
import time #time module
import socket
import lib.packet_processing as pp

def colorAware(message, color):
    global ca_bucketF_size, ca_bucketS_size, ca_dropped, serverSocket
    [contentReceived, originAddress] = message
    packet_size = pp.ipPacketSize(contentReceived)
    if color == "Red":
        ca_dropped.append(contentReceived)
        if debug: print("ColorAware: Red")
    else:
        if ca_bucketS_size < packet_size:
            ca_dropped.append(contentReceived)
            if debug: print("ColorAware: Red")
        else:
            if color == "Yellow":
                ca_bucketS_size -= packet_size
                serverSocket.send(contentReceived)
                if debug: print("ColorAware: Yellow")
            else:
                if ca_bucketF_size < packet_size:
                    serverSocket.send(contentReceived)
                    ca_bucketS_size -= packet_size
                    if debug: print("ColorAware: Yellow")
                else:
                    if debug: print("ColorAware: Green")
                    serverSocket.send(contentReceived)
                    ca_bucketF_size -= packet_size
                    ca_bucketS_size -= packet_size

def colorAwareBucketsRates():
    global ca_bucketF_size, ca_bucketS_size, ca_rateF, ca_rateS, ca_bucketF_max_size, ca_bucketS_max_size
    ca_bucketF_size += ca_rateF if ca_bucketF_size + ca_rateF <= ca_bucketF_max_size else ca_bucketF_max_size
    ca_bucketS_size += ca_rateS if ca_bucketS_size + ca_rateS <= ca_bucketS_max_size else ca_bucketS_max_size

def thread_Time(thread_name, interval):
    global semaphore, rateS, rateF, bucketF_size, bucketF_max_size, bucketS_size, bucketS_max_size
    while 1: #Ver condicao do while
        semaphore.acquire()
        bucketF_size += rateF if bucketF_size + rateF <= bucketF_max_size else bucketF_max_size
        bucketS_size += rateS if bucketS_size + rateS <= bucketS_max_size else bucketS_max_size
        if color_aware: colorAwareBucketsRates()
        semaphore.release()
        time.sleep(interval)

def thread_TwoRateThreeColor():
#Funcao que quando chega pacote e nao tem pacotes na fila entao envia ou adiciona na fila
    global clientSocket, serverSocket, bucketF_size, semaphore, bucketF_max_size, bucketS_size, bucketS_max_size, dropped
    while 1:
        message = clientSocket.recvfrom(65000)
        if (pp.packetAnalysis(message) == 1):
            [contentReceived, originAddress] = message
            packet_size = pp.ipPacketSize(contentReceived)
            semaphore.acquire()
            if bucketS_size < packet_size:
                if color_aware:
                    if debug: print("Mensagem marcada: Red")
                    colorAware(message, "Red")
                else:
                    if debug: print("Mensagem dropada(Red)")
                    dropped.append(contentReceived)
            else:
                if bucketF_size < packet_size:
                    if color_aware:
                        if debug: print("Mensagem maracada: Yellow")
                        colorAware(message, "Yellow")
                    else:
                        if debug: print("Yellow Action")
                        serverSocket(contentReceived)
                    bucketS_size -= packet_size
                else:
                    if color_aware:
                        if debug: print("Mensagem maracada: Green")
                        colorAware(message, "Green")
                    else:
                        if debug: print("Green Action")
                        serverSocket(contentReceived)
                    bucketF_size -= packet_size
                    bucketS_size -= packet_size
            semaphore.release()

dropped = []

#rateF = 150
#rateS = 200
#bucketF_size = 2000
#bucketF_max_size = 2500
#bucketS_size = 1500
#bucketS_max_size = 3000
#interval = 1.0
#interface = 'wlp0s20f3'
#debug = 1
#color_aware = 1
#ca_bucketF_size = 1000
#ca_bucketF_max_size = 1500
#ca_bucketS_size = 1500
#ca_bucketS_max_size = 3000
#ca_rateF = 200
#ca_rateS = 100

#__PARAMETERS__

if color_aware:
    ca_dropped = []
else:
    ca_bucketF_size = 0
    ca_bucketF_max_size = 0
    ca_bucketS_size = 0
    ca_bucketS_max_size = 0
    ca_rateF = 0
    ca_rateS = 0
    ca_dropped = []

clientSocket = pp.socketStart(client_interface)
serverSocket = pp.socketStart(server_interface)

semaphore = threading.Semaphore(1)
timer = threading.Thread(target=thread_Time, args=('timer', interval))
two_rate_three_color = threading.Thread(target=thread_TwoRateThreeColor, args=())

timer.start()
two_rate_three_color.start()
