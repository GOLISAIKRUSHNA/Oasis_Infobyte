import socket
import threading

# Function to receive messages from the server
def receive_messages(client_socket):
    while True:
        try:
            # Receive data from the server
            data = client_socket.recv(1024).decode('utf-8')
            print(data)
        except Exception as e:
            print(f"Error receiving message: {e}")
            break

# Main client code
HOST = '127.0.0.1'
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# Receive and print the welcome message
welcome_message = client.recv(1024).decode('utf-8')
print(welcome_message)

# Enter a username
username = input("Enter your username: ")
client.send(username.encode('utf-8'))

# Start a thread to receive messages from the server
receive_thread = threading.Thread(target=receive_messages, args=(client,))
receive_thread.start()

# Main loop to send messages to the server
while True:
    message = input()
    client.send(message.encode('utf-8'))



# I am already started two client 
# mean's two time i am running the same file 
    
    #see server is activated ...  both client are activated now ,we can chat now
    #now see again

    # this is all about project where one server and two client