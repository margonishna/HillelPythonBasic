from socket import socket
import time


def request():

    while True:
        client_socket = socket()
        client_socket.connect(('localhost', 9002))

        request = 'GET http://localhost/blabla HTTP/1.0\r\n\r\n'.encode()
        client_socket.send(request)

        while True:
            data = client_socket.recv(5000)
            if len(data) < 1:
                break
            print(data.decode())

        client_socket.close()

        time.sleep(2)


request()
