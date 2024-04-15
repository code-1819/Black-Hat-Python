import socket
import threading

IP = "0.0.0.0"
PORT = 9998


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))  # IP address and port the server should listen on
    server.listen(5)  # Maximum backlog of connections = 5
    print(f'[*] Listening in {IP}:{PORT}')

    while True:
        client, address = server.accept()  # Client connects,we receive client_socket
        print(f'[*] Accepted connection from {address[0]}:{address[1]}')
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()  # Start thread to handle client connection


def handle_client(client_socket):  # Performs the recv() and sends an acknowledgement to client
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'[*] Received: {request.decode("utf-8")}')
        sock.send(b'ACK')


if __name__ == '__main__':
    main()
