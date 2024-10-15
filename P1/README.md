# Number Guessing Game

## Description
The Number Guessing Game is an interactive program that challenges users to guess a randomly selected integer within a specified range. The game employs a binary search strategy to minimize the number of guesses needed to arrive at the correct answer.

## How It Works
1. The user inputs a range, e.g., from 1 to 100.
2. The program randomly selects an integer within that range.
3. The user makes guesses, and the program provides feedback on whether the guess was too high, too low, or correct.
4. The game continues until the user successfully guesses the number or exhausts the maximum allowed guesses.

### Example Scenarios
**Scenario 1:**
- User inputs a range from 1 to 100.
- The program randomly selects the number 42.
- The user guesses:
  - 50 → "Try Again! You guessed too high."
  - 25 → "Try Again! You guessed too small."
  - 37 → "Try Again! You guessed too small."
  - 43 → "Try Again! You guessed too high."
  - 40 → "Try Again! You guessed too small."
  - 41 → "Try Again! You guessed too small."
  - 42 → "Congratulations! You guessed the right number."
  
**Total Number of Guesses = 7**

**Scenario 2:**
- User inputs a range from 1 to 50.
- The program randomly selects the number 42.
- The user guesses:
  - 25 → "Try Again! You guessed too small."
  - 37 → "Try Again! You guessed too small."
  - 43 → "Try Again! You guessed too high."
  - 40 → "Try Again! You guessed too small."
  - 41 → "Try Again! You guessed too small."
  - 42 → "Congratulations! You guessed the right number."

**Total Number of Guesses = 6**

## Minimum Guesses Calculation
The minimum number of guesses required to find the correct number can be calculated using the formula:


## Step-by-Step Algorithm
1. User inputs the lower and upper bounds of the range.
2. The program generates a random integer between the specified bounds and stores it for future reference.
3. A loop is initiated for repetitive guessing.
4. The program evaluates the user's guess:
   - If the guess is greater than the random number: "Try Again! You guessed too high."
   - If the guess is smaller than the random number: "Try Again! You guessed too small."
   - If the guess is correct: "Congratulations!"
   - If the user fails to guess the number within the minimum number of guesses: "Better Luck Next Time!"

## Conclusion
This game not only tests the user's guessing ability but also encourages strategic thinking by minimizing the guessing range with each attempt. Enjoy playing and happy guessing!
