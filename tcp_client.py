import socket

HOST = 'localhost'
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("[TCP] Connected to server. Press ENTER to start sending requests")
    while True:
        msg = input("input->")
        # 연결
        s.connect((HOST, PORT))
        # 메세지 전송
        s.sendall(msg.encode())
        # 응답 받음
        received_msg = s.recv(1024)
        print(f"[TCP] Received server msg = {received_msg}")
