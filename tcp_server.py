import select
import socket
import queue

HOST = 'localhost'
PORT = 8080

server_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_tcp.bind((HOST, PORT))
server_tcp.listen(1)

print("[TCP] Start server. Waiting client requests")
connection, client_address = server_tcp.accept()
while True:
    received_msg = connection.recv(1024)
    print(f"[TCP] Received client msg = {received_msg}")
    msg = input("input->")
    connection.send(msg.encode())
