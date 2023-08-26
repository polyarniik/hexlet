import random


def is_even(number):
    return number % 2 == 0


def play_even_odd_game():
    print("Welcome to the Brain Game!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")

    for _ in range(3):
        num = random.randint(1, 100)
        is_even_num = is_even(num)
        correct_answer = "yes" if is_even_num else "no"

        print("Question:", num)
        user_answer = input("Is the number even? (yes/no): ").lower()

        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"Sorry, {name}, but the correct answer was {correct_answer}")
            return

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    play_even_odd_game()
