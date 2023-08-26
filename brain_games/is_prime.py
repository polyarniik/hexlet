import random


def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True


def play_prime_game():
    print("Welcome to the Brain Game!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")

    for _ in range(3):
        num = random.randint(1, 100)
        is_prime_num = is_prime(num)
        correct_answer = "yes" if is_prime_num else "no"

        print("Question:", num)
        user_answer = input("Is the number prime? (yes/no): ").lower()

        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"Sorry, {name}, but the correct answer was {correct_answer}")
            return

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    play_prime_game()
