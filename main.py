import cv2 
import mediapipe as mp
import pygame
import sys
import random
from pygame.locals import *

cam = cv2.VideoCapture(0)
frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

THRESHOLD = 50
prev_x, prev_y = 0, 0
timer = 0
COOLDOWN_FRAMES = 3
BackG = (0, 0, 0)
SnakeHead = (51, 97, 56)
Fruit = (181, 27, 40)
BlockSize = 30
pygame.init()
start_font = pygame.font.SysFont(None, 70)
score_font = pygame.font.SysFont(None, 40)
screen = pygame.display.set_mode((1000, 700))
running = True
start_x = 333
start_y = 350
snake_body = [pygame.Rect(start_x, start_y, BlockSize, BlockSize), pygame.Rect(start_x - BlockSize,start_y, BlockSize, BlockSize), pygame.Rect(start_x - (2*BlockSize),start_y, BlockSize, BlockSize)]
fruit = pygame.Rect(666, 350, BlockSize, BlockSize)
onlybody = snake_body[1:]
direction = 'RIGHT'
snake_speed = BlockSize
FPS = 20
clock = pygame.time.Clock()
game_speed_counter = 0
GAME_SPEED_INTERVAL = 3
game_started = False
score = 0
try:
    with open("highscore.txt", "r") as f:
        high_score = int(f.read())
except (FileNotFoundError, ValueError):
    high_score = 0

while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_started = True
    ret, frame = cam.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)
    rgbframe = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgbframe)
    if game_started:
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                index_finger = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                h, w, c = frame.shape
                cx, cy = int(index_finger.x*w), int(index_finger.y*h)
                dx = cx - prev_x
                dy = cy - prev_y
                
                if(timer == 0):
                    if dx > THRESHOLD and direction != 'LEFT':
                        direction = 'RIGHT'
                        timer = COOLDOWN_FRAMES
                    elif dx < -THRESHOLD and direction != 'RIGHT':
                        direction = 'LEFT'
                        timer = COOLDOWN_FRAMES
                    elif dy > THRESHOLD and direction != 'UP':
                        direction = 'DOWN'
                        timer = COOLDOWN_FRAMES
                    elif dy < -THRESHOLD and direction != 'DOWN':
                        direction = 'UP'
                        timer = COOLDOWN_FRAMES                    
            prev_x, prev_y = cx, cy

        if timer > 0:
            timer -=1
        
        game_speed_counter += 1
        if game_speed_counter % GAME_SPEED_INTERVAL == 0:
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
                score += 1
                if score > high_score:
                    high_score = score
            else:
                snake_body.pop()
            
            if(snake_body[0].left < 0 or snake_body[0].right > 1000 or snake_body[0].top < 0 or snake_body[0].bottom > 700):
                running = False
            for block in snake_body[1:]:
                if snake_body[0].colliderect(block):
                    running = False
                    break

    screen.fill(BackG)
    if game_started:
        score_text = f"Score: {score} High Score: {high_score}"
        score_surface = score_font.render(score_text, True, (255, 255, 255))
        screen.blit(score_surface, (10, 10))
        for block in snake_body:
            pygame.draw.rect(screen, SnakeHead, block)
        pygame.draw.rect(screen, Fruit, fruit)
    else:
        text_surface = start_font.render("Press Space to Start", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(1000//2, 700//2))
        screen.blit(text_surface, text_rect)
    pygame.display.flip()
    clock.tick(FPS)
    cv2.imshow('Camera', frame)

with open("highscore.txt", "w") as f:
    f.write(str(high_score))
cam.release()
cv2.destroyAllWindows()
pygame.quit()
sys.exit()