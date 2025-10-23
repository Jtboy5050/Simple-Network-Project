# Program 2 of 3
# This program is player 2 of 2, with the third function being the server
# The goal of this program is to be a simple computer game of rock, paper, scissors
# This is my first program in python
# Author: Jonathan Andrews
# Class: Networking, Honor's Contract
# Purpose: teach the understanding of how networking works via real implementation

# Imports the needed libraries
from socket import *
import os
import time

# Sets the server host and port to connect to
serverHost = 'localhost'
serverPort = 12036

# Creates the socket and connects to the server
client2 = socket(AF_INET, SOCK_STREAM)
client2.connect((serverHost, serverPort))

print("Sucessfully connected to the server!")

# Asks if the player wants to play against a human or bot
client2Message = client2.recv(1024).decode()
print(client2Message, end='')

# Checks to see what the opponent type is, then sends it to the server
mode = input("Choose opponent (human/bot): ").strip().lower()
client2.send(mode.encode())

# Main loop to keep the client running and responding to server messages
while True:

    # Recieves the message from the server
    client2Message = client2.recv(1024).decode()
    
    # If there isn't a message from the server, the program assumes a disconnection and ends the game
    if not client2Message:
        
        print("Server Disconnected :(")
        break

    # Prints whatever message the server sent
    print(client2Message, end='')

    # The check for if the server sent to enter a move
    if "Enter your move" in client2Message:
        
        # Takes an input of the player's move
        move = input("Your move (rock, paper, scissors, or quit): ").strip().lower()
        
        # Sends the move to the server
        client2.send(move.encode())
        
        # If the move is quit, ends the game
        if move == "quit":

            print("Input is Quit. Exiting Game. Goodbye!")
            break

            # The check for if the server sent to ask if the player wants to play again
    elif "Would you like to play again?" in client2Message:
        
        # Gets the input from the player 
        play_again = input("Would you like to play again? (yes/no): ").strip().lower()
        
        # Sends the input to the server
        client2.send(play_again.encode())

        # Has a delay so that the user isn't instantly shot back to the beginning
        time.sleep(3000)

        # If the player wants to play again, the screen is cleared for cleanliness
        if play_again == "yes":
            os.system('cls' if os.name == 'nt' else 'clear')
        
        # If the player doesn't want to play again, the game ends
        if play_again != "yes":

            print("Exiting Game. Goodbye!")
            break

# Closes the socket as a means of cleanup
client2.close()
