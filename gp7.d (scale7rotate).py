import pygame

pygame.init()

size = (600, 800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Image Transformations")

font = pygame.font.SysFont(None, 30)
clock = pygame.time.Clock()

image_original = pygame.image.load('balloon.png')
image_scaled = pygame.transform.scale(image_original, (200, 200))
image_rotated = pygame.transform.rotate(image_original, 180)

positions = [
    (50, 100),  # Original image
    (350, 100),  # Rotated image
    (50, 500),  # Original scaled image
    (350, 500)  # Scaled image
]

titles = [
    "Original Image",
    "Rotated Image",
    "Original Image (scaled)",
    "Scaled Image"
]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    for i, title in enumerate(titles):
        title_surface = font.render(title, True, (255, 255, 255))
        screen.blit(title_surface, (positions[i][0], positions[i][1] - 50))

    screen.blit(image_original, positions[0])
    screen.blit(image_rotated, positions[1])
    screen.blit(image_original, positions[2])
    screen.blit(image_scaled, positions[3])

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
