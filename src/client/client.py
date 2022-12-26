import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.connect(('localhost', 8000))

def send_command(str_command: str):
    server_socket.send(str_command.encode())
    print('Waiting for response...')


def main():
    while True:
        user_input = input('>> ')
        sp_usin = user_input.split(' ')

        if sp_usin[0] == 'search' and sp_usin[2] == 'from':
            send_command(user_input)
            print()
            print(server_socket.recv(1024).decode())

        if sp_usin[0] == 'select' and sp_usin[2] == 'from':
            send_command(user_input)
            print()
            print(server_socket.recv(1024).decode())

        if user_input == 'file':
            send_command(user_input)
            print()
            print(server_socket.recv(1024).decode())

        if (user_input == 'quit'):
            send_command(user_input)
            server_socket.close()
            break

if __name__ == '__main__':
    main()