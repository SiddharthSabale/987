import pygame
import sys
import time
import random

pygame.init()
width, height = 720, 480
colors = {"black": (0, 0, 0), "white": (255, 255, 255), "red": (255, 0, 0), "green": (0, 255, 0)}
snake_speed, score = 15, 0
snake_pos, snake_body = [100, 50], [[100, 50], [90, 50], [80, 50], [70, 50]]
fruit_pos = [random.randrange(1, (width // 10)) * 10, random.randrange(1, (height // 10)) * 10]
direction = 'RIGHT'

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Siddharth')
fps = pygame.time.Clock()

def show_score(): 
    font = pygame.font.SysFont('times new roman', 20)
    score_surface = font.render(f'Score: {score}', True, colors["white"])
    screen.blit(score_surface, (10, 10))

def game_over(): 
    font = pygame.font.SysFont('times new roman', 50)
    over_surface = font.render(f'Your Score: {score}', True, colors["red"])
    screen.blit(over_surface, (width / 2 - 100, height / 4))
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    sys.exit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit(); sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN': direction = 'UP'
            if event.key == pygame.K_DOWN and direction != 'UP': direction = 'DOWN'
            if event.key == pygame.K_LEFT and direction != 'RIGHT': direction = 'LEFT'
            if event.key == pygame.K_RIGHT and direction != 'LEFT': direction = 'RIGHT'

    snake_pos[1] += (direction == 'DOWN') * 10 - (direction == 'UP') * 10
    snake_pos[0] += (direction == 'RIGHT') * 10 - (direction == 'LEFT') * 10
    snake_body.insert(0, list(snake_pos))
    
    if snake_pos == fruit_pos:
        score += 10
        fruit_pos = [random.randrange(1, (width // 10)) * 10, random.randrange(1, (height // 10)) * 10]
    else:
        snake_body.pop()

    screen.fill(colors["black"])
    for pos in snake_body: pygame.draw.rect(screen, colors["green"], pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(screen, colors["white"], pygame.Rect(fruit_pos[0], fruit_pos[1], 10, 10))
    
    if (snake_pos[0] < 0 or snake_pos[0] > width - 10 or 
        snake_pos[1] < 0 or snake_pos[1] > height - 10 or 
        snake_pos in snake_body[1:]): game_over()

    show_score()
    pygame.display.update()
    fps.tick(snake_speed)
