import turtle

def koch_snowflake(length, level):
    if level == 0:
        turtle.forward(length)
    else:
        length /= 3
        koch_snowflake(length, level - 1)
        turtle.left(60)
        koch_snowflake(length, level - 1)
        turtle.right(120)
        koch_snowflake(length, level - 1)
        turtle.left(60)
        koch_snowflake(length, level - 1)

def draw_snowflake(length, level):
    for _ in range(3):
        koch_snowflake(length, level)
        turtle.right(120)

def main():
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-150, 100)  # Центрування сніжинки
    turtle.pendown()

    recursion_level = int(input("Введіть рівень рекурсії: "))
    length = 300  # Довжина сторони

    draw_snowflake(length, recursion_level)
    turtle.done()

if __name__ == '__main__':
    main()