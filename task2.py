import turtle

angle = 35


def draw(sz, level):

    if level > 0:
        turtle.colormode(255)
        turtle.pencolor(0, 255//level, 0)
        turtle.fd(sz)
        turtle.rt(angle)
        draw(0.8 * sz, level-1)
        turtle.pencolor(0, 255//level, 0)
        turtle.lt(2 * angle)
        draw(0.8 * sz, level-1)
        turtle.pencolor(0, 255//level, 0)
        turtle.rt(angle)
        turtle.fd(-sz)


if __name__ == "__main__":
    window = turtle.Screen()
    window.bgcolor("white")
    turtle.speed('fastest')
    turtle.rt(-90)
    print("Pythagorean Tree level (7 - 15):")
    inp = int(input())
    draw(100, inp)
    window.mainloop()
