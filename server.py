import socket # Importing the socket module

# Defining host address and port value
HOST = "127.0.0.1" 
PORT = 2728
ROOT = "C:\\Users\\srvnn\\Downloads\\htdocs\\" # Absolute path of the htdocs directory

# Function to handle the client connections
def handle_request(client_socket): # client_socket represents the socket connection with the client
    request = client_socket.recv(1024).decode("utf-8") # Reading data from the client using recv(1024), which reads upto 1024 bytes of data which is then decoded using the UTF-8 encoding
    file_path = request.split("\n")[0].split(" ")[1] #Getting the file path from the request
    response = ""

    if (file_path == "/"):
        try:
            with open(ROOT + "index.php", "r") as file:
                php_content = file.read()
            response = f"HTTP/1.1 200 OK\nContent-Type: text/html\n\n{php_content}"
        except FileNotFoundError:
            response = "HTTP/1.1 404 Not Found\nContent-Type: text/plain\n\nFile not found"
    elif (file_path.endswith(".php")):
        path = ROOT + "webpages\\" +file_path[1:]
        try:
            with open(path, "r") as file:
                php_content = file.read()
            response = f"HTTP/1.1 200 OK\nContent-Type: text/html\n\n{php_content}"
        except FileNotFoundError:
            response = "HTTP/1.1 404 Not Found\nContent-Type: text/plain\n\nFile not found"
    client_socket.send(response.encode("utf-8")) # Response is sent to the client socket using send after encoding the response
    client_socket.close() # The client socket connection is closed

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Creating a server socket indicating ipv4 and TCP
server_socket.bind((HOST, PORT)) # Binding the address and port values to the server
server_socket.listen(1) # Specifying the maximum number of queued connections in the server
print("Server is listening => ",HOST,PORT)

# Server will be running until manually stopped
try:
    while True:
        client_socket, client_address = server_socket.accept()
        print("Connection accepted")
        handle_request(client_socket)
except KeyboardInterrupt:
    print("Server is shutting down...")
    server_socket.close()