import socket
import sys

ip = "192.168.1.14"
port = 1443
l = []
lst = []

# Create a UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
# Bind the socket to the port
server_address = (ip, port)
s.bind(server_address)
binary_file=open("my_file", "wb")
print("Data to be recieved")
try:
    while True:
        data, address = s.recvfrom(1024)
        data_id, address_id = s.recvfrom(4096)
        t = data_id.decode('utf-8')
        l.append(int(t))
        binary_file.write(data)
except KeyboardInterrupt:
    # print(l)
    print("\n")
    NoDataLoss_num = 0
    for i in range(len(l)):
        if l[i] != i:
            lst.append(i)
        else:
            NoDataLoss_num += 1
            pass
    print(NoDataLoss_num)
    s.close()