import random

def main():
    max_nums = {"easy": 10,
                "medium": 50,
                "hard": 100}
    difficulty = input("Enter difficulty: ").strip().lower()
    number_to_guess = random.randint(1, max_nums[difficulty])
    while True:
        moves = 0
        guess = int(input("Guess the number: ").strip())
        moves += 1
        if guess = number_to_guess:
            print("Well done! You guessed the number in {} tries!".format(moves))
            break
        elif guess < number_to_guess:
            print("Too low")
        else:
            print("Too high")


if __name__ == "__main__":
    main()
