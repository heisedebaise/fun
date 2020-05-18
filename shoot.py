WIDTH = 800
HEIGHT = 600

alien = Actor('alien')

alien.pos = 400, 100

def draw():
    screen.clear()
    alien.draw()
