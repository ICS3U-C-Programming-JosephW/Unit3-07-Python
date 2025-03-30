#!/usr/bin/env python3
# Created By: Joseph Wondimagnehu
# Date: Mar. 30, 2025
"""
This program checks if a user's age is older than 25
and younger than 40 to get an approval
from grandparents to date their grandchild. Adds additional
checks for validating age inputs.
"""


# Define the main function.
def main():
    # Get the user's entered age as a string.
    age_as_string = input("You want to date our grandchild? How old are you?\n")

    # Try to check the validity of the entered age.
    try:
        # Convert the age as a string to an integer.
        age = int(age_as_string)

        # Check if the user is older than 25 and younger than 40.
        if (age > 25) and (age < 40):
            # Display the user is approved of dating the grandchild.
            print("\nYou are approved of dating our grandchild.")
        # Also, check if the user enters an invalid age not between 0 and 120.
        elif (age < 0) or (age > 120):
            # Display the user needs to enter a valid age.
            print("\nPlease enter a valid age.")
        # Otherwise, they are too young or too old for expectations.
        else:
            # Display the user is not approved of dating the grandchild.
            print(
                "\nYou cannot date our grandchild! "
                "You must be older than 25 and younger than 40."
            )
    # Runs if int() could not convert the user's input value to an integer.
    except ValueError:
        # Display to the user that their age is not an integer.
        print(f"\n{age_as_string} is not an integer.")
    # Finally, run the last block of code in the try statement.
    finally:
        # Display a message thanking the user for playing.
        print("Thanks for playing!")


# Check if the special name of the file is __main__.
if __name__ == "__main__":
    # Run the main function if so.
    main()
