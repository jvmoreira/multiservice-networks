import threading #thread module imported
import time #time module
import socket
import lib.packet_processing as pp
import sys

def saveInfosCA():
    global ca_n_dropped, ca_n_transmitted, arquivoSaida, greenToRed, yellowToRed, greenToYellow, n_Reds, n_Yellows, n_Greens

    saida = '{}__{}__{}__{}__{}__{}__{}__{}'.format(ca_n_transmitted, ca_n_dropped, n_Reds, n_Yellows, n_Greens, greenToRed, yellowToRed, greenToYellow)
    arquivoSaida.write(saida)
    arquivoSaida.close()
    semaphore_ca.release()
    exit()  

def saveInfos():
    global n_dropped, n_transmitted, arquivoSaida, n_Reds, n_Yellows, n_Greens

    saida = '{}__{}__{}__{}__{}'.format(n_transmitted, n_dropped, n_Reds, n_Yellows, n_Greens)
    arquivoSaida.write(saida)
    arquivoSaida.close()
    semaphore_trTCM.release()
    exit() 

def colorAware(contentReceived, color):
    global ca_bucketF_size, ca_bucketS_size, ca_dropped, serverSocket, ca_n_transmitted, ca_n_dropped, n_Reds, n_Yellows, n_Greens, greenToRed, yellowToRed, color_awares, semaphore_ca
    
    packet_size = pp.ipPacketSize(contentReceived)
    semaphore_ca.acquire()
    if color == "Red":
        n_Reds += 1
        ca_dropped.append(contentReceived)
        if debug: 
            print("ColorAware: Red")
            ca_n_dropped += 1
            if pp.numberPacketsProcessed(ca_n_transmitted, ca_n_dropped, 500): saveInfosCA()
    else:
        if ca_bucketS_size < packet_size:
            ca_dropped.append(contentReceived)
            if debug: 
                print("ColorAware: Red")
                if color == "Green":
                    n_Greens += 1
                    greenToRed += 1
                else:
                    n_Yellows += 1
                    yellowToRed += 1
                ca_n_dropped += 1
                if pp.numberPacketsProcessed(ca_n_transmitted, ca_n_dropped, 500): saveInfosCA()
        else:
            if color == "Yellow":
                n_Yellows += 1
                ca_bucketS_size -= packet_size
                serverSocket.send(contentReceived)
                if debug: 
                    print("ColorAware: Yellow")
                    ca_n_transmitted +=1
                    if pp.numberPacketsProcessed(ca_n_transmitted, ca_n_dropped, 500): saveInfosCA()
            else:
                n_Greens += 1 
                if ca_bucketF_size < packet_size:
                    serverSocket.send(contentReceived)
                    ca_bucketS_size -= packet_size
                    if debug: 
                        print("ColorAware: Yellow")
                        ca_n_transmitted +=1
                        greenToYellow += 1
                        if pp.numberPacketsProcessed(ca_n_transmitted, ca_n_dropped, 500): saveInfosCA()
                else:
                    if debug: 
                        print("ColorAware: Green")
                        ca_n_transmitted +=1
                        if pp.numberPacketsProcessed(ca_n_transmitted, ca_n_dropped, 500): saveInfosCA()
                    serverSocket.send(contentReceived)
                    ca_bucketF_size -= packet_size
                    ca_bucketS_size -= packet_size
    color_awares.pop(0)
    semaphore_ca.release()
    exit()

def colorAwareBucketsRates():
    global ca_bucketF_size, ca_bucketS_size, ca_rateF, ca_rateS, ca_bucketF_max_size, ca_bucketS_max_size
    ca_bucketF_size = ca_bucketF_size + ca_rateF if ca_bucketF_size + ca_rateF <= ca_bucketF_max_size else ca_bucketF_max_size
    ca_bucketS_size = ca_bucketS_size + ca_rateS if ca_bucketS_size + ca_rateS <= ca_bucketS_max_size else ca_bucketS_max_size

def thread_Time(thread_name, interval):
    global semaphore_trTCM, rateS, rateF, bucketF_size, bucketF_max_size, bucketS_size, bucketS_max_size
    
    while 1: #Ver condicao do while
        semaphore_trTCM.acquire()
        semaphore_ca.acquire()
        bucketF_size = bucketF_size + rateF if bucketF_size + rateF <= bucketF_max_size else bucketF_max_size
        bucketS_size = bucketS_size + rateS if bucketS_size + rateS <= bucketS_max_size else bucketS_max_size
        if color_aware: colorAwareBucketsRates()
        if debug:
            if color_aware:
                if pp.numberPacketsProcessed(ca_n_transmitted, ca_n_dropped, 500): exit()
            else:
                if pp.numberPacketsProcessed(n_transmitted, n_dropped, 500): exit()
        semaphore_ca.release()
        semaphore_trTCM.release()
        time.sleep(interval)

def thread_TwoRateThreeColor():
#Funcao que quando chega pacote e nao tem pacotes na fila entao envia ou adiciona na fila
    global clientSocket, serverSocket, bucketF_size, semaphore_trTCM, bucketF_max_size, bucketS_size, bucketS_max_size, dropped, n_transmitted, n_dropped, n_Reds, n_Yellows, n_Greens, color_awares

    while 1:
        if debug:
            if color_aware:
                if n_transmitted == 500: exit()
        contentReceived = clientSocket.recv(65535)
        if (pp.packetAnalysis(contentReceived, serverSocket) == 1):
            if debug:
                if color_aware: n_transmitted += 1
            packet_size = pp.ipPacketSize(contentReceived)
            semaphore_trTCM.acquire()
            if bucketS_size < packet_size:
                if color_aware:
                    if debug: print("Mensagem marcada: Red")
                    color_awares.append(threading.Thread(target=colorAware, args=(contentReceived, "Red")))
                    color_awares[-1].start()
                else:
                    if debug: 
                        print("Red Action")
                        n_dropped += 1
                        n_Reds += 1
                        if pp.numberPacketsProcessed(n_transmitted, n_dropped, 500): saveInfos()
                    dropped.append(contentReceived)
            else:
                if bucketF_size < packet_size:
                    if color_aware:
                        if debug: print("Mensagem maracada: Yellow")
                        color_awares.append(threading.Thread(target=colorAware, args=(contentReceived, "Yellow")))
                        color_awares[-1].start()
                    else:
                        if debug: 
                            print("Yellow Action")
                            n_transmitted += 1
                            n_Yellows += 1
                            if pp.numberPacketsProcessed(n_transmitted, n_dropped, 500): saveInfos()
                        serverSocket.send(contentReceived)
                    bucketS_size -= packet_size
                else:
                    if color_aware:
                        if debug: print("Mensagem maracada: Green")
                        color_awares.append(threading.Thread(target=colorAware, args=(contentReceived, "Green")))
                        color_awares[-1].start()
                    else:
                        if debug: 
                            print("Green Action")
                            n_transmitted += 1
                            n_Greens += 1
                            if pp.numberPacketsProcessed(n_transmitted, n_dropped, 500): saveInfos()
                        serverSocket.send(contentReceived)
                    bucketF_size -= packet_size
                    bucketS_size -= packet_size
            semaphore_trTCM.release()

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
    color_awares = []
    if debug:
        greenToRed = 0
        yellowToRed = 0
        greenToYellow = 0
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
    color_awares = []
    if debug:
        n_transmitted = 0
        n_dropped = 0
        n_Greens = 0
        n_Reds = 0
        n_Yellows = 0
        arquivoSaida = open('trTCM-{}-{}-{}-{}.csv'.format(rateF, rateS, bucketF_max_size, bucketS_max_size), 'w')

clientSocket = pp.socketStart(client_interface)
serverSocket = pp.socketStart(server_interface)

semaphore_trTCM = threading.Semaphore(1)
semaphore_ca = threading.Semaphore(1)
timer = threading.Thread(target=thread_Time, args=('timer', interval))
two_rate_three_color = threading.Thread(target=thread_TwoRateThreeColor, args=())

timer.start()
two_rate_three_color.start()
