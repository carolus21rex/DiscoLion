# %%
# Import Libraries
import random                   # Randomization
#from gtts import gTTS          # Text to speech
#import os                      # Load/Save Files
#import io                      # IO
#import pygame                  # Game utilities including playing sound from files
#import pyttsx3                  # text to speech

# %%
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
import random

def Gigi_Puzzle(type, lowest=0, highest=10):
    """
    Generate a Gigi event puzzle based on the specified type.

    Args:
        type (str): The type of puzzle ('Number', 'Count', 'Add', or 'Subtract').
        lowest (int): The lowest possible number for the puzzle.
        highest (int): The highest possible number for the puzzle.

    Returns:
        dict: A dictionary containing the puzzle with keys:
              - 'Question': The puzzle question as a string.
              - 'Answer': The correct answer.
              - 'Options': A CSV string of options for the user to choose from.
    """
    if type == 'Number':
        target_number, options_csv = setup_target_number_and_list(lowest, highest)
        question = f"Pick number {target_number} to stop Gigi!"
    
    elif type == 'Count':
        target_number, options_csv = setup_target_number_and_list(lowest, highest)
        question = f"Count the stars to stop Gigi!"
    
    elif type == 'Add':
        target_number, options_csv = setup_target_number_and_list(lowest, highest)
        addend1 = random.randint(lowest, target_number)
        addend2 = target_number - addend1
        question = f"{addend1} + {addend2} = "
    
    elif type == 'Subtract':
        target_number, options_csv = setup_target_number_and_list(lowest, highest)
        num1 = random.randint(target_number, highest)
        num2 = num1 - target_number
        question = f"{num1} - {num2} = ?"
    
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
    picked_number = get_user_input(options_csv)

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
def display_addition_puzzle(addend1, addend2):
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
import pyttsx3

def Gigi_Attack_Add(lowest=0, highest=10):
    """
    Gigi Attack - Addition game.
    """
    # Set up target number and options list
    target_number, options_csv = setup_target_number_and_list(lowest,highest)

    # Generate two random numbers that add up to the target number
    addend1 = random.randint(lowest, target_number)
    addend2 = target_number - addend1

    # Display Addition Formula
    display_addition_puzzle(addend1, addend2)

    # Display Pick Options
    display_pick_options(options_csv)

    # Get player input
    picked_number = get_user_input(options_csv)

    # Determine win/loss
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
import pyttsx3

def display_subtraction_puzzle(target_number, num1, num2):
    """
    Display the subtraction puzzle to the user.

    Args:
        target_number (int): The target number for the puzzle.
        num1 (int): The first random number.
        num2 (int): The second random number.
    """
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    print(f"{num1} - {num2} = ")
    engine.say(f"{num1} minus {num2} is?")
    engine.runAndWait()


# %%
def Gigi_Attack_Subtract(lowest=0, highest=10):
    """
    Gigi Attack - Subtraction game.
    """
    # Set up target number and options list
    target_number, options_csv = setup_target_number_and_list(lowest,highest)

    # Generate splits such that num2 - num 1 = target number with num1 > target_number
    num1 = random.randint(target_number, highest)
    num2 = num1 - target_number

    # Display the puzzle
    display_subtraction_puzzle(target_number, num1, num2)

    # Display Pick Options
    display_pick_options(options_csv)

    # Get player input
    picked_number = get_user_input(options_csv)

    # Determine win/loss
    win = picked_number == target_number

    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Announce the result
    if win:
        engine.say("Yay, you got it! Roar!")
    else:
        quiz_scores[puzzle_type]["losses"] += 1

# %%
def select_puzzle_type(quiz_scores):
    # Logic to select the puzzle type based on scores
    # Implement your own logic here

    # For example, select the puzzle type with the lowest score
    min_score = float("inf")
    selected_type = None
    for quiz_type, scores in quiz_scores.items():
        win_ratio = scores["wins"] / (scores["wins"] + scores["losses"]) if scores["losses"] > 0 else 1
        if win_ratio < min_score:
            selected_type = quiz_type
            min_score = win_ratio

    return selected_type


