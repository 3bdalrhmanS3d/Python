import random

print("Hi! Welcome to the Number Guessing Game.\nYou have 7 chances to guess the number between 0 and 99. Let's start!")

# Randomly select a number between 0 and 99
number_to_guess = random.randrange(100)

# Set the maximum number of attempts
max_attempts = 7 
guess_counter = 0 

# Game loop for guessing
while guess_counter < max_attempts:
    guess_counter += 1  # Increment the guess counter
    my_guess = int(input('Please enter your guess: '))

    # Check if the guess is correct
    if my_guess == number_to_guess:
        print(f'Congratulations! The number was {number_to_guess}. You found it in {guess_counter} attempts!')
        break

    # Check if the user has exhausted their chances
    if guess_counter == max_attempts:
        print(f'Oops! The number was {number_to_guess}. Better luck next time!')
        break

    # Provide hints based on the guess
    if my_guess > number_to_guess:
        print('Your guess is too high.')
    elif my_guess < number_to_guess:
        print('Your guess is too low.')

# End of game message
if guess_counter < max_attempts:
    print('Thank you for playing!')
