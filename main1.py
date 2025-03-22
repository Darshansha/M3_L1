import turtle

turtle.Screen().bgcolor("Blue")
st=turtle.Screen()
st.setup(500, 290)

turtle.title("Turtle Window")

board = turtle.Turtle()
board.fillcolor("red")
board.begin_fill()
i = 1
for i in range(4):
    board.forward(100)
    board.left(90)
board.end_fill()


turtle.done()