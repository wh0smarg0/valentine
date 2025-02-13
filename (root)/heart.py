import turtle
import math

# Настройка окна
screen = turtle.Screen()
screen.bgcolor("black")

# Настройка черепашки
t = turtle.Turtle()
t.speed(0)
t.width(2)
t.color("red")
t.hideturtle()

# Функция для рисования сердца
def draw_heart():
    t.penup()
    t.goto(0, -150)  # Смещение вверх
    t.pendown()
    
    t.begin_fill()
    t.color("red")

    for angle in range(361):
        x = 16 * math.sin(math.radians(angle))**3
        y = 13 * math.cos(math.radians(angle)) - 5 * math.cos(2 * math.radians(angle)) - 2 * math.cos(3 * math.radians(angle)) - math.cos(4 * math.radians(angle))
        t.goto(x * 15, y * 15 - 100)  # Масштабируем и поднимаем вверх

    t.end_fill()

# Вызов функции рисования
draw_heart()

# Завершение программы
turtle.done()
