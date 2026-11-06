import random

secret = random.randint(1, 50)
max_attempts = 6
attempts = 0

print("Guess the number between 1 and 50")

while attempts < max_attempts:
    guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: "))
    attempts += 1

    if guess == secret:
        print(f"Correct! You won in {attempts} attempts.")
        break
    elif guess < secret:
        print("Too low")
    else:
        print("Too high")
else:
    print(f"Game over. The number was {secret}.")