import pygame
import random
import math

pygame.init()
screen = pygame.display.set_mode((1600, 800))
clock = pygame.time.Clock()
running = True
dt = 0

class Snake():
    def __init__(self):
        player_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)
        self.body = [player_pos]
        self.headPos = self.body[0]
    
    def move():
        pass

class Food():
    def __init__(self):
        self.pos = pygame.Vector2(random.randrange(20, screen.get_width()-20, 40), random.randrange(20, screen.get_height()-20, 40))

snake = Snake()
curDir = "right"
prevDir = "up"
food = Food()

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    #Movement
    if curDir == "right":
        snake.body.pop()
        snake.body.insert(0, pygame.Vector2(snake.headPos.x + 40, snake.headPos.y))
        snake.headPos = snake.body[0]
    if curDir == "up":
        snake.body.pop()
        snake.body.insert(0, pygame.Vector2(snake.headPos.x, snake.headPos.y - 40))
        snake.headPos = snake.body[0]
    if curDir == "left":
        snake.body.pop()
        snake.body.insert(0, pygame.Vector2(snake.headPos.x - 40, snake.headPos.y))
        snake.headPos = snake.body[0]
    if curDir == "down":
        snake.body.pop()
        snake.body.insert(0, pygame.Vector2(snake.headPos.x, snake.headPos.y + 40))
        snake.headPos = snake.body[0]

    #Check Food Collision
    if math.sqrt((food.pos.x - snake.headPos.x)**2 + (food.pos.y - snake.headPos.y)**2) < 40:
        food.pos = pygame.Vector2(random.randrange(40, screen.get_width()-40, 40), random.randrange(40, screen.get_height()-40, 40))
        tempBit = snake.body[-1]
        snake.body.append(tempBit)

    #Check Self Collision
    if len(snake.body) > 4:
        for i in range(4, len(snake.body)):
            if math.sqrt((snake.body[i].x - snake.headPos.x)**2 + (snake.body[i].y - snake.headPos.y)**2) < 40:
                running = False

    #Check Wall Collision
    if snake.headPos.x < 40 or snake.headPos.x > screen.get_width()-40 or snake.headPos.y < 40 or snake.headPos.y > screen.get_height()-40:
        running = False

    #Rendering Snake
    for i in range(len(snake.body)):
        pygame.draw.circle(screen, "green", snake.body[i], 20)

    #Rendering Food
    pygame.draw.circle(screen, "red", food.pos, 20)

    #Key Presses
    key = pygame.key.get_pressed()
    if key[pygame.K_d]:
        prevDir = curDir
        curDir = "right"
    elif key[pygame.K_w]:
        prevDir = curDir
        curDir = "up"
    elif key[pygame.K_a]:
        prevDir = curDir
        curDir = "left"
    elif key[pygame.K_s]:
        prevDir = curDir
        curDir = "down"

    pygame.display.flip()

    clock.tick(30)
    dt = clock.tick(30) / 1000

pygame.quit()