import random

print("Number guessing game")
number = random.randint(1, 9)

chances = 0

print("Guess a number (between 1 and 9):")


while True:

    # Enter a number between 1 to 9
    guess = int(input())


    if guess == number:
        print(
            f'CONGRATULATIONS! YOU HAVE GUESSED THE \
            NUMBER {number} IN {chances} ATTEMPTS!')

        break

    elif guess < number:
        print("Your guess was too low: Guess a number higher than", guess)

    else:
        print("Your guess was too high: Guess a number lower than", guess)

    # Increase the value of chance by 1
    chances += 1
    
