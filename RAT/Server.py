import socket
import os

host = '127.0.0.1'
port = 98

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as skt:
    skt.bind((host, port))
    skt.listen()
    connection, addr = skt.accept()
    with connection:
        print('Connected by', addr)
        data = connection.recv(4068)
        print(data)

        command = input("Enter ")
        connection.sendall(bytes(command, 'utf-8'))
