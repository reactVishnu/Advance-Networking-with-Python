import socket
import subprocess

# socket object
server: socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Host and Port Information
host: str = '0.0.0.0'
port: int = 9999

# Bind and listening
server.bind((host, port))
server.listen(5)


def get_username() -> str:
    host_name = subprocess.run(['cmd.exe', '/c', 'echo %USERNAME%'],
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               text=True)
    if host_name.returncode == 0:
        return str(host_name.stdout)
    else:
        return str(host_name.stderr)


def command_injection_checker(command: str) -> str:
    print('Function runned')
    # For linux/unix subsystem
    # output = subprocess.run([command], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # For windows
    # output = subprocess.run(['cmd.exe', '/c', command], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # For shell
    output = subprocess.run(command, shell=True, capture_output=True, text=True)
    # Check if the command was successful
    if output.stdout=="":
        return str(output.returncode)

    if output.returncode == 0:
        # Print the output
        print('inside if')
        return str(output.stdout.replace('\r', ''))
    else:
        # Print error message
        return f'Error: {output.stderr}'


try:
    while True:
        print(f"Listening from {host}")
        client_socket, addr = server.accept()
        while True:
            print(f'Client connected from {addr[0]}')

            username = get_username()
            client_socket.send(f'{username}'.encode('utf-8'))
            message = client_socket.recv(1024).decode('utf-8')
            print(f'Message Received {message}')
            result = command_injection_checker(str(message))
            client_socket.send(f'{result}'.encode('utf-8'))
            print("Result Sent")
except Exception as e:
    print(f'Exception Occurred {e}')
finally:
    client_socket.close()
