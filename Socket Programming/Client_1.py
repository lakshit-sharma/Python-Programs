import socket
import time

t = time.localtime(time.time())
client_1 = socket.socket()
host = input('Enter host name - ')
port = 9999
client_1.connect((host, port))
print('Connected to the Server')

while True:
    chat = input("Client>>>")
    client_1.send(bytes(chat, 'utf-8'))
    receive = client_1.recv(1024).decode()
    print('Server>>>>', receive, t)
