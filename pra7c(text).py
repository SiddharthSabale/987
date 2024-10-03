import pygame

pygame.init()

white, green, blue = (255, 255, 255), (0, 255, 0), (0, 0, 128)
size = (400, 400)

display_surface = pygame.display.set_mode(size)
pygame.display.set_caption('Show Text')
font = pygame.font.Font('freesansbold.ttf', 32)

text = font.render('Siddharth', True, green, blue)
text_rect = text.get_rect(center=(size[0] // 2, size[1] // 2))

running = True
while running:
    display_surface.fill(white)
    display_surface.blit(text, text_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
