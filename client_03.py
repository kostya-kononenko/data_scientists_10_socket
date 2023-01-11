import socket

while True:
    send_data = input('Введіть будь яке речення: ')
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 3000))

    client_socket.sendall(send_data.encode())
    data = client_socket.recv(1024).decode()

    print('У вашому реченні така кількість слів: ', data)

client_socket.close()
