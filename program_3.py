# Programmer: Austin Long
# Date: 2025-03-26
# Program: Average Numbers

# Program #3: Average Numbers
# Assume a file containing a series of integers is named numbers.txt and exists on the computer's disk.
# (please use the provided numbers.txt)
# Write a program that reads all of the numbers stored in the file and calculates their total.

# The program should handle the following exceptions:
# It should handle any IOError exceptions that are raised.
# It should handle any ValueError exceptions that are raised when the items that are read from the file
# are converted to a number.

import sys


def sum_numbers_from_file():
    ######################
    # Add your code here #
    ######################
    print("In the sum_numbers_from_file function")

    grand_total = 0
    try:
        # Read lines and convert to integers
        with open("numbers.txt") as names_file:
            for line in names_file:
                grand_total += int(line.strip())
    except IOError as err:
        # handle file exceptions
        print(f"An error occurred when reading the file: ", file=sys.stderr)
        exit(err.errno)
    except ValueError as err:
        # handle format exceptions
        print(
            "An error occurred when processing the file. One or more lines may not be integers."
        )

    # display output
    print(f"The grand total is {grand_total}.")


# You don't need to change anything below this line:
if __name__ == "__main__":
    sum_numbers_from_file()
