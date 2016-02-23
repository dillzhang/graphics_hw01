from display import *
from draw import *

screen = new_screen()
color = [ 0, 0, 0 ]

delta = [1, 1]
xory = 1
x = 0
y = 0
i = XRES
while i > 0:
    i += 1
    newX = x + i * delta[0] * xory
    newY = y + i * delta[1] * ((xory + 1) % 2)
    draw_line(screen, x, y, newX, newY, color)
    delta[0] *= xory * -2 + 1
    delta[1] *= (xory + 1) % 2 * -2 + 1
    xory = (xory + 1) % 2
    x = newX
    y = newY
    color[RED] = (color[RED] + 1) % MAX_COLOR
    color[GREEN] = (color[GREEN] + 3) % MAX_COLOR
    color[BLUE] = (color[BLUE] + 8) % MAX_COLOR
    i -= 3
display(screen)

