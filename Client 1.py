# Program 1 of 3
# This program is player 1 of 2, with the third function being the server
# The goal of this program is to be a simple computer game of rock, paper, scissors
# This is my first program in python
# Author: Jonathan Andrews
# Class: Networking, Honor's Contract
# Purpose: teach the understanding of how networking works via real implementation


# Import the network function
from socket import *

# Variable Declaration for the socket
serverHost = 'localhost'
serverPort = 12036

# Connects to the socket

client1 = socket(AF_INET, SOCK_STREAM)

client1.connect(serverHost, serverPort)

print ("Sucessfully connected to the server!")

# Checks if the connection exists. If it doesn't, disconnects the user. Otherwise, prompts the user for their message
while True:

    client1Message = client1.recv(1024).decode()

    print(client1Message, end='')
    
# The error handler
   
    if not client1Message:

        print("Server Disconnected :(")
        break
    
    if ("Enter Move" in client1Message):
        
        move = input("Your move (rock, paper, scisossors, or quit)")
        
        client1.send(move.encode())

    if move == "quit":

        print("Input is Quit. Exiting Game. Goodbye!")
        break

client1.close()