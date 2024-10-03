import pygame

pygame.init()

# Create the display surface object
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Moving Rectangle")

# Initial marker coordinates and dimensions
x, y = 200, 200
width, height, vel = 10, 10, 10

run = True

while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 500 - width:
        x += vel
    if keys[pygame.K_UP] and y > 0:
        y -= vel
    if keys[pygame.K_DOWN] and y < 500 - height:
        y += vel

    win.fill((0, 0, 0))  # Clear the screen
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))  # Draw the rectangle
    pygame.display.update()

pygame.quit()
