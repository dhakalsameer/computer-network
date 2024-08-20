from socket import *

# Server information
serverName = "127.0.0.1"
serverPort = 12000

# Create a UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Ask the user for input
message = input("Input lowercase sentence: ")

# Send the message to the server
clientSocket.sendto(message.encode(), (serverName, serverPort))

# Receive the response from the server
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

# Display the server's response
print("Server response:", modifiedMessage.decode())

# Close the client socket
clientSocket.close()
