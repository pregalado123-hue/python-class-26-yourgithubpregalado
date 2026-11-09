# Starting file for PROJECT 2
# Include your course number, student first and last name, and date in the comment header
# CS 31
# Philip R.
# November 7, 2026
# Project 2 - Brown or Green Thumb

# Function to choose a story
def choose_story():
    print()
    print("Choose Your Story:")
    print("1. The Irrigation Disaster")
    print("2. The GIS Mapping Mystery")
    print()

    choice = input("Enter your choice (1 or 2): ").strip()
    while choice != "1" and choice != "2":
        print("Invalid choice. Please choose 1 or 2.")
        choice = input("Enter your choice (1 or 2): ").strip()
    return int(choice)


# Story 1: The Irrigation Disaster
def story_Irrigation_Disaster():
    print("The Irrigation Disaster")
    print("Answer the following questions to make your story.")

    coworker = input("What is the name of your coworker? ")
    animal = input("What is your favorite animal? ")
    number = input("What is your favorite number? ")
    tool = input("What is your favorite tool? ")
    adjective = input("Give me an adjective: ")
    food = input("What is your favorite food? ")

    print("Your Crazy Story: ")
    print("It was a normal morning at Long Beach City Park.")
    print(f"My coworker {coworker} and I were checking the irrigation system.")
    print(f"Suddenly, {number} sprinklers malfunctioned, spraying everywhere.")
    print(f"You and {coworker} grabbed your {tool}, but a very {adjective} {animal} appeared.")
    print(f"Then the sprinklers began spraying {food} instead of water!")
    print("Nobody knew what to do, but the park became a famous disaster overnight!")


# Story 2: The GIS Mapping Mystery
def story_GIS_Mapping_Mystery():
    print("The GIS Mapping Mystery")
    print("Answer the following questions to make your story.")

    city = input("What is a city you have visited? ")
    number = input("What is your favorite number? ")
    tree = input("What is a type of tree? ")
    object_name = input("What is a random object? ")
    color = input("What is your favorite color? ")
    animal = input("What is your favorite animal? ")
    person = input("Enter a name? ")

    print("Your GIS Story: ")
    print(f"You were assigned to map {number} {tree} trees in {city}.")
    print(f"While checking the data, you noticed a {object_name} on the map.")
    print(f"The {object_name} was marked as a {color} tree!")
    print(f"Even stranger, a {animal} was standing next to the {object_name}.")
    print(f"You called {person} to help investigate the strange location.")
    print("After checking the coordinates, you discover a hidden irrigation valve!")
    print("Thanks to the GIS mistake, the crew fixed the error and saved future problems!")


# Main game function
def main():
    print("Brown or Green Thumb:")
    print("Welcome to my Mad Libs game!")
    print("Let's see how your day turns out!")

    play = input("Would you like to play? (y/n): ").lower()
    if play == "y":
        print("Great! Let's get started!")
    elif play == "n":
        print("Thank you for visiting! Goodbye!")
        return
    else:
        print("Invalid choice. Please enter y or n.")
        return

    name = input("What is your name? ")
    print(f"Welcome, {name}! Let's begin your adventure!")

    story_choice = choose_story()
    if story_choice == 1:
        story_Irrigation_Disaster()
    elif story_choice == 2:
        story_GIS_Mapping_Mystery()

    print("Thanks for playing Brown or Green Thumb!")


# Start the program
if __name__ == "__main__":
    main()
