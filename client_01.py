import socket

socket_server = socket.socket()

name = input("Введіть ваше імя: ")
socket_server.connect(('127.0.0.1', 2000))
socket_server.send(name.encode('utf-8'))
socket_name = socket_server.recv(1024)
server_name = socket_name.decode('utf-8')
print(server_name, ' Приеднався')

while True:
    message = (socket_server.recv(1024).decode('utf-8'))
    print(server_name, ':', message)
    message = input('Я: ')
    socket_server.send(message.encode('utf-8'))
