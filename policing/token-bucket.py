import threading #thread module imported
import time #time module
import socket
import lib.packet_processing as pp

def saveInfos():
    global n_dropped, n_transmitted, arquivoSaida

    saida = '{}__{}'.format(n_transmitted, n_dropped)
    arquivoSaida.write(saida)
    arquivoSaida.close() 

def thread_Time(thread_name, interval):
    global semaphore, rate, bucket_size, bucket_max_size
    while 1:
        semaphore.acquire()
        bucket_size =  bucket_size + rate if bucket_size + rate <= bucket_max_size else bucket_max_size
        semaphore.release()
        time.sleep(interval)

def thread_TokenBucket():
#Funcao que quando chega pacote e nao tem pacotes na fila entao envia ou adiciona na fila
    global clientSocket, serverSocket, bucket_size, semaphore, bucket_max_size, dropped, debug, n_transmitted, n_dropped
    while 1:
        contentReceived = clientSocket.recv(65535)
        if (pp.packetAnalysis(contentReceived, serverSocket) == 1):
            packet_size = pp.ipPacketSize(contentReceived)
            semaphore.acquire()
            if bucket_size < packet_size:
                dropped.append(contentReceived)
                if debug: 
                    print("Mensagem dropada")
                    n_dropped += 1
                    if pp.numberPacketsProcessed(n_transmitted, n_dropped, 300): saveInfos()
            else:
                if debug: 
                    print("Transmitindo pacote")
                    n_transmitted += 1
                    if pp.numberPacketsProcessed(n_transmitted, n_dropped, 300): saveInfos()
                serverSocket.send(contentReceived)
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

if debug:
    n_transmitted = 0
    n_dropped = 0
    arquivoSaida = open('tokenBucketPolicer-{}-{}.csv'.format(rate, bucket_max_size), 'w')

clientSocket = pp.socketStart(client_interface)
serverSocket = pp.socketStart(server_interface)

semaphore = threading.Semaphore(1)
timer = threading.Thread(target=thread_Time, args=('timer', interval))
token_bucket = threading.Thread(target=thread_TokenBucket, args=())

timer.start()
token_bucket.start()
