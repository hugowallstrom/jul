from turtle import *
import random
pencolor('black')
pensize(4)
speed(0)
def get_mouse_click_coor(x, y):
    print(x, y)
    pencolor('black')
    pensize(random.randint(1, 10))
    pendown()
    setx(x)
    sety(y)
    penup()

onscreenclick(get_mouse_click_coor)

mainloop()