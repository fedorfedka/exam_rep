import socket
import data_handler
import os

os.chdir('server')

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8000))
server_socket.listen(1)


def com_search(file_name: str, value):
    return data_handler.search_rows_from_scv(file_name, value)


def com_select(file_name: str, rows_count: int):
    return data_handler.get_rows_from_scv(file_name, rows_count)


def com_file():
    list_dir = os.listdir()
    str_list_dir = ""
    for file in list_dir:
        str_list_dir += file + '\n'
    return str_list_dir


def command_to_list(command) -> list:
    command = command.decode()
    return command.split(' ')
     


while True:
    print('Waiting for connections...')
    user_socket, address = server_socket.accept()
    print(f'Got connection from{address}')

    while True:
        command = user_socket.recv(1024)
        command = command_to_list(command)
        print(f'Got command from {address}')

        if command[0] == 'search' and command[2] == 'from':
            try:
                user_socket.send(com_search(command[3], command[1]).encode())
                
            except Exception as e:
                user_socket.send(str(e).encode())

        if command[0] == 'select' and command[2] == 'from':
            try:
                user_socket.send(com_select(command[3], command[1]).encode())
                
            except Exception as e:
                user_socket.send(str(e).encode())

        if command[0] == 'file':
            user_socket.send(com_file().encode())

        if command[0] == 'quit':
            print('Quiting...')
            break
    
    user_socket.close()