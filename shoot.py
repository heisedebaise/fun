import random

WIDTH = 300
HEIGHT = 900

alien = Actor('alien')
alien.midtop = WIDTH/2, 0
fighter = Actor('fighter')
fighter.midbottom = WIDTH/2, HEIGHT
count = 1
direction = 1


def draw():
    screen.clear()
    alien.draw()
    fighter.draw()


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

    if keyboard.a:
        fighter.left -= 2
        if fighter.left <= 0:
            fighter.left = 0
    elif keyboard.d:
        fighter.left += 2
        if fighter.right >= WIDTH:
            fighter.right = WIDTH
    elif keyboard.w:
        fighter.top -= 1
        if fighter.top <= 0:
            fighter.top = 0
    elif keyboard.s:
        fighter.top += 1
        if fighter.bottom >= HEIGHT:
            fighter.bottom = HEIGHT
