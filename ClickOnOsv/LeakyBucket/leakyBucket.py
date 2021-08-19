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

def nf_main(token):
    print('Server Started')

    bucketSize = 100
    rate = 1
    interval = 0.3141
    lastPacketTime = 0

    allPackets = []

    Socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    Socket.bind(('192.168.122.40', 8005))

    while(token[0]):

        [contentReceived, originAddress] = Socket.recvfrom(65000)

        if(contentReceived == 'end_main'):
            Socket.close()
            print('Received: STOP!')
        elif '_end' in  contentReceived:
            bucket = []
            packetsSent = []
            packetsDropped = []
            lastPacketTime = 0
            intervalsElapsed = 0

            for packet in allPackets:
                [packetSize, packetTime] = packet.split('__')
                timeElapsed = packetTime - lastPacketTime

                packetsToTransmit = (int(packetTime / interval) * rate) - intervalsElapsed


                # Transmit existing packets
                for i in range(0, packetsToTransmit):
                    if len(bucket):
                            packetsSent.append(bucket.pop(0))
                    intervalsElapsed += 1


                # Process current packet
                if len(bucket) < bucketSize:
                    bucket.append(packet)
                else:
                    packetsDroppend.append(packet)

                lastPacketTime = packetTime

        else:
            allPackets.append(contentReceived)
