import pygame, random

pygame.init()

WIDTH, HEIGHT = 800, 600
WHITE, GREEN = (255, 255, 255), (0, 255, 0)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock, FPS = pygame.time.Clock(), 30
font = pygame.font.Font('freesansbold.ttf', 20)

balloonPath, archerPath, arrowPath = "balloon.png", "archer.png", "arrow.png"

class Archer:
    def __init__(self, width, height, speed):
        self.archer = pygame.transform.scale(pygame.image.load(archerPath), (width, height))
        self.archerRect = self.archer.get_rect(x=100, y=HEIGHT//2)
        self.speed = speed

    def display(self): screen.blit(self.archer, self.archerRect)
    def update(self, xFac, yFac):
        self.archerRect.move_ip(xFac * self.speed, yFac * self.speed)
        self.archerRect.clamp_ip(pygame.Rect(0, 0, WIDTH//2, HEIGHT))

class Balloon:
    def __init__(self, posx, posy, width, height, speed):
        self.balloon = pygame.transform.scale(pygame.image.load(balloonPath), (width, height))
        self.balloonRect = self.balloon.get_rect(x=posx, y=posy)
        self.speed = speed

    def display(self): screen.blit(self.balloon, self.balloonRect)
    def update(self):
        self.balloonRect.y -= self.speed
        if self.balloonRect.y < 0: self.balloonRect.y = HEIGHT + 10

class Arrow:
    def __init__(self, posx, posy, width, height, speed):
        self.arrow = pygame.transform.scale(pygame.image.load(arrowPath), (width, height))
        self.arrowRect = self.arrow.get_rect(x=posx, y=posy)
        self.speed, self.hit = speed, 0

    def display(self): screen.blit(self.arrow, self.arrowRect)
    def update(self): self.arrowRect.x += self.speed
    def updateHit(self): self.hit = 1

def populateBalloons(count, width=30, height=40, speed=5):
    return [Balloon(random.randint(WIDTH//2, WIDTH-width), random.randint(0, HEIGHT), width, height, speed) for _ in range(count)]

def gameOver():
    while True:
        screen.blit(font.render("GAME OVER", True, WHITE), (WIDTH//2-100, HEIGHT//2-100))
        screen.blit(font.render("R - Replay  Q - Quit", True, WHITE), (WIDTH//2-100, HEIGHT//2-50))
        for event in pygame.event.get():
            if event.type == pygame.QUIT: return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r: return True
                if event.key == pygame.K_q: return False
        pygame.display.update()

def main():
    score, lives, running = 0, 5, True
    archer, xFac, yFac = Archer(60, 60, 7), 0, 0
    balloons, arrows = populateBalloons(10), []

    while running:
        screen.fill(GREEN)
        for i in range(lives):
            screen.blit(pygame.transform.rotate(pygame.transform.scale(pygame.image.load(arrowPath), (20, 30)), 45), (i*30, 10))
        screen.blit(font.render(f"Score: {score}", True, WHITE), (10, HEIGHT-50))

        if lives <= 0: 
            running = gameOver()
            score, lives, balloons, arrows = 0, 5, populateBalloons(10), []

        for balloon in balloons:
            balloon.update()
            balloon.display()

        for arrow in arrows:
            arrow.update()
            arrow.display()

        archer.display()
        archer.update(xFac, yFac)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r: balloons, score = populateBalloons(10), 0
                if event.key == pygame.K_RIGHT: xFac = 1
                if event.key == pygame.K_LEFT: xFac = -1
                if event.key == pygame.K_DOWN: yFac = 1
                if event.key == pygame.K_UP: yFac = -1
                if event.key == pygame.K_SPACE:
                    arrows.append(Arrow(archer.archerRect.x, archer.archerRect.y + archer.archerRect.h//2 - 15, 60, 30, 10))
            if event.type == pygame.KEYUP:
                if event.key in [pygame.K_RIGHT, pygame.K_LEFT]: xFac = 0
                if event.key in [pygame.K_DOWN, pygame.K_UP]: yFac = 0

        for arrow in arrows[:]:
            if any(pygame.Rect.colliderect(arrow.arrowRect, balloon.balloonRect) for balloon in balloons):
                arrow.updateHit()
                balloons = [balloon for balloon in balloons if not pygame.Rect.colliderect(arrow.arrowRect, balloon.balloonRect)]
                score += 1
            if arrow.arrowRect.x > WIDTH:
                if not arrow.hit: lives -= 1
                arrows.remove(arrow)

        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
    pygame.quit()
