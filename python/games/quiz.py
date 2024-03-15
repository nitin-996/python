def new_games():
    guesses = []
    correct_guess = 0
    num = 0

# questins.items gave tuple in list

    for quest, opts in zip(questions.items(), options):
        print(quest[0])   # here first element of list comes which is a tuple
        for opt in opts:
            print(opt)
        guess = input("A, B, C, or D: ").upper()
        guesses.append(guess)
          
    # here we pass correct answer value with guess value , we access correct answer value from the tuple using indexing
        correct_guess += check_answer(quest[1], guess)
        num += 1

    display_score(correct_guess, guesses)

def check_answer(answer, guess):
    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0

def display_score(correct_guesses, guesses):
    print("--------------------------------")
    print("Results")
    print("--------------------------------")
    print("Answers:", end=" ")
    for key in questions.values():
        print(key, end=" ")
    print("\nGuesses: ", end="")
    for guess in guesses:
        print(guess, end=" ")
    print("\nCorrect Guesses:", correct_guesses)

questions = {
    "Who created Python?": "A",
    "What year was Python created?": "B",
    "Python is attributed to which comedy group?": "C",
    "Is the Earth round?": "B"
}

options = [
    ["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerberg"],
    ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
    ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
    ["A. True", "B. False"]
]

new_games()





