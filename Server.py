# Program 3 of 3
# This program is the server to 2 players 
# This is part of my first python project, which has a goal of teaching how networking works via real use applications
# Author: Jonathan Andrews
# Class: Networking, Honor's Contract
# Purpose: teach the understanding of how networking works via real implementation

# Imports all functions from the socket function that allows connection to a server
from socket import *

userInput1 = "Yes"
userInput2 = "Yes"

# Creates the socket for the players to connect to
serverPort = 12036
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind('', serverPort)

# Listens for two players inputs
serverSocket.listen(2)

# Conformation that the server is active
print ("The server is now active and ready to recieve player connections")

# Both attempt to connect to each player, and upon doing so prompt the player with a message that says they connected
print ("Attempting to recieve player 1..")
player1Socket, address1 = serverSocket.accept()
print ("Player 1 connected! Address: ", address1)

print ("Attempting to recieve player 2...")
player2Socket, address2 = serverSocket.accept() 
print ("Player 2 Connected! Address: ", address2)

player1Socket.send(b"Connected. You are player 1. Welcome!\n")
player2Socket.send(b"Connected. You are player 2. Welcome!\n")

# While this is all true, runs different outcomes such as if someone enters quit, rock, etc. 

# COME BACK HERE AND FINISH UP THE LOOPING FUNCTION YOU WERE GONNA TRY TO IMPLEMENT
while userInput1 == "Yes" and userInput2 == "Yes":

    while 1:
        
        # Sends a command to the player to input a response which is a cue on the client sides to allow input from the user
        player1Socket.send(b"Enter your move (rock, paper, scissors, or quit): ")
        player2Socket.send(b"Enter your move (rock, paper, scissors, or quit): ")

        # Gets the input from the users
        move1 = player1Socket.recv(1024).decode().strip().lower()
        move2 = player2Socket.recv(1024).decode().strip().lower()

        # For if a user wants to quit the game
        if move1 or move2 == "quit":
            print("One player has quit. Ending Game")
            player1Socket.send("A player has quit the game. Goodbye!\n")
            player2Socket.send("A player has quit the game. Goodbye!\n")
            break

        # If there's a tie
        if move1 == move2:
            result = "Both players chose {move}. It's a tie.\n"
        
        # Every scenario where player 1 wins is checked for 
        elif (move1 == "rock" and move2 == "paper") or (move1 == "scissors" and move2 == "rock") or (move1 == "paper" and move2 == "scissors"):
            result = "Player 1 wins! {move1} beats {move2}!\n"
        
        # ...otherwise player 2 is declared the winner
        else: 
            result = "Player 2 wins! {move1} beats {move2}!\n"

        # Whichever player won, the results are sent to both players
        player1Socket.send(result.encode())
        player2Socket.send(result.encode())


        # Closes the sockets as a means of cleanup and lets the server runner know the game is over
        player1Socket.close()
        player2Socket.close()
        serverSocket.close()
        print("Game over.")