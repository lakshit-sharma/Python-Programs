import socket

client_2=socket.socket()
host=input('Enter Server - ')
port=9999
client_2.connect((host,port))
print('connected to the Server')

while True:
    '''receive = client_2.recv(1024).decode()
    print('Server>>>>', receive)

    chat = input("Client>>>")
    client_2.send(bytes(chat, 'utf-8'))'''
