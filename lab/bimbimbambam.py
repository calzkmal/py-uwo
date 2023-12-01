import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()

def drawTurtle(myTurtle, linelen):
    myTurtle.forward(linelen)
    myTurtle.left(10)
    myTurtle.speed(50)
    drawTurtle(myTurtle, linelen-10)

drawTurtle(myTurtle, 40)
myWin.exitonclick()
