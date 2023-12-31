#===================================================================================================
#  ?                                           ABOUT
#  @author         :  Santiago Arellano
#  @repo           :  Battleship.io
#  @createdOn      :  08-06-23
#  @description    :  Main Implementation of the Battleship.io Python Representation
#===================================================================================================

#! Preproccesing Directives
from BPG_Main_Menu_Functions import Main_Menu_Option_1
from os import environ, getenv
from dotenv import load_dotenv

load_dotenv()
#? Main Greeting Interface and Game Start

welcome_screen_width: int =  int(environ.get('MAX_SCREEN_WIDTH'));
print("|Welcome to Battleship.io!|".center(welcome_screen_width,'='))
print("Choose one of the following Menu Options.\n1. Play a Game for Two.\n2. Quit the Game.")
user_choice: int = 0;
while (user_choice != 2):
    try:
        user_choice = int(input("Your choice: "))
        #? Block of Code Definition for Menu Option 1:
        if user_choice == 1:
            Main_Menu_Option_1();
        elif user_choice == 2:
            print("|Thank you for playing Battleship.io! See you next time!!|".center(welcome_screen_width,'='))


            
    except ValueError:
        print("Invalid Input. Please try again using the number defined for each menu option\nExample: To play the game input 1.")



