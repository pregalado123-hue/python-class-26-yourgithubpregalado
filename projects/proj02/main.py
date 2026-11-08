# Starting file for PROJECT 2
# Include your course number, student first and last name, and date in the comment header
# CS 31
# Philip R.
# November 7, 2026
# Project 2 - Brown or Green Thumb 

def main():
  print("Brown or Green Thumb")

  print("Welcome to my Mad Libs game!")
  print("Let's see how your day turns out!")
  print()

  play = input("WOuld you like to play? (y/n): ").lower()

  if play == "y":
    name = input("What is your name? ")
    print()
    print("Welcome,", name + "!")
    print("Let's see if you have a bown or green thumb!")

elif play == "n":
    print("Thanks for stopping by!")

else:
    print("Please enter y or n.")

if __name__ == "_main_":
  main()
