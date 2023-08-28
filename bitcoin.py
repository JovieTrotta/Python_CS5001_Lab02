'''
Jovienne Trotta
CS 5001 | Fall 2022
Lab 2: Crypto Currency Conversion

This creates the Bitcoin sign using python turtle.
'''

from turtle import *

scale = .75

#this will help shift the logo down a little further
up()
right(90)
forward(150)
left(90)
down()

#this will set the fill color to orange
fillcolor("orange")

#this will create the orange circle in the Bitcoin logo
begin_fill()
circle(200)
end_fill()

#this will set the fill color to white
fillcolor("white")

#this will create the "B" for Bitcoin
up()
left(90)
forward(60)
right(90)
forward(30)
(down)
begin_fill()
circle(80,180)
right(180)
circle(60,180)
forward(120)
left(90)
forward(30)
left(90)
forward(30)
right(90)
forward(220)
right(90)
forward(30)
left(90)
forward(30)
left(90)
forward(60)
end_fill()
up()
left(90)
forward(40)
right(90)
forward(20)
down()

#this will switch the color back to orange
fillcolor("orange")
color("orange")

#this will finish the "B"
begin_fill()
circle(80*scale,180)
right(180)
circle(60*scale,180)
left(90)
forward(220)
end_fill()

#this will draw the picture
mainloop()