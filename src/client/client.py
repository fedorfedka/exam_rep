import socket

# создаем сокет и подключаем его к сереверу -> ip: localhost port: 8000
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8000))

# функция для отправки сообщений серверу
def send_command(str_command: str):
    client_socket.send(str_command.encode())
    print('Waiting for response...')


# функция отправки ввода и ожидания, а затем показа, ответа от сервера
def send_recive(user_input: str):
    send_command(user_input)
    print()
    print(client_socket.recv(1024).decode())


# главная функция
def main():

    # цикл отправки и получения сообщений
    while True:

        # ввод пользователя
        user_input = input('>> ')

        # конвертируем ввод в удобный для работы список
        sp_usin = user_input.split(' ')

        # обработка команды search
        if sp_usin[0] == 'search' and sp_usin[2] == 'from':
            send_recive(user_input)

        # обработка команды select
        if sp_usin[0] == 'select' and sp_usin[2] == 'from':
            send_recive(user_input)

        # обработка команды file
        if user_input == 'file':
            send_recive(user_input)

        # oбработка команды quit для нормального завершения работы с сервером
        if (user_input == 'quit'):
            send_command(user_input)

            # закрытие соединения с сервером
            client_socket.close()
            break

# выполняется только если код запускают из этого файла
# (не запустится при импорте)
if __name__ == '__main__':
    main()