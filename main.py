"""Matrix Application calculator where a user enters 2 3x3 matrices
    and can conduct different math operations"""

import re
import sys
import numpy as np


def goodbye():
    """Print out goodbye message and exit app"""
    print("\nHave a good day. Goodbye!")
    sys.exit()


def check_continuation():
    """Method to check whether user wants to continue or exit app"""
    to_continue = input("Would you like to continue?\n"
                        "Enter a \'y\' for yes or \'n\' for no: ")
    while not to_continue or not to_continue.isalpha() or to_continue.lower() not in ['y', 'n']:
        to_continue = input("Please enter a \'y\' for yes or \'n\' for no: ")

    if to_continue.lower() == 'n':
        goodbye()
    else:
        return 'y'


def display_results(result, operation):
    """
    Method to display results from math operations.
    Parameters
    ----------
    result : array_like
        Array containing numbers whose results are desired.
    operation : Text of selected math operation
    """
    print("You selected " + operation + ". Here are the results: \n", result)
    print("Transpose of result: \n", np.transpose(result))
    print("Mean of rows of result: ", np.mean(result, 1))
    print("Mean of columns of result: ", np.mean(result, 0))


def addition(matrix1, matrix2):
    """Method to Adds matrices.
    Parameters
    ----------
    matrix1 : array_like
        Array containing numbers from users first input
    matrix2 : array_like
        Array containing numbers from users first input
    """
    result = np.add(matrix1, matrix2)
    display_results(result, "Addition")


def subtraction(matrix1, matrix2):
    """
    Method to Subtracts matrices.
    Parameters
    ----------
    matrix1 : array_like
        Array containing numbers from users first input
    matrix2 : array_like
        Array containing numbers from users first input
    """
    result = np.subtract(matrix1, matrix2)
    display_results(result, "Subtraction")


def matrix_multiply(matrix1, matrix2):
    """
    Method to Multiply matrices.
    Parameters
    ----------
    matrix1 : array_like
        Array containing numbers from users first input
    matrix2 : array_like
        Array containing numbers from users first input
    """
    result = np.matmul(matrix2, matrix1)
    display_results(result, "Multiplication")


def element_multiply(matrix1, matrix2):
    """
    Method to Element by element multiply matrices.
    Parameters
    ----------
    matrix1 : array_like
        Array containing numbers from users first input
    matrix2 : array_like
        Array containing numbers from users first input
    """
    result = np.multiply(matrix2, matrix1)
    display_results(result, "Multiplication")


def menu(matrix1, matrix2):
    """
    Method to get users input on what math operation to perform.
    Parameters
    ----------
    matrix1 : array_like
        Array containing numbers from users first input
    matrix2 : array_like
        Array containing numbers from users first input
    """
    print("Select a matrix operation from the list: \n"
          "a. Addition \n"
          "b. Subtraction \n"
          "c. Matrix Multiplication \n"
          "d. Element by element multiplication \n"
          "e. Exit Application")

    option = input("\nWhat would you like to do? \n"
                   "Enter \'a\' through \'d\' or to exit program enter \'e\': ")

    valid_inputs = ['a', 'b', 'c', 'd', 'e']

    while not option or option.lower() not in valid_inputs:
        option = input("\nOops, you may have accidentally entered an invalid entry. \n"
                       "Please only enter \'a\' through \'d\' or to exit program enter \'e\': ")

    option = option.lower()
    if option == 'e':
        goodbye()

    if option == 'a':
        addition(matrix1, matrix2)

    if option == 'b':
        subtraction(matrix1, matrix2)

    if option == 'c':
        matrix_multiply(matrix1, matrix2)

    if option == 'd':
        element_multiply(matrix1, matrix2)

    if check_continuation() == 'y':
        menu(matrix1, matrix2)


def define_matrices():
    """Method to get two 3x3 matrices from user and validates input"""
    matrix_a = input("Enter your first 3x3 matrix. separate by each number by dash.\n"
                     "(Ex: 1-2-3-2-3-4-3-4-5): ")
    matrix_a_list = matrix_a.split("-")
    while not matrix_a or not matrix_a.replace("-", "").isnumeric() or len(matrix_a_list) != 9:
        matrix_a = input("Please enter a valid input for your first matrix \n"
                         "(Ex: 1-2-3-2-3-4-3-4-5): ")
        matrix_a_list = matrix_a.split("-")

    row1 = [int(i) for i in matrix_a_list[:3]]
    row2 = [int(i) for i in matrix_a_list[3:6]]
    row3 = [int(i) for i in matrix_a_list[6:9]]

    matrix1 = np.array([list(row1), list(row2), list(row3)])

    print("Your first 3x3 matrix is: \n", matrix1)

    matrix_b = input("Enter your second 3x3 matrix. separate by space.\n"
                     "(Ex: 1-2-3-2-3-4-3-4-5): ")
    matrix_b_list = matrix_b.split("-")
    while not matrix_b or not matrix_b.replace("-", "").isnumeric() or len(matrix_b_list) != 9:
        matrix_b = input("Please enter a valid input for your second matrix \n"
                         "(Ex: 1-2-3-2-3-4-3-4-5): ")
        matrix_b_list = matrix_b.split("-")

    row1 = [int(i) for i in matrix_b_list[:3]]
    row2 = [int(i) for i in matrix_b_list[3:6]]
    row3 = [int(i) for i in matrix_b_list[6:9]]
    matrix2 = np.array([list(row1), list(row2), list(row3)])

    print("Your second 3x3 matrix is: \n", matrix2)

    if check_continuation() == 'y':
        menu(matrix1, matrix2)


def main():
    """Main menu to get users phone number and zipcode"""
    print("********Welcome to Jackie\'s Matrix Calculator********")
    play = input("Do you want to play the matrix game?\n"
                 "Enter \'y\' for yes or \'n\' for no: ")

    while not play or not play.isalpha() or play.lower() not in ['y', 'n']:
        play = input("Please enter a \'y\' for yes or \'n\' for no: ")

    if play.lower() == 'n':
        goodbye()

    phone_regex = r"\w{3}-\w{3}-\w{4}"
    phone = input("Enter your 9 digit phone number (Ex: 301-999-3333): ")
    phone_is_numeric = phone.replace("-", "").isnumeric()
    while not phone or not re.search(phone_regex, phone) or not phone_is_numeric:
        phone = input("Please enter a valid 9 digit phone number \n"
                      "(Ex: 301-999-3333): ")
        phone_is_numeric = phone.replace("-", "").isnumeric()

    zip_regex = r"\w{5}-\w{4}"
    zipcode = input("Enter your full zip code with 4 digits & hyphen (Ex: 20770-3245): ")
    zip_is_numeric = zipcode.replace("-", "").isnumeric()
    while not zipcode or not re.search(zip_regex, zipcode) or not zip_is_numeric:
        zipcode = input("Please enter a valid input for your full zip code (Ex: 20770-3245): ")
        zip_is_numeric = zipcode.replace("-", "").isnumeric()

    define_matrices()


main()
