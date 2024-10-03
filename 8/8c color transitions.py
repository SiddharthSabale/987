import pygame
import random
import sys

pygame.init()
screen = pygame.display.set_mode((720, 600))

c1 = random.randint(0, 255)
c2 = random.randint(0, 255)
c3 = random.randint(0, 255)

clock = pygame.time.Clock()
c1_dir, c2_dir, c3_dir = 1, 1, 1

while True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if 0 <= c1 <= 255:
        c1 += c1_dir
    if c1 > 255 or c1 < 0:
        c1_dir *= -1
        c1 += c1_dir

    if 0 <= c2 <= 255:
        c2 += c2_dir
    if c2 > 255 or c2 < 0:
        c2_dir *= -1
        c2 += c2_dir

    if 0 <= c3 <= 255:
        c3 += c3_dir
    if c3 > 255 or c3 < 0:
        c3_dir *= -1
        c3 += c3_dir

    screen.fill((c1, c2, c3))
    pygame.display.update()
    clock.tick(60)
