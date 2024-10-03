import pygame as pg
import sys
import time

XO, winner, draw = 'x', None, None
width, height = 400, 400
white, line_color = (255, 255, 255), (0, 0, 0)
board = [[None]*3 for _ in range(3)]

pg.init()
CLOCK = pg.time.Clock()
screen = pg.display.set_mode((width, height + 100))
pg.display.set_caption("My Tic Tac Toe")

initiating_window = pg.transform.scale(pg.image.load("modified_cover.jpg"), (width, height + 100))
x_img = pg.transform.scale(pg.image.load("x_modified.png"), (80, 80))
o_img = pg.transform.scale(pg.image.load("o_modified.png"), (80, 80))

def game_initiating_window():
    screen.blit(initiating_window, (0, 0))
    pg.display.update()
    time.sleep(2)
    screen.fill(white)
    for i in range(1, 3):
        pg.draw.line(screen, line_color, (width / 3 * i, 0), (width / 3 * i, height), 7)
        pg.draw.line(screen, line_color, (0, height / 3 * i), (width, height / 3 * i), 7)
    draw_status()

def draw_status():
    global draw
    message = (winner.upper() + " won !" if winner else XO.upper() + "'s Turn")
    if draw: message = "Game Draw !"
    font = pg.font.Font(None, 30)
    text = font.render(message, 1, (255, 255, 255))
    screen.fill((0, 0, 0), (0, 400, 500, 100))
    screen.blit(text, text.get_rect(center=(width / 2, 500 - 50)))
    pg.display.update()

def check_win():
    global winner, draw
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0]:
            winner = board[row][0]
            pg.draw.line(screen, (250, 0, 0), (0, (row + 1) * height / 3 - height / 6), (width, (row + 1) * height / 3 - height / 6), 4)
            break
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col]:
            winner = board[0][col]
            pg.draw.line(screen, (250, 0, 0), ((col + 1) * width / 3 - width / 6, 0), ((col + 1) * width / 3 - width / 6, height), 4)
            break
    if board[0][0] == board[1][1] == board[2][2] and board[0][0]:
        winner = board[0][0]
        pg.draw.line(screen, (250, 70, 70), (50, 50), (350, 350), 4)
    if board[0][2] == board[1][1] == board[2][0] and board[0][2]:
        winner = board[0][2]
        pg.draw.line(screen, (250, 70, 70), (350, 50), (50, 350), 4)
    if all(all(row) for row in board) and winner is None:
        draw = True
    draw_status()

def drawXO(row, col):
    global board, XO
    posx, posy = 30 + (row - 1) * (width // 3), 30 + (col - 1) * (height // 3)
    board[row - 1][col - 1] = XO
    screen.blit(x_img if XO == 'x' else o_img, (posy, posx))
    XO = 'o' if XO == 'x' else 'x'
    pg.display.update()

def user_click():
    x, y = pg.mouse.get_pos()
    col, row = (1 + x // (width // 3), 1 + y // (height // 3)) if x < width and y < height else (None, None)
    if row and col and board[row - 1][col - 1] is None:
        drawXO(row, col)
        check_win()

def reset_game():
    global board, winner, XO, draw
    time.sleep(3)
    XO, draw, winner = 'x', False, None
    board = [[None]*3 for _ in range(3)]
    game_initiating_window()

game_initiating_window()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            user_click()
            if winner or draw:
                reset_game()
    pg.display.update()
    CLOCK.tick(30)
