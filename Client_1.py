import datetime
import socket
import sys

ip = "192.168.1.14"
port = 1443
buff = 1024
i = 0
dic = {}

# Create socket for server
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
# Let's send data through UDP protocol
begin_time = datetime.datetime.now()
tup = (ip, port)
try:
    while True:
        print("Enter File name")
        k = input()
        file = open(k,'r+b')
        send_data = file.read(buff)
        while send_data:
            s.sendto(send_data, tup)
            string = str(i)
            s.sendto(string.encode('utf-8'), tup)
            dic[i] = send_data
            send_data = file.read(buff)
            i += 1
        print(f"Time taken to send file is : {datetime.datetime.now() - begin_time} s")
        print("Client sent the file")
        file.close()
        print(f"Size of file sent was {i * buff}")
except KeyboardInterrupt:
    s.close()
