import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Custom Events')
timer = pygame.time.Clock()

WHITE, GREEN, RED = (255, 255, 255), (0, 255, 0), (255, 0, 0)
bg_color = WHITE
screen.fill(WHITE)

CHANGE_COLOR, ON_BOX = pygame.USEREVENT + 1, pygame.USEREVENT + 2
box = pygame.Rect((225, 225, 50, 50))
grow = True
pygame.time.set_timer(CHANGE_COLOR, 500)

running = True
while running:
    for event in pygame.event.get():
        if event.type == CHANGE_COLOR:
            bg_color = WHITE if bg_color == GREEN else GREEN
            screen.fill(bg_color)
        
        if event.type == ON_BOX:
            box.inflate_ip(3 if grow else -3, 3 if grow else -3)
            grow = box.width < (75 if grow else 50)

        if event.type == pygame.QUIT:
            running = False

    if box.collidepoint(pygame.mouse.get_pos()):
        pygame.event.post(pygame.event.Event(ON_BOX))

    pygame.draw.rect(screen, RED, box)
    pygame.display.update()
    timer.tick(30)

pygame.quit()
