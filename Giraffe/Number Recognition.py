# %%
# Import Libraries
import random                   # Randomization
#from gtts import gTTS          # Text to speech
#import os                      # Load/Save Files
#import io                      # IO
import pygame                   # Game utilities including playing sound from files
import pyttsx3                  # text to speech

# %%
import random

def setup_target_number_and_list():
    """
    Set up a random number and a CSV string of 4 random numbers, including the correct number.
    
    Returns:
        random_number (int): The generated random number.
        options_csv (str): A CSV string of 4 random numbers, including the correct number.
    """
    # Generate a random number between 0 and 9
    target_number = random.randint(0, 9)

    # Generate a list of 4 random numbers, including the correct number
    options = [target_number]
    while len(options) < 4:
        random_option = random.randint(0, 9)
        if random_option not in options:
            options.append(random_option)

    # Shuffle the options so the correct answer isn't always in the same position
    random.shuffle(options)

    # Convert the list of options to a CSV string
    options_csv = ",".join(map(str, options))

    return target_number, options_csv

# Example usage:
# random_number, options_csv = setup_target_number_and_list()
# number_text = str(random_number)  # You can convert the random_number to text here


# %%
import pyttsx3

def announce_number(number_text):
    """
    Announces a number with text-to-speech.

    Args:
        number_text (str): The number to announce.
    """
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Create a text-to-speech announcement for the number
    announcement_text = f"Pick number {number_text} to stop Gigi!"

    # Announce the number
    engine.say(announcement_text)

    # Play the announcement
    engine.runAndWait()

# Example usage:
# announce_number("5")

# %%
def display_pick_options(options_csv):
    """
    Display the pick options to the user.

    Args:
        options_csv (str): A CSV string containing the options to display.
    """
    options = options_csv.split(",")  # Split the CSV string into a list of options
    for i, option in enumerate(options):
        print(f"{i + 1}: {option}")

# Example usage:
# options_csv = "6,5,1,2"  # Replace with your CSV string of options
# display_pick_options(options_csv)


# %%
import pyttsx3

def get_user_input(options_csv, random_number):
    """
    Get user input and repeatedly prompt until valid input is provided.

    Args:
        options_csv (str): A CSV string containing the options.
        random_number (int): The correct random number.

    Returns:
        bool: True if the user guessed correctly, False otherwise.
    """
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Split the CSV string into a list of options
    options = options_csv.split(",")

    # Get user input and repeatedly prompt until valid input is provided
    while True:
        try:
            user_guess = int(input())
            if 1 <= user_guess <= len(options):
                picked_number = int(options[user_guess - 1])
                if picked_number == random_number:
                    engine.say("Yay, you got it! Roar!")
                else:
                    engine.say(f"Oops! The number you picked was {picked_number}.")
                engine.runAndWait()
                return picked_number == random_number  # True if correct, False otherwise
            else:
                print("Invalid input. Looping.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Example usage:
# options_csv = "6,5,1,2"  # Replace with your CSV string of options
# random_number = 1  # Replace with the correct random number
# result = get_user_input(options_csv, random_number)


# %%
import random
import pyttsx3

def Gigi_Attack_Number_Recognition():
    """
    Gigi Attack - Number Recognition game.
    """
    # Set up target number and options list
    target_number, options_csv = setup_target_number_and_list()

    # Announce Target Number
    announce_number(target_number)

    # Display Pick Options
    display_pick_options(options_csv)

    # Get play input
    win = get_user_input(options_csv, target_number)

    # Return
    return win

# Example usage:
# if __name__ == "__main__":
#     result = Gigi_Attack_Number_Recognition()


# %%
win = Gigi_Attack_Number_Recognition()
print(win)


