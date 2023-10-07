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

def setup_target_number_and_list(lowest=0, highest=9):
    """
    Set up a random number and a CSV string of 4 random numbers, including the correct number.
    
    Returns:
        random_number (int): The generated random number.
        options_csv (str): A CSV string of 4 random numbers, including the correct number.
    """
    # Generate a random number between lowest and highest
    target_number = random.randint(lowest, highest)

    # Generate a list of 4 random numbers, including the correct number
    options = [target_number]
    while len(options) < 4:
        random_option = random.randint(lowest, highest)
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
import pyttsx3

def display_counting_objects(target_number):
    """
    Displays the number of objects equal to the target.

    Args:
        target_number (int or str): The target number to display.
    """
    # Convert the target number to an integer if it's given as a string
    if isinstance(target_number, str):
        try:
            target_number = int(target_number)
        except ValueError:
            print("Invalid target number.")
            return

    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Create a text-to-speech announcement
    announcement_text = f"Count the stars to stop Gigi!"
    engine.say(announcement_text)
    engine.runAndWait()

    # Display the target number of stars
    for i in range(target_number):
        print("*", end=" ")  # Display a star
        if (i + 1) % 5 == 0:  # Add a line break every 5 stars
            print()
    
    # Add a line break after stars
    print()  # Add a line break after the stars

# Example usage:
# display_counting_objects(10)  # Display 10 stars

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
def get_user_input(options_csv, random_number):
    """
    Get user input and repeatedly prompt until valid input is provided.

    Args:
        options_csv (str): A CSV string containing the options.
        random_number (int): The correct random number.

    Returns:
        int: The number picked by the user.
    """
    # Split the CSV string into a list of options
    options = options_csv.split(",")

    # Get user input and repeatedly prompt until valid input is provided
    while True:
        try:
            user_guess = int(input())
            if 1 <= user_guess <= len(options):
                picked_number = int(options[user_guess - 1])
                return picked_number
            else:
                print("Invalid input. Looping.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# %%
import pyttsx3

def Gigi_Attack_Number_Recognition(lowest=0, highest=9):
    """
    Gigi Attack - Number Recognition game.
    """
    # Set up target number and options list
    target_number, options_csv = setup_target_number_and_list(lowest, highest)

    # Announce Target Number
    announce_number(target_number)

    # Display Pick Options
    display_pick_options(options_csv)

    # Get player input
    picked_number = get_user_input(options_csv, target_number)

    # Determine win/losss
    win = picked_number == target_number

    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Announce the result
    if win:
        engine.say("Yay, you got it! Roar!")
        engine.runAndWait()
    else:
        engine.say(f"Oops! The number you picked was {picked_number}.")
        engine.runAndWait()

    # Return
    return win

# Example usage:
# if __name__ == "__main__":
#     result = Gigi_Attack_Number_Recognition()


# %%
import pyttsx3

def Gigi_Attack_Counting(lowest=0, highest=20):
    """
    Gigi Attack - Counting game.
    """
    # Set up target number and options list
    target_number, options_csv = setup_target_number_and_list(lowest,highest)

    # Display Counting Objects
    display_counting_objects(target_number)

    # Display Pick Options
    display_pick_options(options_csv)

    # Get player input
    picked_number = get_user_input(options_csv, target_number)

    # Determine win/losss
    win = picked_number == target_number

    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Announce the result
    if win:
        engine.say("Yay, you got it! Roar!")
        engine.runAndWait()
    else:
        engine.say(f"Oh no! There were {target_number}.")
        engine.runAndWait()

    # Return
    return win

# Example usage:
# if __name__ == "__main__":
#     result = Gigi_Attack_Number_Recognition()

# %%
import pyttsx3

def Gigi_Attack_Add(lowest=0, highest=20):
    """
    Gigi Attack - Addition game.
    """
    # Set up target number and options list
    target_number, options_csv = setup_target_number_and_list(lowest,highest)

    # Generate two random numbers that add up to the target number
    addend1 = random.randint(lowest, target_number)
    addend2 = target_number - addend1

    # Display Addition Formula
    display_addition_puzzle(target_number, addend1, addend2)

    # Display Pick Options
    display_pick_options(options_csv)

    # Get player input
    picked_number = get_user_input(options_csv, target_number)

    # Determine win/losss
    win = picked_number == target_number

    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Announce the result
    if win:
        engine.say("Yay, you got it! Roar!")
        engine.runAndWait()
    else:
        engine.say(f"Oh no! {addend1} plus {addend2} is {target_number}.")
        engine.runAndWait()

    # Return
    return win

# Example usage:
# if __name__ == "__main__":
#     result = Gigi_Attack_Number_Recognition()

# %%
def display_addition_puzzle(target_number, addend1, addend2):
    """
    Display the addition puzzle to the user.

    Args:
        target_number (int): The target number for the puzzle.
        num1 (int): The first random number.
        num2 (int): The second random number.
    """
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    print(f"{addend1} + {addend2} = ")
    engine.say(f"{addend1} plus {addend2} is?")
    engine.runAndWait()

# %%
#win = Gigi_Attack_Number_Recognition()
#print(win)

# %%
#win = Gigi_Attack_Counting()

# %%
#win = Gigi_Attack_Add()


