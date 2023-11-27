import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)

print('Server listening on {}:{}'.format(*server_address))

# Wait for a connection
client_socket, client_address = server_socket.accept()
print('Connection from', client_address)

# Send data to the client
message = 'Hello, client!'
client_socket.sendall(message.encode())

# Close the connection
client_socket.close()
server_socket.close()
