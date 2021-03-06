import random

def main():
    max_nums = {"easy": 10,
                "medium": 50,
                "hard": 100}
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
