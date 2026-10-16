# Starting file for LAB 3-2
# Include your course number, student first and last name, and date in the comment header

# display a welcome message
print("The Test Scores application")
print()

# setting a default choice for the while loop
repeat_test_scores = "y"


while repeat_test_scores.lower() == "y":
    print("Enter test scores")
    print("Enter 999 to end input")
    print("======================")

    # initialize variables
    counter = 0
    score_total = 0
    test_score = 0

    while test_score != 999:
        test_score = int(input("Enter test score or end to end input: "))
        if test_score.lower() == "end":
            break
        else:
            # change the input to an integer
            test_score = int(test_score)
        if 0 <= test_score <= 100:
            score_total += test_score
            counter += 1
        else:
            print(f"Test score must be from 0 through 100. "
                f"Score discarded. Try again.")

    # calculate average score
    average_score = round(score_total / counter)
                    
    # format and display the result
    print("======================")
    print(f"Total Score: {score_total}"
        f"\nAverage Score: {average_score}")
    print()
    repeat_test_scores = input("Would you like to enter another set of test scores? (y/n): ")
print()


print("Goodbye. Thank you for using the Test Scores application!")

