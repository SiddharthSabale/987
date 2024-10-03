import pygame
import random

pygame.init()

WHITE = [255, 255, 255]
LIGHT_BLUE = [173, 216, 230]  # Snowflake color
LIGHT_GREY = [192, 192, 192]  # Background color mimicking a cloudy sky
SIZE = [400, 400]

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Siddharth")

snowFall = [[random.randrange(0, 400), random.randrange(0, 400)] for _ in range(50)]

clock = pygame.time.Clock()
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(LIGHT_GREY)  # Setting the cloudy sky background

    for snowflake in snowFall:
        pygame.draw.circle(screen, LIGHT_BLUE, snowflake, 3)  # Drawing snowflakes
        snowflake[1] += 1
        if snowflake[1] > 400:
            snowflake[1] = random.randrange(-50, -10)
            snowflake[0] = random.randrange(0, 400)

    pygame.display.flip()
    clock.tick(20)

pygame.quit()
