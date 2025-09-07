import turtle


def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        size /= 3.0
        koch_curve(t, order - 1, size)
        t.left(60)
        koch_curve(t, order - 1, size)
        t.right(120)
        koch_curve(t, order - 1, size)
        t.left(60)
        koch_curve(t, order - 1, size)


def snowflake(order, size):
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, size / 3)
    t.pendown()
    for i in range(3):
        koch_curve(t, order, size)
        t.right(120)
    turtle.done()


if __name__ == "__main__":
    level = int(input("Введіть рівень рекурсії: "))
    snowflake(level, 300)
