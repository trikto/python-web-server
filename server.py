import socket
import subprocess

# Defining constants
HOST = "127.0.0.1" # Required host
PORT = 2728 # Required port
ROOT = "D:\\Academics\\Networking\\21001512\\htdocs\\" # Absolute path of the htdocs directory
PHP_FILE_PATH = "D:/Academics/Networking/21001512/htdocs/" # Location of the php file
PHP_FILE_NAME = "run.php" # Name of the php file
PORT_2 = "8000" # Any port that is not in use for the localhost

# Function to handle the client connections
def handle_request(client_socket): # client_socket represents the socket connection with the client
    request = client_socket.recv(4096).decode("utf-8") # Reading data from the client using recv(4096), which reads upto 4096 bytes of data which is then decoded using the UTF-8 encoding
    request_type = request.split("\n")[0].split(" ")[0]
    file_path = request.split("\n")[0].split(" ")[1] #Getting the file path from the request
    response = ""

    if (request_type == "POST"):
        # Getting x and y from the request
        x_and_y = request.split("\n")[-1]
        x = x_and_y.split("&")[0].split("=")[1]
        y = x_and_y.split("&")[1].split("=")[1]
        
        # Server strings
        start_server = "php -S localhost:" + PORT_2 + " -t " + PHP_FILE_PATH
        post_data = "x=" + x + "&y=" + y
        connection_string = "http://localhost:" + PORT_2 + "/" + PHP_FILE_NAME

        # Curl command
        run = "curl -d \"" + post_data + "\" -X POST " + connection_string

        # Starting the php server to handle the POST request
        php_server_process = subprocess.Popen(start_server, shell=True, text=True)

        # Run the curl command in the Command Prompt
        response = subprocess.run(run, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Get the command output from stdout
        cmd_output = response.stdout

        response = f"HTTP/1.1 200 OK\nContent-Type: text/html\n\n{cmd_output}"

    elif (file_path == "/"): # Default path / home page
        try:
            with open(ROOT + "index.php", "r") as file:
                php_content = file.read()
            response = f"HTTP/1.1 200 OK\nContent-Type: text/html\n\n{php_content}"
        except FileNotFoundError:
            response = "HTTP/1.1 404 Not Found\nContent-Type: text/plain\n\nFile not found"
    elif (file_path.endswith(".php")): # Other pages
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
        # print("Connection accepted")
        handle_request(client_socket)
except KeyboardInterrupt:
    print("Server is shutting down...")
    server_socket.close()