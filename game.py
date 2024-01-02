# Import the random module for generating random choices
import random


# Define the available options for rock, paper, scissors
options=("rock" , "paper" ,"scissor")


# Set a flag to control the game loop
running=True


# Main game loop
while running:
    

    # Get player's name and choice
    player=input("Enter a name of player:")
    
    
    # Generate the computer's choice randomly
    computer= random.choice(options)
    
    
    # Keep prompting until a valid choice is made
    while player not in options:
         player= input(f"Enter a choice {player} :")
         

    # Print player and computer choices    
    print(f"player :{player}")
    print(f"computer :{computer}")


     # Determine the winner based on game rules
    if player=="rock" and computer=="scissor":
        print(" You Win :) ")
        
    elif player=="paper" and computer=="rock":
        print(" You Win :) ")
        
    elif player=="scissor" and computer=="paper":
        print(" You Win :) ")  
        
    elif player=="rock" and computer=="paper":
        print(" You Lose :( ") 
        
    elif player=="paper" and computer=="scissor":
        print(" You Lose :( ")
        
    elif player=="scissor" and computer=="rock":
        print(" You Lose :( ")    
        
    else: 
        print(" It is a tie ")  
        
    
    # Ask if the player wants to play again
    choice = input("you wanna play again? (y/n):")
    if choice == 'y':
         running = True
    else:
        running = False
        
        
# Print a final message    
print("THANKS FOR PLAYING")                   
          


