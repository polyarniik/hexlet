import math
import random


def calculate_gcd(a, b):
    return math.gcd(a, b)


def play_gcd_game():
    print("Welcome to the Brain Game!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")

    for _ in range(3):
        num1 = random.randint(1, 50)
        num2 = random.randint(1, 50)
        correct_answer = calculate_gcd(num1, num2)

        print("Question:", num1, num2)
        user_answer = int(
            input("What is the greatest common divisor of the two numbers? ")
        )

        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"Sorry, {name}, but the correct answer was {correct_answer}")
            return

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    play_gcd_game()
