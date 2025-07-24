import pygame
import random

WIDTH, HEIGHT = 600, 600
LANE_HEIGHT = 60
PLAYER_SIZE = 40
CAR_WIDTH, CAR_HEIGHT = 60, 40

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 36)

def draw_text(text, pos):
    img = font.render(text, True, (0,0,0))
    screen.blit(img, pos)

class Car:
    def __init__(self, lane, direction):
        self.lane = lane
        self.direction = direction
        if direction == 1:
            self.rect = pygame.Rect(-CAR_WIDTH, lane*LANE_HEIGHT+10, CAR_WIDTH, CAR_HEIGHT)
            self.speed = random.randint(3,6)
        else:
            self.rect = pygame.Rect(WIDTH, lane*LANE_HEIGHT+10, CAR_WIDTH, CAR_HEIGHT)
            self.speed = -random.randint(3,6)
    def update(self):
        self.rect.x += self.speed
    def draw(self):
        pygame.draw.rect(screen, (255,0,0), self.rect)

class Player:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH//2 - PLAYER_SIZE//2, HEIGHT - LANE_HEIGHT//2 - PLAYER_SIZE//2, PLAYER_SIZE, PLAYER_SIZE)
    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        self.rect.x = max(0, min(WIDTH - PLAYER_SIZE, self.rect.x))
        self.rect.y = max(0, min(HEIGHT - PLAYER_SIZE, self.rect.y))
    def draw(self):
        pygame.draw.rect(screen, (0,255,0), self.rect)

cars = []
player = Player()
score = 0

running = True
spawn_timer = 0

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move(-5,0)
    if keys[pygame.K_RIGHT]:
        player.move(5,0)
    if keys[pygame.K_UP]:
        player.move(0,-5)
    if keys[pygame.K_DOWN]:
        player.move(0,5)

    spawn_timer += 1
    if spawn_timer > 30:
        lane = random.randint(0, (HEIGHT//LANE_HEIGHT)-2)
        direction = random.choice([-1,1])
        cars.append(Car(lane, direction))
        spawn_timer = 0

    screen.fill((135,206,250))

    for i in range(HEIGHT//LANE_HEIGHT):
        pygame.draw.line(screen, (200,200,200), (0, i*LANE_HEIGHT), (WIDTH, i*LANE_HEIGHT))

    for car in list(cars):
        car.update()
        car.draw()
        if car.rect.right < 0 or car.rect.left > WIDTH:
            cars.remove(car)
        if car.rect.colliderect(player.rect):
            running = False

    if player.rect.top < 0:
        score += 1
        player = Player()
        cars.clear()

    player.draw()
    draw_text(f"Score: {score}", (10,10))
    pygame.display.flip()

pygame.quit()
