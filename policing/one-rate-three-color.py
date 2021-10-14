import threading #thread module imported
import time #time module
import socket
import lib.packet_processing as pp

def saveInfosCA():
    global ca_n_dropped, ca_n_transmitted, arquivoSaida, greenToRed, yellowToRed, n_Reds, n_Yellows, n_Greens

    saida = '{}__{}__{}__{}__{}__{}__{}'.format(ca_n_transmitted, ca_n_dropped, n_Reds, n_Yellows, n_Greens, greenToRed, yellowToRed)
    arquivoSaida.write(saida)
    arquivoSaida.close() 

def saveInfos():
    global n_dropped, n_transmitted, arquivoSaida

    saida = '{}__{}'.format(n_transmitted, n_dropped)
    arquivoSaida.write(saida)
    arquivoSaida.close() 

def colorAware(message, color):
    global ca_bucketF_size, ca_bucketS_size, ca_dropped, serverSocket, n_Reds, n_Yellows, n_Greens, ca_n_transmitted, ca_n_dropped
    [contentReceived, originAddress] = message
    packet_size = pp.ipPacketSize(contentReceived)
    if color == "Green":
        n_Greens += 1
        if ca_bucketF_size < packet_size:
            ca_dropped.append(contentReceived)
            if debug: 
                print("ColorAware: Red")
                greenToRed += 1
                ca_n_dropped += 1
                if pp.numberPacketsProcessed(ca_n_transmitted, ca_n_dropped, 300): saveInfosCA()
        else:
            ca_bucketF_size -= packet_size
            serverSocket.send(contentReceived)
            if debug: 
                print("ColorAware: Green")
                n_transmitted +=1
                if pp.numberPacketsProcessed(ca_n_transmitted, ca_n_dropped, 300): saveInfosCA()
    elif color == "Yellow":
        n_Yellows += 1
        if ca_bucketS_size < packet_size:
            ca_dropped.append(contentReceived)
            if debug: 
                print("ColorAware: Red")
                yellowToRed += 1
                ca_n_dropped += 1
                if pp.numberPacketsProcessed(ca_n_transmitted, ca_n_dropped, 300): saveInfosCA()
        else:
            serverSocket.send(contentReceived)
            ca_bucketS_size -= packet_size
            if debug: 
                print("ColorAware: Yellow")
                n_transmitted +=1
                if pp.numberPacketsProcessed(ca_n_transmitted, ca_n_dropped, 300): saveInfosCA()

    else:
        n_Reds += 1
        ca_dropped.append(message)
        if debug: 
            print("ColorAware: Red")
            ca_n_dropped += 1
            if pp.numberPacketsProcessed(ca_n_transmitted, ca_n_dropped, 300): saveInfosCA()


def colorAwareBucketRate():
    global ca_bucketF_size, ca_bucketS_size, ca_rate, ca_bucketF_max_size, ca_bucketS_max_size
    ca_bucketF_size = ca_bucketF_size + ca_rate if ca_bucketF_size + ca_rate <= ca_bucketF_max_size else ca_bucketF_max_size
    ca_bucketS_size = ca_bucketS_size + ca_rate if ca_bucketS_size + ca_rate <= ca_bucketS_max_size else ca_bucketS_max_size

def thread_Time(thread_name, interval):
    global semaphore, rate, bucketF_size, bucketF_max_size, bucketS_size, bucketS_max_size
    while 1: #Ver condicao do while
        semaphore.acquire()
        bucketF_size = bucketF_size + rate if bucketF_size + rate <= bucketF_max_size else bucketF_max_size
        bucketS_size = bucketS_size + rate if bucketS_size + rate <= bucketS_max_size else bucketS_max_size
        if color_aware: colorAwareBucketRate()
        semaphore.release()
        time.sleep(interval)

def thread_OneRateThreeColor():
#Funcao que quando chega pacote e nao tem pacotes na fila entao envia ou adiciona na fila
    global clientSocket, serverSocket, bucketF_size, semaphore, bucketS_size, dropped, debug, n_transmitted, n_dropped
    while 1:
        contentReceived = clientSocket.recv(65000)
        if (pp.packetAnalysis(contentReceived, serverSocket) == 1):
            packet_size = pp.ipPacketSize(contentReceived)
            semaphore.acquire()
            if bucketF_size < packet_size:
                if bucketS_size < packet_size:
                    if color_aware:
                        if debug: print("Mensagem marcada: Red")
                        colorAware(message, "Red")
                    else:
                        if debug: print("Red Action")
                        n_dropped += 1
                        if pp.numberPacketsProcessed(n_transmitted, n_dropped, 300): saveInfos()
                        dropped.append(contentReceived)
                else:
                    if color_aware:
                        if debug: print("Mensagem marcada: Yellow")
                        colorAware(message, "Yellow")
                    else:
                        serverSocket.send(contentReceived)
                        if debug: 
                            print("Yellow Action")
                            n_transmitted += 1
                            if pp.numberPacketsProcessed(n_transmitted, n_dropped, 300): saveInfos()
                    bucketS_size -= packet_size
            else:
                if color_aware:
                    if debug: print("Mensagem marcada: Green")
                    colorAware(message, "Green")
                else:
                    serverSocket.send(contentReceived)
                    if debug: 
                        print("Green Action")
                         n_transmitted += 1
                        if pp.numberPacketsProcessed(n_transmitted, n_dropped, 300): saveInfos()
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
    if debug:
        greenToRed = 0
        yellowToRed = 0
        ca_n_dropped = 0
        ca_n_transmitted = 0
        n_transmitted = 0
        n_dropped = 0
        n_Greens = 0
        n_Reds = 0
        n_Yellows = 0
        arquivoSaida = open('srTCM_CA-{}-{}-{}.csv'.format(rate, ca_bucketF_max_size, ca_bucketS_max_size), 'w')
else:
    ca_bucketF_size = 0
    ca_bucketF_max_size = 0
    ca_bucketS_size = 0
    ca_bucketS_max_size = 0
    ca_rate = 0
    ca_dropped = []
    if debug:
        n_transmitted = 0
        n_dropped = 0
        arquivoSaida = open('srTCM-{}-{}-{}.csv'.format(rate, bucketF_max_size, bucketS_max_size), 'w')

clientSocket = pp.socketStart(client_interface)
serverSocket = pp.socketStart(server_interface)

semaphore = threading.Semaphore(1)
timer = threading.Thread(target=thread_Time, args=('timer', interval))
one_rate_three_color = threading.Thread(target=thread_OneRateThreeColor, args=())

timer.start()
one_rate_three_color.start()
