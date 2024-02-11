import socket

target_host: str = '192.168.1.17'
target_port: int = 9999

client: socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host, target_port))

message: str = input('Enter your message\n').__str__()

client.send(message.encode('utf-8'))
print(client.recv(1024).decode('utf-8'))
