import socket

listening_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listening_socket.bind(('127.0.0.1', 2000))
listening_socket.listen(4)

while True:
    socket_for_communication, addr = listening_socket.accept()
    print('Приєднався до: ', addr)
    data = socket_for_communication.recv(1024).decode()
    if data == 'Авто':
        answer = 'Ви обрали рубрику Авто'
        socket_for_communication.sendall(answer.encode())
    elif data == 'Дом':
        answer = 'Ви обрали рубрику Дом'
        socket_for_communication.sendall(answer.encode())
    elif data == 'Спорт':
        answer = 'Ви обрали рубрику Спорт'
        socket_for_communication.sendall(answer.encode())
    elif data == 'Техніка':
        answer = 'Ви обрали рубрику Техніка'
        socket_for_communication.sendall(answer.encode())
    elif data == 'Дача':
        answer = 'Ви обрали рубрику Дача'
        socket_for_communication.sendall(answer.encode())
    else:
        error = 'Така рубрика відсутня, повторіть будь ласка'
        socket_for_communication.sendall(error.encode())
    socket_for_communication.close()

listening_socket.close()

