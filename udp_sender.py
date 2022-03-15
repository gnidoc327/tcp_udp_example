import socket

PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    print("[UDP] Connected to server. Press ENTER to start sending requests")
    while True:
        msg = input()
        # 메세지 전송
        s.sendto(msg.encode(), ('', PORT))
