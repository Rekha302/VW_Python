import random

secret_number = random.randint(1, 100)
attempts = 7

for i in range(attempts):
    guess = int(input("Enter your guess (1-100): "))

    if guess > secret_number:
        print("Too high! Try a smaller number.")
    elif guess < secret_number:
        print("Too low! Try a larger number.")
    else:
        print("Congratulations! You guessed the number.")
        break
else:
    print("You lost! The correct number was:", secret_number)
