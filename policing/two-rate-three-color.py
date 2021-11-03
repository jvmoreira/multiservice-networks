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
    global n_dropped, n_transmitted, arquivoSaida, n_Reds, n_Yellows, n_Greens

    saida = '{}__{}__{}__{}__{}'.format(n_transmitted, n_dropped, n_Reds, n_Yellows, n_Greens)
    arquivoSaida.write(saida)
    arquivoSaida.close() 

def colorAware(message, color):
    global ca_bucketF_size, ca_bucketS_size, ca_dropped, serverSocket, ca_n_transmitted, ca_n_dropped, n_Reds, n_Yellows, n_Greens
    [contentReceived, originAddress] = message
    packet_size = pp.ipPacketSize(contentReceived)
    if color == "Red":
        n_Reds += 1
        ca_dropped.append(contentReceived)
        if debug: 
            print("ColorAware: Red")
            ca_n_dropped += 1
            if pp.numberPacketsProcessed(ca_n_transmitted, ca_n_dropped, 300): saveInfosCA()
    else:
        if ca_bucketS_size < packet_size:
            ca_dropped.append(contentReceived)
            if debug: 
                print("ColorAware: Red")
                ca_n_dropped += 1
                if pp.numberPacketsProcessed(ca_n_transmitted, ca_n_dropped, 300): saveInfosCA()
        else:
            if color == "Yellow":
                n_Yellows += 1
                ca_bucketS_size -= packet_size
                serverSocket.send(contentReceived)
                if debug: 
                    print("ColorAware: Yellow")
                    n_transmitted +=1
                    if pp.numberPacketsProcessed(ca_n_transmitted, ca_n_dropped, 300): saveInfosCA()
            else:
                n_Greens += 1 
                if ca_bucketF_size < packet_size:
                    serverSocket.send(contentReceived)
                    ca_bucketS_size -= packet_size
                    if debug: 
                        print("ColorAware: Yellow")
                        n_transmitted +=1
                        if pp.numberPacketsProcessed(ca_n_transmitted, ca_n_dropped, 300): saveInfosCA()
                else:
                    if debug: 
                        print("ColorAware: Green")
                        n_transmitted +=1
                        if pp.numberPacketsProcessed(ca_n_transmitted, ca_n_dropped, 300): saveInfosCA()
                    serverSocket.send(contentReceived)
                    ca_bucketF_size -= packet_size
                    ca_bucketS_size -= packet_size

def colorAwareBucketsRates():
    global ca_bucketF_size, ca_bucketS_size, ca_rateF, ca_rateS, ca_bucketF_max_size, ca_bucketS_max_size
    ca_bucketF_size = ca_bucketF_size + ca_rateF if ca_bucketF_size + ca_rateF <= ca_bucketF_max_size else ca_bucketF_max_size
    ca_bucketS_size = ca_bucketS_size + ca_rateS if ca_bucketS_size + ca_rateS <= ca_bucketS_max_size else ca_bucketS_max_size

def thread_Time(thread_name, interval):
    global semaphore, rateS, rateF, bucketF_size, bucketF_max_size, bucketS_size, bucketS_max_size
    while 1: #Ver condicao do while
        semaphore.acquire()
        bucketF_size = bucketF_size + rateF if bucketF_size + rateF <= bucketF_max_size else bucketF_max_size
        bucketS_size = bucketS_size + rateS if bucketS_size + rateS <= bucketS_max_size else bucketS_max_size
        if color_aware: colorAwareBucketsRates()
        semaphore.release()
        time.sleep(interval)

def thread_TwoRateThreeColor():
#Funcao que quando chega pacote e nao tem pacotes na fila entao envia ou adiciona na fila
    global clientSocket, serverSocket, bucketF_size, semaphore, bucketF_max_size, bucketS_size, bucketS_max_size, dropped, n_transmitted, n_dropped
    while 1:
        contentReceived = clientSocket.recv(65535)
        if (pp.packetAnalysis(contentReceived, serverSocket) == 1):
            packet_size = pp.ipPacketSize(contentReceived)
            semaphore.acquire()
            if bucketS_size < packet_size:
                if color_aware:
                    if debug: 
                        print("Mensagem marcada: Red")
                    colorAware(message, "Red")
                else:
                    if debug: 
                        print("Red Action")
                        n_dropped += 1
                        n_Reds += 1
                        if pp.numberPacketsProcessed(n_transmitted, n_dropped, 300): saveInfos()
                    dropped.append(contentReceived)
            else:
                if bucketF_size < packet_size:
                    if color_aware:
                        if debug: print("Mensagem maracada: Yellow")
                        colorAware(message, "Yellow")
                    else:
                        if debug: 
                            print("Yellow Action")
                            n_transmitted += 1
                            n_Yellows += 1
                            if pp.numberPacketsProcessed(n_transmitted, n_dropped, 300): saveInfos()
                        serverSocket.send(contentReceived)
                    bucketS_size -= packet_size
                else:
                    if color_aware:
                        if debug: print("Mensagem maracada: Green")
                        colorAware(message, "Green")
                    else:
                        if debug: 
                            print("Green Action")
                            n_transmitted += 1
                            n_Greens += 1
                            if pp.numberPacketsProcessed(n_transmitted, n_dropped, 300): saveInfos()
                        serverSocket.send(contentReceived)
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
        arquivoSaida = open('trTCM_CA-{}-{}-{}-{}.csv'.format(ca_rateF, ca_rateS, ca_bucketF_max_size, ca_bucketS_max_size), 'w')
else:
    ca_bucketF_size = 0
    ca_bucketF_max_size = 0
    ca_bucketS_size = 0
    ca_bucketS_max_size = 0
    ca_rateF = 0
    ca_rateS = 0
    ca_dropped = []
    if debug:
        n_Greens = 0
        n_Reds = 0
        n_Yellows = 0
        n_transmitted = 0
        n_dropped = 0
        arquivoSaida = open('trTCM-{}-{}-{}-{}.csv'.format(rateF, rateS, bucketF_max_size, bucketS_max_size), 'w')

clientSocket = pp.socketStart(client_interface)
serverSocket = pp.socketStart(server_interface)

semaphore = threading.Semaphore(1)
timer = threading.Thread(target=thread_Time, args=('timer', interval))
two_rate_three_color = threading.Thread(target=thread_TwoRateThreeColor, args=())

timer.start()
two_rate_three_color.start()
