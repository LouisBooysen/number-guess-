import random
# game intro
print("this is a number guessing game.")
print("guess a number between 1 and 20.")

# Generate random number
secret_number = random.randint(1, 20)

# generate guess variable
guess = None

# Loop until the correct guess
while guess != secret_number:
    guess = int(input("Take a guess: "))
    
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number {secret_number} correctly!")

