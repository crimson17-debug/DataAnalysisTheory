import turtle

cir = turtle.Turtle()

cir.color("blue", "cyan")
cir.speed(500)

cir.begin_fill()  # sets border and filling

while True:
    for i in range(72):
        cir.forward(5)
        cir.left(5)

    cir.forward(10)



turlte.done()