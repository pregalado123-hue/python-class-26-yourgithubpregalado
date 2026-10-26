# Starting file for PROJECT 1
# Include your course number, student first and last name, and date in the comment header
# Project: Green Thumb Garden Shop
# Name: Philip R.
# Course: CS 31

# Welcome the customer
print("Welcome to Green Thumb Garden Shop!")
print("We provide friendly and affordable garden maintenance services.")

# Ask if the customer wants to learn more
learn_more = input("Would you like to learn more? (yes/no): ")

# Decide what to do with the answer
if learn_more.lower() === "yes":
  print()
  print("We help keep your garden clean, healthy, and beautiful!")
  print("Our garden maintenance service costs $25.00.")

# Ask if the customer wants to purchase 
purchase = input("Would you like to purchase our service? (yes/no): ")

If purchase.lower() == "yes":
# Collect customer information
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
email = input("Enter your email address: ")
phone = input("Enter your phone number: ")

# Set the service price
price = 25.00

# Ask for quantity and convert the answer to a number
quantity = int(input("How many services would you like to purchase? "))

# Calculate the purchase
subtotal = quantity * price
tax = subtotal * 0.10
total = subtotal + tax

# Print the receipt
print()
print("===================================")
print("       GREEN THUMB GARDEN SHOP")
print("             SALES RECEIPT")
print("===================================")
print("Customer:", first_name, last_name)
print("Email:", email)
print("Phone:", phone)
print("-----------------------------------")
print("Quantity:", quantity)
print("Price per service: $", format(price, ".2f"))
print("Subtotal: $", format(subtotal, ".2f"))
print("Sales tax (10%): $", format(tax, ".2f"))
print("TOTAL DUE: $", format(total, ".2f"))
print("===================================")
print("Thank you for supporting our garden shop!")
print("Have a wonderful day!")

else:
print("Thank you for visiting Green Thumb Garden Shop!")
print("Have a wonderful day!")

else:
print("Thank you for your time!")
print("Goodbye from Green Thumb Garden Shop!")
