import random

WIDTH = 800
HEIGHT = 600

alien = Actor('alien')
alien.pos = 400, 0
count = 1
direction = 1


def draw():
    screen.clear()
    alien.draw()


def update():
    global count, direction
    count += 1
    if count % 100 == 0:
        direction = random.randint(-1, 1)
    alien.left += direction*random.randint(0, 3)
    if alien.left < 0:
        alien.left = WIDTH
    elif alien.left > WIDTH:
        alien.left = 0
    alien.top += 1
    if alien.top > HEIGHT:
        alien.top = 0
