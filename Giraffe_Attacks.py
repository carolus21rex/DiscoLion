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
# Initialize a global dictionary to store scores for each quiz type
quiz_scores = {
    'Number': [],
    'Count': [],
    'Add': [],
    'Subtract': []
}

quiz_scores['Number'] = []
quiz_scores['Count'] = []
quiz_scores['Add'] = []
quiz_scores['Subtract'] = []

print(quiz_scores)

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
    # quiz_type = random.choice(quiz_types)

    quiz_type = select_puzzle_type() # Advanced version

    # Call the respective puzzle function based on the chosen quiz type
    if quiz_type == "Number":
        lowest = 0
        highest= 10
    elif quiz_type == 'Count':
        lowest = 0
        highest = 5
    elif quiz_type == 'Add':
        lowest = 0
        highest = 20
    elif quiz_type == 'Subtract':
        lowest = 0
        highest = 15
    
    puzzle = Gigi_Puzzle(quiz_type, lowest, highest)

    return puzzle

# %%
def Puzzle_Result(puzzle_info):
    puzzle_type = puzzle_info["Type"]
    answer = puzzle_info["Answer"]
    user_selection = puzzle_info["Selection"]
    
    # Calculate is_correct based on answer and user_selection
    is_correct = answer == user_selection
    
    # Update the scores based on the result
    scores = quiz_scores[puzzle_type]
    scores.append(is_correct)

    # Keep only the last 10 results
    if len(scores) > 10:
        scores.pop(0)  # Remove the oldest score

    return is_correct

# %%
import random

def select_puzzle_type():
    # Calculate the percentage of wins for each type
    total_wins = {type: sum(quiz_scores[type][-10:]) for type in quiz_scores}

    # Determine the selected type based on cascading random chance
    selected_type = None

    # Start with "Number" type
    if random.random() < (1 - total_wins.get("Number", 0) / 10):
        selected_type = "Number"
    else:
        # If "Number" is not selected, try "Count" type
        if random.random() < (1 - total_wins.get("Count", 0) / 10):
            selected_type = "Count"
        else:
            # If "Count" is not selected, try "Add" type
            if random.random() < (1 - total_wins.get("Add", 0) / 10):
                selected_type = "Add"
            else:
                # If none of the above types are selected, choose "Subtract" type
                if random.random() < (1 - total_wins.get("Subtract", 0) / 10):
                    selected_type = "Subtract"
                else:
                    # If still none of the types are selected, choose randomly
                    selected_type = random.choice(["Number", "Count", "Add", "Subtract"])

    return selected_type


# %%
"""
# Gigi Simulation
import random

# Simulated sequence of Gigi events and puzzle results
for i in range(50):
    # Simulate Gigi event
    puzzle = Gigi_Event()
    print(i, puzzle)

    # Simulate puzzle result (80% success rate)
    is_correct = random.random() < 0.8

    # Create puzzle_info dictionary
    puzzle_info = {
        'Type': puzzle["Type"],
        'Question': puzzle["Question"],
        'Answer': puzzle["Answer"],
        'Selection': puzzle["Answer"] if is_correct else puzzle["Answer"] + 1
    }
    print(puzzle_info)

    # Pass puzzle_info to Puzzle_Result
    Puzzle_Result(puzzle_info)

    # Print updated scores
    print("\nUpdated Scores:")
    print(quiz_scores)
    print("=" * 30)
"""

# %%


# %%



