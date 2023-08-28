'''
Jovienne Trotta
CS 5001 | Fall 2022
Lab 2: Crypto Currency Conversion

This creates the US dollar sign using python turtle.
'''

import turtle as t

def usdSign():

    #this will set the fill color to green
    t.fillcolor("green")

    #this will create the green dollar sign
    t.begin_fill()
    t.forward(90)
    t.right(90)
    t.forward(60)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(30)
    t.left(90)
    t.forward(60)
    t.left(90)
    t.forward(60)
    t.left(90)
    t.forward(90)
    t.right(90)
    t.forward(120)
    t.right(90)
    t.forward(120)
    t.right(90)
    t.forward(60)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(30)
    t.left(90)
    t.forward(60)
    t.left(90)
    t.forward(60)
    t.left(90)
    t.forward(90)
    t.right(90)
    t.forward(120)
    t.right(90)
    t.forward(30)
    t.end_fill()

    #this will set the fill color to green
    t.fillcolor("black")

    #this will create the first black line through the dollar sign
    t.begin_fill()
    t.left(90)
    t.forward(30)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(270)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(270)
    t.end_fill()

    #this will create the second black line through the dollar sign
    t.up()
    t.right(90)
    t.forward(50)
    t.down()
    t.begin_fill()
    t.forward(10)
    t.right(90)
    t.forward(270)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(270)
    t.end_fill()

    #this will draw the picture
    t.mainloop()
