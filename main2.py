import turtle

turtle.Screen().bgcolor("Purple")
st = turtle.Screen()
st.setup(600,200)

turtle.title("Turtle WIndow")

board = turtle.Turtle()
board.begin_fill()
i = 1
for i in range(3):
    board.forward(100)
    board.left(120)

turtle.done()