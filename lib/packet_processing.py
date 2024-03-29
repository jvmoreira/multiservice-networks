from socket import *
import struct
import binascii
import sys

def unpackFrameEthernet(frame):
    destiny, origin, protocol = struct.unpack('! 6s 6s H', frame[:14])
    return bytesToHexa(destiny), bytesToHexa(origin), htons(protocol), frame[14:]

def bytesToHexa(bytes_address):
    hex_list = []
    address = binascii.hexlify(bytes_address).decode("ascii")
    for i in range(0,12,2):
        hex_list.append(address[i:i+2])
    mac = ":".join(hex_list)
    return mac

def ipPacketData(data):
    ip_data_tuple = struct.unpack("!BBHHHBBH4s4s", data[:20])
    version = ip_data_tuple[0]
    header_len = version >> 4
    service_type = ip_data_tuple[1]
    total_size = ip_data_tuple[2]
    identifier = ip_data_tuple[3]
    offset_fragment = ip_data_tuple[4]
    life_time_ttl = ip_data_tuple[5]
    protocols = ip_data_tuple[6]
    checksum_header = ip_data_tuple[7]
    ip_origin = inet_ntoa(ip_data_tuple[8])
    ip_destiny = inet_ntoa(ip_data_tuple[9])
 
    header_size_bytes = (version & 15) * 4

    return version, header_len, service_type, + \
           total_size, identifier, offset_fragment, + \
           life_time_ttl, protocols, checksum_header, ip_origin, ip_destiny, data[header_size_bytes:] 

def ipPacketSize(frame):
    #destiny, origin, protocol, data = unpackFrameEthernet(frame)
    total_size = len(frame)
    '''Apenas IPV4
    if protocol == 8:
        (version, header_len, service_type,
        total_size, identifier, offset_fragment,
        life_time_ttl, protocols, checksum_header,
        ip_origin, ip_destiny, tcp_data) = ipPacketData(data)'''
    return total_size

def socketStart(net_interface):
    Socket = socket(AF_PACKET, SOCK_RAW, htons(3))
    Socket.bind((net_interface, 0))
    return Socket

def packetAnalysis(data, serverSocket):
    if (data[:6] == b'\x00\x00\x00\x00\x01\x01'):
        return 0
    if (data[6:][:6] == b'RT\x001\x82'):
        return 0
    if (data[:6] == b'\xff\xff\xff\xff\xff\xff'):
        if (data[6:][:6] == b'\x00\x00\x00\x00\x01\x01'):
            serverSocket.send(data)
            return 2
    if (data[:6] == b'\x00\x00\x00\x00\x01\x02') and (data[6:][:6] == b'\x00\x00\x00\x00\x01\x01'):
        return 1
    
    return 0

def packetDelay(last, now):
    diff = last - now
    return diff

def numberPacketsProcessed(n_transmitted, n_dropped, max_processed):
    total =  n_transmitted + n_dropped
    #print (total)
    if total >= max_processed:
        return 1
    return 0

