import socket
import threading

HOST = '127.0.0.1'
PORT = 5000

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket: for network communication between two computers (or terminals)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[SERVER] Listening on {HOST}:{PORT}...")
    conn, addr = server.accept()
    print(f"[SERVER] Connected by {addr}")

    def receive():
        while True:
            try:
                msg = conn.recv(1024).decode()
                if msg:
                    print(f"[Client] {msg}")
            except:
                print("[SERVER] Connection closed.")
                conn.close()
                break

    def send():
        while True:
            msg = input("")
            conn.send(msg.encode())

    threading.Thread(target=receive).start() #threading: so you can send and receive messages at the same time
    threading.Thread(target=send).start()

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    print(f"[CLIENT] Connected to server at {HOST}:{PORT}")

    def receive():
        while True:
            try:
                msg = client.recv(1024).decode()
                if msg:
                    print(f"[Server] {msg}")
            except:
                print("[CLIENT] Connection closed.")
                client.close()
                break

    def send():
        while True:
            msg = input("")
            client.send(msg.encode())

    threading.Thread(target=receive).start()
    threading.Thread(target=send).start()

# User prompt
mode = input("Enter mode (server/client): ").strip().lower()
if mode == 'server':
    start_server()
elif mode == 'client':
    start_client()
else:
    print("Invalid mode. Please enter 'server' or 'client'.")
