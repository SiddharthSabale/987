import pygame as py
import math

py.init()

WIDTH, HEIGHT = 800, 600
SCROLL_SPEED = 6

screen = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption("Endless Scrolling in Pygame")
clock = py.time.Clock()
bg = py.image.load("ganpati.png").convert()


tiles = math.ceil(WIDTH / bg.get_width()) + 1
scroll = 0

running = True
while running:
    clock.tick(33)
    
    for i in range(tiles):
        screen.blit(bg, (bg.get_width() * i + scroll, 0))
    
    scroll -= SCROLL_SPEED
    if abs(scroll) > bg.get_width():
        scroll = 0
    
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
    
    py.display.update()

py.quit()
