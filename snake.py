# Импорт нужных модулей
import pygame, pygame.display
import time
import random

# Инициализация
pygame.init()

# Создаем экран
screen_width = 1080
screen_height = 720
screen = pygame.display.set_mode([screen_width, screen_height])

# Параметры змейки
snake_pos_x = screen_width // 2
snake_pos_y = screen_height // 2
snake_size = 20

# Параметры яблока
apple_pos_x = round(random.randrange(10, screen_width-10), -1)
apple_pos_y = round(random.randrange(10, screen_height-10), -1)
apple_size = 10

direction = None

# Игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Функционал при нажатии на клавиши
        elif event.type == pygame.KEYDOWN:
            # Движение змейки
            if event.key == pygame.K_UP:
                direction = 'up'
            elif event.key == pygame.K_DOWN:
                direction = 'down'
            elif event.key == pygame.K_LEFT:
                direction = 'left'
            elif event.key == pygame.K_RIGHT:
                direction = 'right'
                
    # Координаты углов змейки и яблока
    snake_rect = pygame.Rect(snake_pos_x - snake_size, snake_pos_y - snake_size, 2 * snake_size, 2 * snake_size)
    apple_rect = pygame.Rect(apple_pos_x - apple_size, apple_pos_y - apple_size, 2 * apple_size, 2 * apple_size)

    # При пересечения яблока и змейки
    if snake_rect.colliderect(apple_rect):
        apple_pos_x = round(random.randrange(10, screen_width-10), -1)
        apple_pos_y = round(random.randrange(10, screen_height-10), -1)

        snake_size += 5

    # Покрывает все черным, чтобы перерисовать все 
    screen.fill((0, 0, 0))  

    if direction == 'up':
        snake_pos_y -= 10
        time.sleep(.05)
    elif direction == 'down':
        snake_pos_y += 10
        time.sleep(.05)
    elif direction == 'left':
        snake_pos_x -= 10
        time.sleep(.05)
    elif direction == 'right':
        snake_pos_x += 10
        time.sleep(.05)


    # Рисуется змейка и яблоко
    pygame.draw.circle(screen, (224, 176, 255), (snake_pos_x, snake_pos_y), snake_size)
    pygame.draw.circle(screen, (255, 0, 0), (apple_pos_x, apple_pos_y), apple_size)

    pygame.display.flip()

pygame.quit()