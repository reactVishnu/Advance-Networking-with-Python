import socket

HOST = '0.0.0.0'
PORT = 9999

# creating the socket object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# binding it to the socket
server.bind((HOST, PORT))

server.listen(5)

try:
    while True:
        print(f'Listening from the host {HOST} .....')
        client_socket, addr = server.accept()
        print(f'Connection Listened from {addr}')
        message = client_socket.recv(1024).decode('utf-8')
        print(f'Decoded Message: {message}')
        client_socket.send(f"Did you just said {message}".encode('utf-8'))
        client_socket.close()
        print("The connection has been closed")
except Exception as e:
    print(f"An Exception Occurred! {e}")
finally:
    print("Closing the connection")
    client_socket.close()
