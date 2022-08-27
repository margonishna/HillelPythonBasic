from socket import socket, SHUT_WR
import pprint


def handler(socket):
    counter = 0

    while True:
        client_socket, address = socket.accept()

        incoming_data = client_socket.recv(5000)

        # print(incoming_data)
        incoming_data = incoming_data.decode()

        pieces = incoming_data.split('\r\n')
        if len(pieces) > 0:
            counter += 1
            pprint.pprint(f'Request {counter}')
            pprint.pprint(pieces)

            # for piece in pieces:
            #     print(piece)

        data = f'HTTP/1.1 200 OK \r\n' \
               f'Content-Type: text/html; carset=utf-8\r\n\r\n' \
               f'<html><body>HELLO! It\'s request number: {counter} </html></body>\r\n\r\n'
        client_socket.sendall(data.encode())
        client_socket.shutdown(SHUT_WR)


def my_server():
    server_socket = socket()

    try:
        server_socket.bind(('localhost', 9002))
        print('Started at http://localhost:9002')

        server_socket.listen(5)
        handler(server_socket)

    except KeyboardInterrupt:
        print(f'Shutting down')
    except Exception as e:
        print(Exception)
        print(e)

    finally:
        server_socket.close()


my_server()
