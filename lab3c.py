#!/usr/bin/env python3
'''
Author: Mitchell Gregoris
Student ID: 133349191
Email: mgregoris2@myseneca.ca
Program Name: lab3c.py
Date: 2024-05-14
Description: function operations
'''

def operate(number1, number2, operator):
 if operator == "add":
    return int(number1) + int(number2)
 elif operator == "subtract":
    return int(number1) - int(number2)
 elif operator == "multiply":
    return int(number1) * int(number2)
 elif operator == "divide":
    return 'Error: function operator can be "add", "subtract", or "multiply"'

if __name__ == '__main__':
    print(operate(10, 5, 'add'))
    print(operate(10, 5, 'subtract'))
    print(operate(10, 5, 'multiply'))
    print(operate(10, 5, 'divide'))