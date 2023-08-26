import operator
import random

OPERATORS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
}


def play_calculator_game():
    print("Welcome to the Brain Game!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")

    for _ in range(3):
        num1 = random.randint(1, 50)
        num2 = random.randint(1, 50)
        operator_str = random.choice(list(OPERATORS.keys()))
        operation = OPERATORS[operator_str]

        question = f"{num1} {operator_str} {num2}"
        correct_answer = operation(num1, num2)

        print("Question:", question)
        user_answer = int(input("Your answer: "))

        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"Sorry, {name}, but the correct answer was {correct_answer}")
            return

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    play_calculator_game()
