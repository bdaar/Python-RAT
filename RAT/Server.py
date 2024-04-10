import socket
import os

host = "[IP]"
port = [Connection Port]

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
