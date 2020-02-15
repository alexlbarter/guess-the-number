import random


def get_max_num(difficulty):
    max_nums = {"easy": 10,
                "medium": 50,
                "hard": 100}
    try:
        return max_nums[difficulty]
    except KeyError:
        return None


def generate_number(max_num):
    return random.randint(1, max_num)


def check_guess(guess, number_to_guess):
    if guess == number_to_guess:
        return "correct"


def main():
    while True:
        difficulty = input("Enter difficulty: ").strip().lower()
        try:
            number_to_guess = random.randint(1, max_nums[difficulty])
            break
        except KeyError:
            print("Invalid difficulty")
            continue
    moves = 0
    while True:
        try:
            guess = int(input("Guess the number: ").strip())
        except ValueError:
            print("Invalid input")
            continue
        else:
            moves += 1
        if guess == number_to_guess:
            print("Well done! You guessed the number in {} {}!".format(moves, "try" if moves == 1 else "tries"))
            break
        elif guess < number_to_guess:
            print("Too low")
        else:
            print("Too high")


if __name__ == "__main__":
    main()
