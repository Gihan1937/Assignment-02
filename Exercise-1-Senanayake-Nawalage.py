# -*- coding: utf-8 -*-
"""
Program: Assignment 02
Author: Paolo
Last date modified: 2022/09/20

"""

## question 01

### libraries ###
# import the math library
from math import *

# Welcome Message
welcome = 'Welcome to Simple Calculator.'
print(welcome)

### Variables
# Message to be displayed at the start
user_message_1 = 'Please enter number 01: '
user_message_2 = 'Please enter number 02: '
operation_symbol = 'Please enter the Operation symbol from(+,-,*,/) and $ to exit: '


### receive input
# read user input & store in variables
user_input_1 = input(user_message_1)
user_input_2 = input(user_message_2)
user_input_3 = input(operation_symbol)

### Logic
# cast input from text to number
number_1 = int(user_input_1)
number_2 = int(user_input_2)

# perform the calculation: selecting the mathamatical operation to do

if(user_input_3 == '+'):
   print('Sum of 2 numbers is: ',number_1 + number_2) 

elif(user_input_3 == '-'):
   print('Difference of 2 numbers is: ',number_1 - number_2)

elif(user_input_3 == '*'):
   print('Product of 2 numbers is: ',number_1 * number_2)

elif(user_input_3 == '/'):
   print('Division of 2 numbers is: ',number_1 / number_2)

elif(user_input_3 == '$'):
   print('Exit')

else:
    print('Invalid Insert')






