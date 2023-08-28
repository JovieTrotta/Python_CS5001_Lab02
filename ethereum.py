'''
Jovienne Trotta
CS 5001 | Fall 2022
Lab 2: Crypto Currency Conversion

This creates the Ethereum sign using python turtle.
'''

from turtle import *

#this make the first diamond black
fillcolor("black")

#this will create the black diamond in the Ethereum logo
begin_fill()
left(20)
forward(100)
left(140)
forward(100)
left(40)
forward(100)
left(140)
forward(100)
end_fill()

#this make the second shapes grey
fillcolor("grey")

#this will create the grey arrow pointing up in the Ethereum logo
up()
left(40)
forward(110)
down()
begin_fill()
left(140)
forward(110)
left(40)
forward(110)
right(160)
forward(130)
right(78)
forward(135)
end_fill()

#this will create the grey arrow pointing down in the Ethereum logo
up()
forward(20)
down()
begin_fill()
right(85)
forward(220)
right(115)
forward(220)
right(150)
forward(140)
left(60)
forward(140)
end_fill()

#this will draw the picture
mainloop()