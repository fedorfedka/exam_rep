import socket
import data_handler
import os

# так как я запускаю сервер из src для удобства
# я меняю директорию на /server
os.chdir('server')

# создаем сокет сервера и привязываем его к ip: localhost port: 8000
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8000))

# слушаем заданый порт
server_socket.listen(1)


# логика серверной части команды search
def com_search(file_name: str, value):
    return data_handler.search_rows_from_scv(file_name, value)


# логика серверной части команды select
def com_select(file_name: str, rows_count: int):
    return data_handler.get_rows_from_scv(file_name, rows_count)


# логика серверной части команд file
def com_file():

    # получение всего списка файлов в виде list
    list_dir = os.listdir()

    # создание пустой строки для добавления в нее
    # отформатированных элементов list_dir
    # для более приятного на вид вывода списка файлов 
    str_list_dir = ""

    # цикл добавление строк
    for file in list_dir:
        str_list_dir += file + '\n'
    
    return str_list_dir


# превращение полученной команды в list для удобства с работой
def command_to_list(command) -> list:
    command = command.decode()
    return command.split(' ')
     

# цикл подключений и отключений пользователей
while True:
    print('Waiting for connections...')

    # получение сокета клиента и его адреса ip port
    user_socket, address = server_socket.accept()

    print(f'Got connection from{address}')

    # цикл работы с подключенными
    while True:

        # получение и форматирование команды
        command = user_socket.recv(1024)
        command = command_to_list(command)

        print(f'Got command from {address}')

        # обработка команды search
        if command[0] == 'search' and command[2] == 'from':
            try:
                user_socket.send(com_search(command[3], command[1]).encode())
                
            except Exception as e:
                user_socket.send(str(e).encode())

        # обработка команды select
        if command[0] == 'select' and command[2] == 'from':
            try:
                user_socket.send(com_select(command[3], command[1]).encode())
                
            except Exception as e:
                user_socket.send(str(e).encode())

        # обработка команды file
        if command[0] == 'file':
            user_socket.send(com_file().encode())

        # обработка команды quit
        if command[0] == 'quit':
            print('Quiting...')
            break
    
    user_socket.close()