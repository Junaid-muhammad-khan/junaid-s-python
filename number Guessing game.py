import random


def guess(a):
    random_number = random.randint(1,a)
    guess = 0
    while guess != random_number:
        guess = int(input("Enter a number between 1 to 100: "))
        if guess > random_number:
            print("Try again.Too High")
        if guess < random_number:
            print("Try again.Too Low")

    print(f"You guessed the correct number {guess}!!")

guess(100)