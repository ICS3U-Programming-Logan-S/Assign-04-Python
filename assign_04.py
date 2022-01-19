#!/usr/bin/env python3

# Created by: Logan S
# Created on: Jan. 5, 2022
# This program asks the user to enter a positive number
# and then uses a loop to calculate and display the sum
# of all numbers from 0 until that number.

# Module found within imported modules and researched from
# https://www.w3schools.com/python/python_datetime.asp
import datetime
import time
# Module for the loop to have typing text
# Found from stackoverflow
from sys import stdout


def begin():

    # ask the user to start the program
    print("Today's date & time: {}" .format(datetime.datetime.now()))
    explanation = "This program reverses any sequence of numbers inputted."
    # Loop to have typing text
    for letter in explanation:
        time.sleep(0.06)  # In seconds
        stdout.write(letter)
        stdout.flush()

    print()
    print()
    time.sleep(0.5)
    begin_program = input("Begin reversing numbers? y/n: ")

    if begin_program == "y":
        main()
    elif begin_program == "n":
        print("Goodbye!")
    else:
        print()
        print("I don't understand that. I'll just assume you meant yes?")
        time.sleep(0.5)
        main()


def ask_again():

    # User input
    print()
    user_answer = input("Would you like to put another character? ")

    # Answer statement to respond to yes or no
    if user_answer == "yes" or user_answer == "y" or user_answer == "Yes":
        main()
    elif user_answer == "no" or user_answer == "n" or user_answer == "No":
        print()
        thank_you_message = "Thanks for trying it out anyway!"
        for letter in thank_you_message:
            time.sleep(0.06)  # In seconds
            stdout.write(letter)
            stdout.flush()
    else:
        print()
        print("Error. Try again?")
        print()
        ask_again()


def main():

    # get the user number as a string
    print()
    user_number = input("Enter a number: ")
    reversed_number = 0

    try:
        # initialize the integer version of the input
        user_number_int = int(user_number)

        # calculate the sum of all numbers from 0 to user number
        while (user_number_int > 0):
            reminder = user_number_int % 10
            reversed_number = (reversed_number * 10) + reminder
            user_number_int = user_number_int // 10
        print()
        reversed_version = "The reversed version of the entered number is"
        three_dots = "..."
        for letter in reversed_version:
            time.sleep(0.06)  # In seconds
            stdout.write(letter)
            stdout.flush()
        for letter in three_dots:
            time.sleep(0.3)  # In seconds
            stdout.write(letter)
            stdout.flush()

        time.sleep(1)
        print()
        print("{}!" .format(reversed_number))
        ask_again()
    except ValueError:
        print()
        invalid_entry = ("[{}] is an invalid entry. Please try again."
                         .format(user_number))
        for letter in invalid_entry:
            time.sleep(0.06)  # In seconds
            stdout.write(letter)
            stdout.flush()
        print()
        ask_again()


if __name__ == "__main__":
    begin()
