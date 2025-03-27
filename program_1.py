# Programmer: Austin Long
# Date: 2025-03-26
# Program: Item Counter

# Program #1: Item Counter
# Assume a file containing a series of names (as strings) is named names.txt
# (Use the included example file names.txt) and exists on the computer's disk.
# Write a program that displays the number of names that are stored in the file.

import sys

def count_file_lines():
    ######################
    # Add your code here #
    ######################
    print("In the count_file_lines function")

    # Read file
    count = 0
    try:
        with open("names.txt") as names_file:
            for _ in names_file:
                count += 1
    except IOError as err:
        print(f"An error occurred when reading the file: {err}", file=sys.stderr)
        exit(err.errno)

    # Display to user
    print(
        f"There {'are' if count != 1 else 'is'} {count} name{'s' if count != 1 else ''} in names.txt"
    )


# You don't need to change anything below this line:
if __name__ == "__main__":
    count_file_lines()
