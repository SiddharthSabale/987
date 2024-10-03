import pygame
import sys

pygame.init()

# Screen dimensions
res = (800, 600)
screen = pygame.display.set_mode(res)
pygame.display.set_caption("Button Example")

# Colors
color = (255, 255, 255)
color_light = (170, 170, 170)
color_dark = (100, 100, 100)

# Font settings
smallfont = pygame.font.SysFont('Corbel', 35)
text = smallfont.render('Quit', True, color)

# Button dimensions
button_rect = pygame.Rect((screen.get_width() / 2 - 70, screen.get_height() / 2 - 20, 140, 40))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Check if mouse button is clicked
        if event.type == pygame.MOUSEBUTTONDOWN and button_rect.collidepoint(event.pos):
            pygame.quit()
            sys.exit()

    # Fill the screen with color
    screen.fill((60, 25, 60))

    # Change button color on hover
    if button_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen, color_light, button_rect)
    else:
        pygame.draw.rect(screen, color_dark, button_rect)

    # Draw the text on the button
    text_rect = text.get_rect(center=button_rect.center)
    screen.blit(text, text_rect)

    # Update the display
    pygame.display.update()
