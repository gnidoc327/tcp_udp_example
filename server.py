import select
import socket
import queue

HOST = 'localhost'
PORT = 8080

server_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_tcp.setblocking(0)
server_tcp.bind((HOST, PORT))
server_tcp.listen(5)

server_udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_udp.bind((HOST,PORT))

inputs = [server_udp,server_tcp]
outputs = []
message_queues = {}

while inputs:
    readable, writable, exceptional = select.select(inputs, outputs, inputs)
    for s in readable:
        if s is server_tcp:
            connection, client_address = s.accept()
            connection.setblocking(0)
            inputs.append(connection)
            print("Received connection request from: ",client_address)
            message_queues[connection] = queue.Queue()
        elif s is server_udp:
            data, addr = s.recvfrom(1024)
            if data:
                print("data received over UDP: ", data)
                data = ("ACK - data received: "+str(data)).encode()
                s.sendto(data,addr)
        else:
            data = s.recv(1024)
            if data:
                print("data received: ",data)
                data = ("ACK - data received: "+str(data)).encode()
                message_queues[s].put(data)
                if s not in outputs:
                    outputs.append(s)
                    
    for s in writable:
        if not message_queues[s].empty():
            next_msg = message_queues[s].get()
            s.send(next_msg)
        else:
            outputs.remove(s)

    for s in exceptional:
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()
        del message_queues[s]
