"""Game Project"""
import random


def get_guess():
    """
    :return: GET GUESS
    """
    return list(input("What is your guess: "))


def generate_code():
    """
    GENERATE COMPUTER CODE 123
    Shuffle the digits, Then grab the first three
    """
    digits = [str(num) for num in range(10)]
    random.shuffle(digits)
    return digits[:3]


def generate_clues(code, user_guess):
    """
    :param code: GENERATE THE CLUES
    :param user_guess: user guess input
    :return: code status
    """
    try:
        if user_guess == code:
            return "CODE CRACKED!"
        clues = []
        for ind, num in enumerate(user_guess):
            if num == code[ind]:
                clues.append("match")
            elif num in code:
                clues.append("Close")
        if not clues:
            return ["Nope"]
        return clues
    except IndexError:
        print("\nPlease enter three integer!\n")


# RUN GAME LOGIC
print("Welcome Code Breaker!")
SECRET_CODE = generate_code()
CLUE_REPORT = []
while CLUE_REPORT != "CODE CRACKED!":
    GUESS = get_guess()
    CLUE_REPORT = generate_clues(GUESS, SECRET_CODE)
    print("Here is the result of your guess: ")
    try:
        for clue in CLUE_REPORT:
            print(clue)
    except TypeError:
        print("\nPlease enter three integer.\n")
