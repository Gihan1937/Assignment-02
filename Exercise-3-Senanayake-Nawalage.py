# -*- coding: utf-8 -*-
"""
Program: Assignment 02
Author: Paolo
Last date modified: 2022/09/20

"""

## question 03

### libraries ###
# import the turtle library
import turtle

# Welcome Message
welcome = 'Welcome to Turtle .'
print(welcome)

### Variables

# create the pen
pen = turtle.Pen()

# Message to be displayed at the start
user_message_1 = 'Please enter length of the rectangle you want: '
user_message_2 = 'Please enter width of the rectangle you want: '

### receive input
# read user input & store in variables
user_input_1 = input(user_message_1)
user_input_2 = input(user_message_2)

### Logic
# cast input from text to number
number_1 = int(user_input_1)
number_2 = int(user_input_2)

# draw
pen.forward(number_1)
pen.right(90)
pen.forward(number_2)
pen.right(90)
pen.forward(number_1)
pen.right(90)
pen.forward(number_2)
pen.right(90)


# close window on click
turtle.exitonclick()



