#!/usr/bin/env python3

# Created by: Hussein Mansour
# Created on: Tue/May4/2021
# This program is "Positive / Negative / 0" program


def main():
    # this function checks if the integer number is Positive / Negative / 0

    # input
    int_number = int(input("Enter an integer:"))

    # process & output
    if (int_number > 0):
        print("{} is a positive number.".format(int_number))
    elif (int_number < 0):
        print("{} is a negative number.".format(int_number))
    elif (int_number == 0):
        print("0 is just a zero!")
    else:
        print("no idea!")

    print("\nDone.")


if __name__ == "__main__":
    main()
