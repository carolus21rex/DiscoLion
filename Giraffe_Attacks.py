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
        return None  # Invalid puzzle type

    return {'Type': type, 'Question': question, 'Answer': target_number, 'Options': options_csv}


# %%
#Test calls


#Quiz = Gigi_Puzzle('Number',0,9)
#print(Quiz)
#Quiz = Gigi_Puzzle('Count',0,20)
#print(Quiz)
#Quiz = Gigi_Puzzle('Add',0,15)
#print(Quiz)                   
#Quiz = Gigi_Puzzle('Subtract',0,15)
#print(Quiz)

# %%
# Initialize a global dictionary to store scores for each quiz type
quiz_scores = {
    'Number': [],
    'Count': [],
    'Add': [],
    'Subtract': []
}

# %%
import random

def Gigi_Event():
    """
    Gigi Math Quiz Game.

    Called by Main to initiate Gigi event
    Selects puzzle based on results in quiz_scores
    
    Returns:
        dict: A dictionary containing the puzzle and results with keys:
              - 'QuizType': The type of quiz (e.g., 'Number', 'Counting', 'Add', 'Subtract').
              - 'Puzzle': A dictionary containing the puzzle with keys:
                - 'Question': The question of the puzzle.
                - 'Answer': The correct answer to the puzzle.
                - 'Options': A CSV string of options for the user to choose from.
              - 'Result': True if the user's answer is correct, False otherwise.
    """
    # List of available quiz types
    quiz_types = ['Number', 'Count', 'Add', 'Subtract']

    # Randomly choose a quiz type
    quiz_type = random.choice(quiz_types)

    # quiz_type = select_puzzle_type(quiz_scores) - Advanced version

    # Call the respective puzzle function based on the chosen quiz type
    if quiz_type == "Number":
        lowest = 0
        highest= 10
    elif quiz_type == 'Count':
        lowest = 0
        highest = 20
    elif quiz_type == 'Add':
        lowest = 0
        highest = 20
    elif quiz_type == 'Subtract':
        lowest = 0
        highest = 15
    
    puzzle = Gigi_Puzzle(quiz_type, lowest, highest)

    return puzzle

# %%
#puzzle = Gigi_Event()
#print(puzzle)

# %%
def Puzzle_Result(puzzle_info):
    puzzle_type = puzzle_info["puzzle_type"]
    answer = puzzle_info["answer"]
    user_selection = puzzle_info["user_selection"]
    
    # Calculate is_correct based on answer and user_selection
    is_correct = answer == user_selection
    
    # Update the scores based on the result
    if is_correct:
        quiz_scores[puzzle_type]["wins"] += 1
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


