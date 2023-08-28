'''
Jovienne Trotta
CS 5001 | Fall 2022
Lab 2: Crypto Currency Conversion

This creates the US dollar sign using python turtle.
'''

from turtle import *

#this will set the fill color to green
fillcolor("green")

#this will create the green dollar sign
begin_fill()
forward(90)
right(90)
forward(60)
right(90)
forward(30)
right(90)
forward(30)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(90)
right(90)
forward(120)
right(90)
forward(120)
right(90)
forward(60)
right(90)
forward(30)
right(90)
forward(30)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(90)
right(90)
forward(120)
right(90)
forward(30)
end_fill()

#this will set the fill color to green
fillcolor("black")

#this will create the first black line through the dollar sign
begin_fill()
left(90)
forward(30)
right(90)
forward(10)
right(90)
forward(270)
right(90)
forward(10)
right(90)
forward(270)
end_fill()

#this will create the second black line through the dollar sign
up()
right(90)
forward(50)
down()
begin_fill()
forward(10)
right(90)
forward(270)
right(90)
forward(10)
right(90)
forward(270)
end_fill()

#this will draw the picture
mainloop()
