import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 2000))
server.listen(4)

print('Сервер працює....')
name = input('Введіть своє імя: ')
conn, add = server.accept()

client = (conn.recv(1024).decode('utf-8'))
print(client + ' Приєднався!')
conn.send(name.encode('utf-8'))

while True:
    message = input('Я: ')
    conn.send(message.encode('utf-8'))
    message = conn.recv(1024)
    message = message.decode('utf-8')
    print(client, ':', message)
