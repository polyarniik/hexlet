import random


def generate_progression(start, step, length):
    return [start + step * i for i in range(length)]


def play_progression_game():
    print("Welcome to the Brain Game!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")

    for _ in range(3):
        start = random.randint(1, 100)
        step = random.randint(2, 10)
        length = random.randint(5, 10)
        progression = generate_progression(start, step, length)
        missing_index = random.randint(0, length - 1)
        correct_answer = progression[missing_index]
        progression[missing_index] = ".."

        print("Question:", " ".join(map(str, progression)))
        user_answer = int(input("Your answer: "))

        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"Sorry, {name}, but the correct answer was {correct_answer}")
            return

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    play_progression_game()
