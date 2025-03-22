import turtle

turtle.Screen().bgcolor("Purple")
st = turtle.Screen()
st.setup(600,200)

turtle.title("Turtle WIndow")

board = turtle.Turtle()
i = 1
for i in range(3):
    board.forward(100)
    board.left(120)

board.penup()
board.left(90)
board.forward(50)

board.pendown()
board.right(90)

i = 1
for i in range(3):
    board.forward(100)
    board.right(120)

turtle.done()