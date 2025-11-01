import pygame
import sys
import random
from pygame.locals import *
BackG = (0, 0, 0)
SnakeHead = (51, 97, 56)
Fruit = (181, 27, 40)
BlockSize = 30
pygame.init()
screen = pygame.display.set_mode((1000, 700))
running = True
snake_body = [pygame.Rect(333, 350, BlockSize, BlockSize), pygame.Rect(303,350, BlockSize, BlockSize), pygame.Rect(273,350, BlockSize, BlockSize)]
fruit = pygame.Rect(666, 350, BlockSize, BlockSize)
onlybody = snake_body[1:]
direction = 'RIGHT'
snake_speed = BlockSize
FPS = 10
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_UP or event.key == pygame.K_w) and direction !='DOWN':
                direction = 'UP'
            elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and direction !='UP':
                direction = 'DOWN'
            elif (event.key == pygame.K_LEFT or event.key == pygame.K_a) and direction !='RIGHT':
                direction = 'LEFT'
            elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and direction !='LEFT':
                direction = 'RIGHT'
    new_head = snake_body[0].copy()
    if direction == 'UP':
        new_head.y -= snake_speed
    elif direction == 'DOWN':
        new_head.y += snake_speed
    elif direction == 'LEFT':
        new_head.x -= snake_speed
    elif direction == 'RIGHT':
        new_head.x += snake_speed
    snake_body.insert(0, new_head)
    if snake_body[0].colliderect(fruit):
        fruit.x = random.randrange(30, 970, BlockSize)
        fruit.y = random.randrange(30, 670, BlockSize)
    else:
        snake_body.pop()
    screen.fill(BackG)
    for block in snake_body:
        pygame.draw.rect(screen, SnakeHead, block)
    pygame.draw.rect(screen, Fruit, fruit)
    if(snake_body[0].left < 0 or snake_body[0].right > 1000 or snake_body[0].top < 0 or snake_body[0].bottom > 700):
        running = False
    for block in snake_body[1:]:
        if snake_body[0].colliderect(block):
            running = False
            break
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
sys.exit()
