# Starting file for LAB 2
# Include your course number, student first and last name, and date in the comment header
#CS 31 Philip R. 10/8/2026

# Horticulture Quiz
# This program asks the user 5 easy horticulture questions.

print("Horticulture Quiz")

# Ask for the user's name
name = input("What is your name? ")

# Greet the user
print(f"Hello, {name}! Welcome to the Horticulture Quiz.")

# Ask if the user wants to take the quiz
start = input("Would you like to take the quiz? (Yes/No): ").strip().lower()

if start == "yes":
    # Set the score counter to zero
    score = 0

    # Question 1
    print("\n1) What do plants need from the sun to grow?")
    print("A) Sunlight")
    print("B) Plastic")
    print("C) Rock")
    answer = input("Enter A, B, or C: ").upper()

    if answer == "A":
        print("Correct! Plants need sunlight.")
        score += 1
    else:
        print("Incorrect. The correct answer is A) Sunlight.")

    # Question 2
    print("\n2) What part of the plant absorbs water from the soil?")
    print("A) Flower")
    print("B) Roots")
    print("C) Leaves")
    answer = input("Enter A, B, or C: ").upper()

    if answer == "B":
        print("Correct! Roots absorb water.")
        score += 1
    else:
        print("Incorrect. The correct answer is B) Roots.")

    # Question 3
    print("\n3) What do we call the process of giving plants water?")
    print("A) Painting")
    print("B) Pruning")
    print("C) Watering")
    answer = input("Enter A, B, or C: ").upper()

    if answer == "C":
        print("Correct! Watering helps plants stay healthy.")
        score += 1
    else:
        print("Incorrect. The correct answer is C) Watering.")

    # Question 4
    print("\n4) Which tool is commonly used to prune small branches?")
    print("A) Hand pruners")
    print("B) Hammer")
    print("C) Screwdriver")
    answer = input("Enter A, B, or C: ").upper()

    if answer == "A":
        print("Correct! Hand pruners are used to cut small branches.")
        score += 1
    else:
        print("Incorrect. The correct answer is A) Hand pruners.")

    # Question 5
    print("\n5) What do we call the material added to soil to help plants grow?")
    print("A) Concrete")
    print("B) Fertilizer")
    print("C) Glass")
    answer = input("Enter A, B, or C: ").upper()

    if answer == "B":
        print("Correct! Fertilizer can provide nutrients for plants.")
        score += 1
    else:
        print("Incorrect. The correct answer is B) Fertilizer.")

    # Display the final score
    print("\n================================")
    print(f"Your final score is: {score}/5")
    print("================================")

    # Give feedback based on the score
    if score == 5:
        print("Awesome work! You are a horticulture rockstar!")
    elif score == 4:
        print("Nice job! You almost got a perfect score.")
    elif score >= 3:
        print("Good effort! Keep learning about plants.")
    else:
        print("Keep studying! You can grow your knowledge.")

    # Personalized farewell
    print("Thanks for playing, " + name + "!")
    print("Keep growing and have a great day!")

else:
    # Farewell if the user does not want to play
    print(f"No problem, {name}! Maybe next time. Have a great day!")
