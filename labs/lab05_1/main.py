# Starting file for LAB 5-1
# Include your course number, student first and last name, and date in the comment header
#CS 31 - Lab 5.1 
# Name: Philip R
# Date: 10/30/2026

# Import the nameformat module
import nameformat

# Main function
def main():

  # Display welcome message
  print("The NameFormat Module")
  print()
  print("Hello!")
  print()

# Ask the user for their name
firstName = input("Please enter your first name:")
lastName = input("Please enter your last name: ")

print()

# Start the menu loop 
while True:

  # Display menu options 
  print("******** MENU ********")
  print()
  print("1 - Say Hello")
  print("2 - Output Full Name")
  print("3 - Output Last Name, First Name")
  print("4 - Read Documentation")
  print()

# Ask user to select an option 
choice = input("What is your choice?")

print()

# Option 1 - Say Hello 
if choice == "1":
  print(nameformat.sayHello(firstName))

# Option 2 - Full Name 
elif choice == "2":
  print(nameformat.fullName(firstName, lastName))

# Option 3 Last Name First 
elif choice == "3":
  print(nameformat.lastNameFirst(firstName, lastName))

# Option 4 - Documentation
elif choice == "4":
  print("NameFormat Documentation")
  print()

  help(nameformat)
  help(nameformat.sayHello)
  help(nameformat.fullName)
  help(nameformat.lastNameFirst)

# Option 5 - Exit
elif choice == "5":
  print("Goodbye!")
  break

# Invalid menu selection
else:
  print("Invalid choice. Please select 1 through 5.")

print()

# Run the main Program
if__name__ == "__main__":
main()
