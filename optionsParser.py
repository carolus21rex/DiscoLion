def answers(answers_csv):
    # Split the CSV string into individual values
    answer_values = answers_csv.split(',')

    # Initialize a list to store the integer values
    answer_list = []

    # Convert the values to integers and store them in the list
    for answer in answer_values:
        try:
            answer_int = int(answer)
            answer_list.append(answer_int)
        except ValueError:
            # Handle the case where a value cannot be converted to an integer
            # You can raise an error, skip the value, or handle it as needed
            print(f"Value '{answer}' is not a valid integer and will be skipped.")

    # Now, answer_list contains the integers from the CSV string
    return answer_list


