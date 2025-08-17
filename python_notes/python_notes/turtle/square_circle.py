import turtle

su = turtle.Turtle()
su.color("blue", "cyan")
su.speed(500)

su.begin_fill()  # sets border and filling  



for i in range(200):
    su.left(45)
    for i in range(3):
        su.left(90)
        su.forward(100)


    su.forward(1)






turtle.done()  # this code is completed