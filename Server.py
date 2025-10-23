# Program 3 of 3
# This program is the server to 2 players 
# This is part of my first python project, which has a goal of teaching how networking works via real use applications
# Author: Jonathan Andrews
# Class: Networking, Honor's Contract
# Purpose: teach the understanding of how networking works via real implementation

# Imports all functions from the socket function that allows connection to a server
from socket import *
import random

# Sets  up to recieve user inputs later for if they users want to play again
userInput1 = "yes"
userInput2 = "yes"

# Creates the socket for the players to connect to
serverPort = 12036
serverSocket = socket(AF_INET, SOCK_STREAM)

# Binds the server to the port
serverSocket.bind(('', serverPort))

# Listens for two players inputs
serverSocket.listen(2)

# Conformation that the server is active
print ("The server is now active and ready to recieve player connections")

# Both attempt to connect to each player, and upon doing so prompt the player with a message that says they connected
print ("Attempting to recieve player 1..")
player1Socket, address1 = serverSocket.accept()
print ("Player 1 connected! Address: ", address1)

# Sends the initial message to player 1 asking what type of opponent they want to play against
player1Socket.send(b"Would you like to play against a human or a bot? (human/bot): \n")
mode = player1Socket.recv(1024).decode().strip().lower()

# If the mode is human, attempts to connect to player 2
if mode == "human":
    print ("Attempting to recieve player 2...")
    player2Socket, address2 = serverSocket.accept() 
    print ("Player 2 Connected! Address: ", address2)

    player1Socket.send(b"Connected. You are player 1. Welcome!\n")
    player2Socket.send(b"Connected. You are player 2. Welcome!\n")

    # Otherwise, if the mode is bot, doesn't try to connect to player 2 and gets right to the game
else: 
    player1Socket.send(b"Connected to bot opponent. You are player 1. Welcome!\n")
    print("Bot opponent selected. Starting game against bot.")


# While this is all true, runs different outcomes such as if someone enters quit, rock, etc. 

# Starts the scorekeep before entering both while loops
trueScore1 = 0
trueScore2 = 0

# Two while loops for allowing the game to continue
while userInput1 == "yes" and userInput2 == "yes":

    while True:
        
        # Sends a command to the player to input a response which is a cue on the client sides to allow input from the user
        player1Socket.send(b"Enter your move (rock, paper, scissors, or quit): ")
        
        # If the mode is human, also sends the command to player 2
        if mode == "human":
        
            player2Socket.send(b"Enter your move (rock, paper, scissors, or quit): ")

        # Gets the input from the users
        move1 = player1Socket.recv(1024).decode().strip().lower()
        
        # If the mode is bot, randomly selects a move for player 2. Otherwise gets the input from player 2
        if mode == "bot":
            move2 = random.choice(["rock", "paper", "scissors"])
        else:
            move2 = player2Socket.recv(1024).decode().strip().lower()

        # For if a user wants to quit the game
        if move1 == "quit" or move2 == "quit":
            print("One player has quit. Ending Game")

            # Notifies player 1 that someone has quit
            player1Socket.send(b"A player has quit the game. Goodbye!\n")

            # Notifies player 2 that someone has quit if there is a player 2
            if mode == "human":
                player2Socket.send(b"A player has quit the game. Goodbye!\n")
            
            break
        
        # If there's a tie, both players are notified of the tie
        if move1 == move2:
            
            result = f"Both players chose {move1}. It's a tie.\n"
        
        # Every scenario where player 1 wins is checked for, and if met, the player is given a point
        elif (move1 == "rock" and move2 == "scissors") or (move1 == "scissors" and move2 == "paper") or (move1 == "paper" and move2 == "rock"):
            result = f"Player 1 wins! {move1} beats {move2}!\n"

            trueScore1 += 1
              
        # ...otherwise player 2 is declared the winner
        else: 
            result = f"Player 2 wins! {move2} beats {move1}!\n"

            trueScore2 += 1

        # Whichever player won, the results are sent to player 1
        player1Socket.send(result.encode())
        player1Socket.send(f"Player 1 Score: {trueScore1}\nPlayer 2 Score: {trueScore2}\n".encode())

        # ...and to player 2 if there is a player 2
        if mode == "human":
            player2Socket.send(result.encode())
            player2Socket.send(f"Player 1 Score: {trueScore1}\nPlayer 2 Score: {trueScore2}\n".encode())

        # Asks if player 1 want to play again
        player1Socket.send(b"Would you like to play again? (yes/no): ")
        
        # If there is a player 2, also asks them if they want to play again
        if mode == "human":
            player2Socket.send(b"Would you like to play again? (yes/no): ")

        # Gets the input from player 1 on if they want to play again
        userInput1 = player1Socket.recv(1024).decode().strip().lower()

        # If there is a player 2, gets their input on if they want to play again
        if mode == "human":        
            userInput2 = player2Socket.recv(1024).decode().strip().lower()
        else:
            # Bot always says yes
            userInput2 = "yes"  
        
# Closes the sockets as a means of cleanup and lets the server runner know the game is over
player1Socket.close()
if mode == "human":

    player2Socket.close()

serverSocket.close()

# The server is now closed and as such lets the server owner know
print("Game over.")
