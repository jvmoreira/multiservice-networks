//VNF_HEADER
//VNF_VERSION: 1.0
//VNF_ID: 979eaf94-ad8c-4aef-90fa-c29189b42fde
//VNF_PROVIDER: UFPR
//VNF_NAME: Content Find
//VNF_RELEASE_DATE: 2020-11-08 11-45-45
//VNF_RELEASE_VERSION: 1.0
//VNF_RELEASE_LIFESPAN: 2020-11-09 11-45-45
//VNF_DESCRIPTION: Find a required content in a CDN pool
//VNF_FRAMEWORK: Python2
//VNF_NETWORK: VirtIO
import socket

def nf_stop(token):
    Socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    Socket.sendto('end_main', ('192.168.122.40', 8005))

    print('Sent: STOP!')
    Socket.close()
    return

def informMessageWasDropped(Socket, Address):
    Socket.sendto('Package dropped', Address)

def nf_main(token):
    print('Server Started')

    bucket = 50
    rate = 3

    Socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    Socket.bind(('192.168.122.40', 8005))

    while(token[0]):

        [contentReceived, originAddress] = Socket.recvfrom(65000)

        if(contentReceived == 'end_main'):
            Socket.close()
            print('Received: STOP!')
        elif '_reset' in contentReceived[0:6]:
            bucket = 50
            options = contentReceived.split(' ')[1:]
            rate = int( options[0].split('=')[1] )
            print('\n\nRefilling bucket with rate {}...\n'.format(rate))
        else:
            bytesReceived = len(contentReceived)
            padding = ' ' * (15-bytesReceived)
            #print('Received = {}{} | Size = {:02d} | Bucket = {:02d} | From = {}'.format(contentReceived, padding, bytesReceived, bucket, originAddress))

            if(bytesReceived > bucket):
                informMessageWasDropped(Socket, originAddress)
            else:
                bucket = bucket - bytesReceived

                contentToSend = '`{}` - OK'.format(contentReceived)
                Socket.sendto(contentToSend, originAddress)

            bucket = bucket + rate if bucket + rate <= 50 else 50
