import socket # Importing the socket module
import os

# Defining host address and port value
HOST = "127.0.0.1" 
PORT = 2728

# Function to handle the client connections
def handle_request(client_socket): # client_socket represents the socket connection with the client
    request = client_socket.recv(1024).decode("utf-8") # Reading data from the client using recv(1024), which reads upto 1024 bytes of data which is then decoded using the UTF-8 encoding
    file_path = request.split("\n")[0].split(" ")[1] #Getting the file path from the request

    if (file_path == "/"):
        php_output = os.popen("index.html").read()
        response = f"HTTP/1.1 200 OK\nContent-Type: text/html\n\n{php_output}"

    if (file_path.endswith(".html")):
        if (os.path.isfile(file_path)):
            # Connecting to the command line and executing the php script and reading the output
            php_output = os.popen(file_path).read()
            response = f"HTTP/1.1 200 OK\nContent-Type: text/html\n\n{php_output}"
    response = "HTTP/1.1 200 OK\nContent-Type: text/html\n\nFile not found"
    client_socket.send(response.encode("utf-8")) # Response is sent to the client socket using send after encoding the response
    client_socket.close() # The client socket connection is closed

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Creating a server socket indicating ipv4 and TCP
server_socket.bind((HOST, PORT)) # Binding the address and port values to the server
server_socket.listen(1) # Specifying the maximum number of queued connections in the server
print("Server is listening => ",HOST,PORT)

# Server will be running until manually stopped
while True:
    client_socket, client_address = server_socket.accept() # Server listens to incoming connections; when a connection is established a client_socket and client_address is created
    print("Connection accepted")
    handle_request(client_socket)

    # cd Downloads & python server.py