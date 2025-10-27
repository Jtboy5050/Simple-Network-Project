# Program 1 of 3
# This program is player 1 of 2, with the third function being the server
# The goal of this program is to be a simple computer game of rock, paper, scissors
# This is my first program in python
# Author: Jonathan Andrews
# Class: Networking, Honor's Contract
# Purpose: teach the understanding of how networking works via real implementation
# A change after github desktop
# Imports the needed libraries
from socket import *
import os
import time

# Sets the server host and port to connect to
serverHost = 'localhost'
serverPort = 12036

# Creates the socket and connects to the server
client1 = socket(AF_INET, SOCK_STREAM)
client1.connect((serverHost, serverPort))

print("Sucessfully connected to the server!")

# Asks if the player wants to play against a human or bot
client1Message = client1.recv(1024).decode()
print(client1Message, end='')

# Checks to see what the opponent type is, then sends it to the server
mode = input("Choose opponent (human/bot): ").strip().lower()
client1.send(mode.encode())

# Main loop to keep the client running and responding to server messages
while True:
    client1Message = client1.recv(1024).decode()
    
    # If there isn't a message from the server, the program assumes a disconnection and ends the game
    if not client1Message:
        print("Server Disconnected :(")
        break

        # Prints whatever message the server sent
    print(client1Message, end='')

    # The check for if the server sent to enter a move
    if "Enter your move" in client1Message:
        move = input("Your move (rock, paper, scissors, or quit): ").strip().lower()

        # Sends the move to the server
        client1.send(move.encode())

        # If the move is quit, ends the game
        if move == "quit":
            print("Input is Quit. Exiting Game. Goodbye!")
            break

    # The check for if the server sent to ask if the player wants to play again
        elif "Would you like to play again?" in client1Message:

        # Takes input from the player on if they want to play again
         play_again = input("Would you like to play again? (yes/no): ").strip().lower()

        # Sends the player's decision to the server
        client1.send(play_again.encode())

        # Pause for 3 seconds before clearing the console
        time.sleep(3000)

        # Clears the console for a fresh start if the player wants to play again
        if play_again == "yes":
            os.system('cls' if os.name == 'nt' else 'clear')

        # If the player does not want to play again, exits the game
        if play_again != "yes":
            print("Exiting Game. Goodbye!")
            break
    # Closes the socket as a means of cleanup
    client1.close()
