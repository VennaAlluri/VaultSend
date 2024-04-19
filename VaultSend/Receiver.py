import socket
import Decryption
# Define the server address and port
host = 'localhost'  # Listen on all available network interfaces
port = 12345

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
server_socket.bind((host, port))

# Listen for incoming connections (maximum of 5 queued connections)
server_socket.listen(5)
print(f"Server listening on {host}:{port}")

# Accept incoming connections
client_socket, client_address = server_socket.accept()
print(f"Connection from {client_address}")

# Receive the file content
with open('received_file.txt', 'wb') as file:
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        file.write(data)
with open('received_file.txt', 'r') as text_file:
    image_base64 = text_file.read()
decoded_image_binary = Decryption.decode_base64(image_base64)
with open('receivedimage.png', 'wb') as output_image:
    output_image.write(decoded_image_binary)
print("File received successfully.")

# Close the client socket
client_socket.close()

# Close the server socket
server_socket.close()
