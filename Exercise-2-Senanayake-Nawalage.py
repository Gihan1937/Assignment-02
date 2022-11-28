# -*- coding: utf-8 -*-
"""
Program: Assignment 02
Author: Paolo
Last date modified: 2022/09/20

"""

## question 02

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
user_message_1 = 'Please enter length of the square you want: '

### receive input
# read user input & store in variables
user_input_1 = input(user_message_1)

### Logic
# cast input from text to number
number_1 = int(user_input_1)


# draw
pen.forward(number_1)
pen.right(90)
pen.forward(number_1)
pen.right(90)
pen.forward(number_1)
pen.right(90)
pen.forward(number_1)
pen.right(90)


# close window on click
turtle.exitonclick()



