# Program 2 of 3
# This program is player 2 of 2, with the third function being the server
# The goal of this program is to be a simple computer game of rock, paper, scissors
# This is my first program in python
# Author: Jonathan Andrews
# Class: Networking, Honor's Contract
# Purpose: teach the understanding of how networking works via real implementation

# Import the network function
from socket import *

# Creates the socket info to connect to the other user
serverHost = 'localhost'
serverPort = 12036

# Starts the socket by connecting it to the server
client2 = socket(AF_INET, SOCK_STREAM)

client2.connect(serverHost, serverPort)

print ("Connected to Server Sucessfully!")

# Checks to see if the connection exists. If not, disconnects user, otherwise proceeds with the game
while True:
    
    client2Message = client2.recv(1024).decode()

    print (client2Message, end='')

# Handles error of no connection

    if not client2Message:
        print("The server has disconnected. Try again.")
        break

    if ("Enter Move" in client2Message):

        move = input("Your move. (Input Rock, Paper, Scissors, OR Quit.)")

        client2.send(move.encode())

        if move == "quit":

            print ("Input quit detected. Exiting game. Thank you for playing.")


client2.close()