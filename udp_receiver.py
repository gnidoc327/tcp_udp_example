import select
import socket
import queue

HOST = 'localhost'
PORT = 8080

server_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_udp.bind((HOST, PORT))

print("[UDP] Start server. Waiting sender msg")
while True:
    received_msg, sender = server_udp.recvfrom(1024)
    print(f"[UDP] Received msg = {received_msg}")
