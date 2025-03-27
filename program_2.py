# Programmer: Austin Long
# Date: 2025-03-26
# Program: Random Number File Writer

# Program #2: Random Number File Writer
# Write a program that writes a series of random numbers (up to 1000) to a file.
# Each random number should be in the range of 1 through 500.
# The application should let the user specify how many random numbers the file will hold
# (up to 1000).

import sys
import random


def main():
    filename = input("Enter the filename to write to: ")
    num_numbers = None
    while num_numbers == None:
        try:
            num_numbers = int(input("Enter the number of random numbers to write: "))
            if num_numbers < 0 or num_numbers > 1000:
                num_numbers = None
            else:
                break
        except ValueError:
            pass
        print(
            "Error. You must enter a positive integer less than or equal to 1000.",
            file=sys.stderr,
        )

    try:
        with open(filename, "w") as file:
            for _ in range(num_numbers):
                file.write(str(random.randint(1, 500)) + "\n")
    except IOError as err:
        print(f"An error occurred when writing to the file: {err}", file=sys.stderr)
        exit(err.errno)

    print("Done.")


if __name__ == "__main__":
    main()
