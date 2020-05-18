WIDTH = 800
HEIGHT = 600

alien = Actor('alien')


def draw():
    screen.clear()
    alien.pos = 400, 100
    alien.draw()
