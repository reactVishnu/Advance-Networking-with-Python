import socket

target_host = '192.168.1.17'
target_port = 9999

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to the server
    client.connect((target_host, target_port))

    host_name = client.recv(1024).decode('utf-8').replace('\n', '')
    # Prompt the user for a message
    message = str(input(f'{host_name}@{target_host}:~$ '))

    # Send the message to the server
    client.send(message.encode('utf-8'))

    # Receive the response from the server
    response = client.recv(1024)

    # Print the response
    print(response.decode('utf-8'))

except Exception as e:
    # Handle any exceptions that occur during the connection process
    print('An error occurred:', e)

finally:
    # Close the connection
    client.close()
