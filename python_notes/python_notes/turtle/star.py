import turtle
star = turtle.Turtle()

star.getscreen().bgcolor("black")

star.color("cyan", "blue")
star.speed(50)


for i in range(5):
    for i in range(5):
        for i in range(5):
            for i in range(5):
                star.begin_fill()
                star.forward(3)
                star.left(144)
                star.end_fill()

            star.forward(20)
            star.left(144)


        star.left(144)
        star.forward(70)


    star.forward(200)
    star.left(144)


turtle.done()