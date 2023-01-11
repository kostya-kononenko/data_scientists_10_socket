import socket

listening_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listening_socket.bind(('127.0.0.1', 3000))
listening_socket.listen(4)

while True:
    socket_for_communication, addr = listening_socket.accept()
    print('Приєднався до: ', addr)
    data = socket_for_communication.recv(1024).decode()
    new_data = len(list(data.split()))
    print(new_data)
    socket_for_communication.sendall(str(new_data).encode())
    socket_for_communication.close()

listening_socket.close()

