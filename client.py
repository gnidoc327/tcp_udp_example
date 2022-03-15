import socket

HOST = 'localhost'
PORT = 8080

use_tcp = False

if not use_tcp:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.sendto(b'Hello, world',(HOST,PORT))
        data, addr = s.recvfrom(1024)
        print(f'received data / addr : {data} / {addr}')
else:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print("Connected to server. Press ENTER to start sending requests")
        input()
        s.sendall(b'Hello, world')
        data = s.recv(1024)
        print(f'received data : {data}')

print('Received', repr(data))
