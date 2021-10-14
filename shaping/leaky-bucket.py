import threading #thread module imported
import time #time module
import socket
import lib.packet_processing as pp

def consumeBucket():
    global bucket, packets_to_release, serverSocket, debug, n_transmitted#, last_number_message_transmitted, n_delay, sum_delay
    if (len(bucket) == 0):
        return
    while (len(bucket)) and (packets_to_release > 0):
        if debug: 
            print("Transmitindo pacote fila")
            n_transmitted += 1
            if pp.numberPacketsProcessed(n_transmitted, n_dropped, 300): saveInfos()

        serverSocket.send(bucket.pop(0))
        packets_to_release -= 1

def thread_Time(thread_name, interval):
    global semaphore, packets_to_release, packets_to_release_value
    while 1: #Ver condicao do while
        semaphore.acquire()
        packets_to_release = packets_to_release_value
        consumeBucket()
        semaphore.release()
        time.sleep(interval)

def saveInfos():
    global n_dropped, n_transmitted, arquivoSaida

    saida = '{}__{}'.format(n_transmitted, n_dropped)
    arquivoSaida.write(saida)
    arquivoSaida.close() 

def thread_LeakyBucket():
#Funcao que quando chega pacote e nao tem pacotes na fila entao envia ou adiciona na fila
    global clientSocket, serverSocket, packets_to_release, bucket, semaphore, bucket_max_size, debug, n_delay, n_dropped, n_transmitted, last_number_message_transmitted

    n_message = 0
    while 1:
        contentReceived = clientSocket.recv(65535)
        if (pp.packetAnalysis(contentReceived, serverSocket) == 1):
            n_message += 1
            if len(bucket):
                if len(bucket) < bucket_max_size:
                    if debug: 
                        print("Adicionou na fila e bucket nao vazio")
                    bucket.append(contentReceived)
                else:
                    if debug: 
                        print("Mensagem dropada")
                        n_dropped += 1
                        if pp.numberPacketsProcessed(n_transmitted, n_dropped, 300): saveInfos()
            else:
                semaphore.acquire()
                if packets_to_release > 0:
                    if debug: 
                        print("Transmitindo pacote")
                        n_transmitted += 1
                        if pp.numberPacketsProcessed(n_transmitted, n_dropped, 300): saveInfos()
                    serverSocket.send(contentReceived)
                    packets_to_release -= 1
                else:
                    if debug: 
                        print("Adicionou na fila e bucket vazio")
                    bucket.append(contentReceived)
            semaphore.release()

bucket = []

#packets_to_release = 3
#bucket_max_size = 30
#interval = 0.3
#interface = 'wlp0s20f3'
#debug = 1

#__PARAMETERS__

packets_to_release_value = packets_to_release

if debug:
    n_transmitted = 0
    n_dropped = 0
    arquivoSaida = open('leakybucket-{}.csv'.format(packets_to_release_value), 'w')

clientSocket = pp.socketStart(client_interface)
serverSocket = pp.socketStart(server_interface)

semaphore = threading.Semaphore(1)
timer = threading.Thread(target=thread_Time, args=('timer', interval))
leaky_bucket = threading.Thread(target=thread_LeakyBucket, args=())

timer.start()
leaky_bucket.start()
