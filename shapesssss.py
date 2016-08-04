goto(0,0)
def draw_square(color):
    for i in range(4):
        pencolor(color)
        pendown()
        forward(80)
        right(90)
    penup()

draw_square("blue")
