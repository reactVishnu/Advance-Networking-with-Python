import socket

target_host = "8.8.8.8"  # DNS server (Google's public DNS)
target_port = 53

# Create a socket client
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# DNS query for google.com (encoded to bytes)
dns_query = b"\xAA\xAA\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x06google\x03com\x00\x00\x01\x00\x01"

# Send the DNS query to the DNS server
client.sendto(dns_query, (target_host, target_port))

# Receive a response from the DNS server (if any)
data, addr = client.recvfrom(4096)

# Closing the client
client.close()

print(data)
