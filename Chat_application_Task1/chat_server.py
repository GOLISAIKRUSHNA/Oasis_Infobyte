import socket   #module's
import threading

# Function to handle client connections
def handle_client(client_socket, username):
    while True:
        try:
            # Receive data from the client
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break

            # Broadcast the message to all connected clients
            message = f"{username}: {data}"
            print(message)
            broadcast(message, client_socket)

        except Exception as e:
            print(f"Error: {e}")
            break

    # Remove the client from the list
    remove_client(client_socket)
    client_socket.close()

# Function to broadcast messages to all clients
def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message.encode('utf-8'))
            except Exception as e:
                print(f"Error broadcasting message: {e}")
                remove_client(client)

# Function to remove a client from the list
def remove_client(client_socket):
    if client_socket in clients:
        clients.remove(client_socket)

# Main server code
HOST = '127.0.0.1'
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"Server listening on {HOST}:{PORT}")

clients = []

while True:
    # Accept a new client connection
    client_socket, client_address = server.accept()
    print(f"Connection established from {client_address}")

    # Prompt the client for a username
    client_socket.send("Enter your username: ".encode('utf-8'))
    username = client_socket.recv(1024).decode('utf-8')

    # Add the client to the list
    clients.append(client_socket)

    # Broadcast a welcome message
    welcome_message = f"{username} has joined the chat!"
    print(welcome_message)
    broadcast(welcome_message, client_socket)

    # Start a new thread to handle the client
    client_thread = threading.Thread(target=handle_client, args=(client_socket, username))
    client_thread.start()




        #IN this, I need three terminal's
        #1 server
        #2 client1   now this terminal
        #3 client2   
    



    # Server listening on 127.0.0.1:12345 is started  let see... 
    # how two client interact like whatsapp