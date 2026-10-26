# Starting file for LAB 4
# Include your course number, student first and last name, and date in the comment header
# Starting file for LAB 4
# Course: CS 31
# Philip R. 
# Assignment: Labe 4 - Horticulture Challenge

import random

# THis function runs one round of the horticulture game. 
def play_game (name, difficulty):

# Set the number range and guess limit:
if difficulty == "EASY":
  max_number = 10
  max_tries = 5 
elif difficulty == "MEDIUM":
  max_number = 100
  max_tries = 8
else:
  max_number = 1000
  max_tries = 10

# Pick a random number for the player to guess. 
secret_number = random. randint(1, max_number)

print("\nWelcome to the Horticulture Challenge!")
print(f"I'm thinking of a number from 1 to {max_number}.")
print(f"You have {max_tries} guesses, {name}.")
print(Use your gardening knowledge and see if you can win!")

# Let the player guess until they win or run out of tries. 
for attempt in range(1, max_ties + 1):
  guess = int(input(f"Guess {attempt}: Enter a number: "))

if guess == secret_number:
  print(f"Great job, {name}! You guessed the number!")
  print("Your horticulture skills are growing!")
  return True
elif guess < secret_number:
  print("Too low! Try a higher number.")
else:
  print("Too high! Try a lower number.")

# The player loses if all guesses are used. 
print(f"\nGood try, {name}! You ran out of guesses.")
print(f"The secret number was {secret_number}.")
print("Keep practicing your horticulture skills!")

return False

This function controls the game and keeps track of scores.
f main():

  # Ask for the player's name.
  name = input("Welcome to the Horticulture Challenge! What is your name? ")
print(f"\nHello, {name}! Let's test your gardening skills.")

# Start the scoreboard at zero.
wwins = 0
losses = 0

# Let the player keep playing until they choose to stop.
play_again = "yes"

while play_again == "yes":

  # Ask the player to choose a difficulty.
  difficulty = input(
    "\nChoose your difficulty (EASY, MEDIUM, or HARD): "
  ).upper()

# Check that the difficulty is valid.
while difficulty not in ["EASY", "MEDIUM", "HARD"]:
  print("Please choose EASY, MEDIUM, or HARD.")
  difficulty = input("Choose your difficulty:").upper()

# Play a round and check whether the player won. 
won = play_game(name, difficulty)

# Update the scoreboard. 
if won:
  wins += 1
else:
  loses += 1

# Display the player's score after each round.
print("\n==============================")
print(f"HORTICULTURE SCOREBOARD: {name}")
print(f"Wins: {wins}")
print(f"Losses: {losses}")
print("==============================")

# Ask if the player wants to play another round.
play_again = input(
  "\nWould you like to play again? (yes/no): "
  ).lower()

 # Check that the answer is yes or no.
while play_again not in ["yes", "no"]:
  play_again = input(
   "Please enter yes or no: "
  ).lower()

 # End the game with a goodbye message.
print(f"\nThanks for playing, {name}!")
print("Keep growing your horticulture knowledge!")

# Start the game by calling the main function.
if __name__ == "__main__":
  main()
