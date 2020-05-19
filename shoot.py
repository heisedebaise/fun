import random

WIDTH = 300
HEIGHT = 900

alien = Actor('alien')
alien.midtop = WIDTH/2, 0
alienWidth = 66
alienHeight = 92
count = 1
direction = 1


def draw():
    screen.clear()
    alien.draw()


def update():
    global count, direction
    count += 1
    if alien.left <= 0:
        direction = 1
    elif alien.right >= WIDTH:
        direction = -1
    elif count % 50 == 0:
        direction = 1 if random.randint(0, 1) == 1 else -1
    alien.left += direction*random.randint(0, 3)

    alien.top += 1
    if alien.bottom > HEIGHT:
        alien.top = 0
