# -*- coding: utf-8 -*-
"""
Program: Assignment 02
Author: Paolo
Last date modified: 2022/09/20

"""

## question 06

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
user_message_1 = 'Please enter length of the line you want: '
user_message_2 = 'Please enter gap of the line you want: '
user_message_3 = 'Please enter angle of the line you want: '

### receive input
# read user input & store in variables
user_input_1 = input(user_message_1)
user_input_2 = input(user_message_2)
user_input_3 = input(user_message_3)

### Logic
# cast input from text to number
number_1 = int(user_input_1)
number_2 = int(user_input_2)
x = int(user_input_3)

# draw
pen.left(x)
pen.forward(number_1)
pen.backward(number_1)
pen.right(x)
pen.up()
pen.forward(number_2)

pen.down()
pen.left(x)
pen.forward(number_1)
pen.backward(number_1)

pen.right(x)
pen.up()
pen.forward(number_2)

pen.down()
pen.left(x)
pen.forward(number_1)
pen.backward(number_1)

pen.right(x)
pen.up()
pen.forward(number_2)

# close window on click
turtle.exitonclick()



