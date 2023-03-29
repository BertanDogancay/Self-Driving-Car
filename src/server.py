import socket
import time

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.2.19', 1234))
s.listen(5)

while True:
    clientSocket, address = s.accept()
    print(f"Connection from {address} has been established!")

    msg = "Welcome to the server!"
    msg = f'{len(msg):<{HEADERSIZE}}' + msg

    clientSocket.send(bytes(msg, "utf-8"))

    while True:
        time.sleep(3)
        msg = f"Time is {time.time()}"
        msg = f'{len(msg):<{HEADERSIZE}}' + msg
        clientSocket.send(bytes(msg, "utf-8"))