import socket

server=socket.socket()
host=socket.gethostname()
print('Server is Ready on Host',host)
port=9999
server.bind((host,port))
server.listen(5)
print('Server Created')
connection,addr = server.accept()
print(addr,'Has Connected...........')
while True:
    receive = connection.recv(1024).decode()
    print('Client_1', receive)
    chat=input("Server>>>")
    connection.send(bytes(chat,'utf-8'))


