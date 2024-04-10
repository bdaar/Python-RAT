import socket

host = "[Server IP]"
port = [Connection Port]

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
