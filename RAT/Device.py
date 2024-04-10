import socket

host = "127.0.0.1"
port = 98

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as skt:
    skt.bind((host, port))
    skt.listen()
    connection, addr = skt.accept()
    with connection:
        print("{addr}")
        data = connection.recv(4068)
        print(data)

        command = input("Enter command: ")
        connection.sendall(bytes(command, encoding="utf-8"))
