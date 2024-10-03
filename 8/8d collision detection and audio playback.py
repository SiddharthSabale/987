import pygame as pg
import sys

pg.init()
screen = pg.display.set_mode((800, 600))
pg.display.set_caption("Collision Detection and Audio Example")

pg.mixer.init()
collision_sound = pg.mixer.Sound("npc_pain.mp3")

WHITE, RED, BLUE = (255, 255, 255), (255, 0, 0), (0, 0, 255)
circle_radius, circle_color = 30, BLUE

def draw_circle(pos): pg.draw.circle(screen, circle_color, pos, circle_radius)
def play_collision_sound(): collision_sound.play()
def check_collision(circle_pos, rect): 
    return (rect[0] <= circle_pos[0] <= rect[0] + rect[2] and 
            rect[1] <= circle_pos[1] <= rect[1] + rect[3])

running = True
while running:
    screen.fill(WHITE)
    pg.draw.rect(screen, RED, (350, 250, 100, 100))
    
    mouse_pos = pg.mouse.get_pos()
    draw_circle(mouse_pos)

    if check_collision(mouse_pos, (350, 250, 100, 100)):
        play_collision_sound()

    for event in pg.event.get():
        if event.type == pg.QUIT: running = False

    pg.display.flip()

pg.quit()
sys.exit()
