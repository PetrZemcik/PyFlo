# This code creates the quiz.txt file for you to test with.
# You can change what gets written to test various scenarios!
f = open('quiz.txt', 'w')
f.write('what color is the sky?|||blue\nhow many years did it take to build the panama canal?|||10\nwhat is the term length in years for POTUS?|||4\nWhat color are the leaves of most plants?|||green\n')
f.close()

def load_questions_and_answers(file_name):
    # Put your code here!
    f = open(file_name, 'r')
    # Define dictionary to store questions and answers
    questions = {}
    # Loop through each line in the file
    for line in f:
        # Remove the newline character from the end of the line
        line = line.strip()
        # Split the line into a question and answer
        question, answer = line.split('|||')
        # Add the question and answer to the dictionary
        questions[question] = answer
    # Close the file
    f.close()
    # Return the dictionary
    return questions

questions=load_questions_and_answers('quiz.txt')
print(questions)
print()

def get_random_question(qa):
    # Put your code here!
    import random
    # Get a random question from the dictionary
    question = random.choice(list(qa.keys()))
    # Return the question # and answer
    return question# , qa[question]

def ask_question(qa):
    # Call get_random_question() and store the question and answer
    question = get_random_question(qa)
    # Print the question
    print(question)
    # Get the user's answer
    user_answer = input('Enter your answer: ')
    # Check if the user's answer is correct
    if user_answer == qa[question]:
        # Print a message if the answer is correct
        print('Correct!')
        # Remove the question from the dictionary
        del qa[question]
        return True
    else:
        # Print a message if the answer is incorrect
        print('Incorrect! The correct answer is: ' + qa[question])
        return False

# ask_question(questions)
# print(questions)

def main():
    file_name = input('What is the name of the QA file? ')
    number_of_questions = int(input('How many questions should be asked? '))
    questions_answers = load_questions_and_answers(file_name)
    correct_count = 0
    for i in range(number_of_questions):
        if ask_question(questions_answers):
            correct_count += 1
    print('You got', correct_count, 'out of', number_of_questions, 'correct.')
    print('Your percentage grade: ' + str(correct_count / number_of_questions * 100) + '%')

main()