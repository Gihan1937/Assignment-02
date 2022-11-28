# -*- coding: utf-8 -*-
"""
Program: Assignment 02
Author: Paolo
Last date modified: 2022/09/20

"""

## question 07

### libraries ###
# import the turtle library
import turtle

# Welcome Message
welcome = 'Welcome to Turtle Selection.'
print(welcome)

### Variables

# create the pen
pen = turtle.Pen()

# Message to be displayed at the start
design = 'Please choose which pattern to draw 1.Horizontal, 2.Vertical, 3.Diagonal: ' 
user_message_1 = 'Please enter length of the line you want: '
user_message_2 = 'Please enter gap of the line you want: '

### receive input
# read user input & store in variables
design_input = input(design)
user_input_1 = input(user_message_1)
user_input_2 = input(user_message_2)

### Logic
# cast input from text to number
number_1 = int(user_input_1)
number_2 = int(user_input_2)

#checking the pattern choosed.
if(design_input == '1'):
    
    pen.forward(number_1)
    pen.up()
    pen.right(90)
    pen.forward(number_2)
    pen.right(90)

    pen.down()
    pen.forward(number_1)
    pen.up()
    pen.left(90)
    pen.forward(number_2)

    pen.down()
    pen.left(90)
    pen.forward(number_1)
    pen.up()
    pen.right(90)
    pen.forward(number_2)
    pen.left(90)
    pen.backward(number_1)

    # close window on click
    turtle.exitonclick()

elif(design_input =='2'):
    pen.left(90)
    pen.forward(number_1)
    pen.up()
    pen.right(90)
    pen.forward(number_2)
    pen.right(90)

    pen.down()
    pen.forward(number_1)
    pen.up()
    pen.left(90)
    pen.forward(number_2)

    pen.down()
    pen.left(90)
    pen.forward(number_1)
    pen.up()
    pen.right(90)
    pen.forward(number_2)
    pen.right(90)
    pen.forward(number_1)
    pen.left(180)


    # close window on click
    turtle.exitonclick()

elif(design_input =='3'):
    angle = 'Please enter angle of the line you want: '
    x = int(input(angle))

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
    
else:
    print('Invalid selection')
