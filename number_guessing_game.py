import random


def play_game():
    number = random.randint(1, 100)
    attempts = 0

    print("\n===== NUMBER GUESSING GAME =====")
    print("I have selected a number between 1 and 100.")
    print("Try to guess it!")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            if guess < number:
                print("Too low!")

            elif guess > number:
                print("Too high!")

            else:
                print(f"Correct! You guessed it in {attempts} attempts.")
                break

        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    while True:
        play_game()

        again = input("\nDo you want to play again? (yes/no): ").lower()

        if again != "yes":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()