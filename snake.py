import pygame 
import pygame
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
snake_speed = 10

# Параметры яблока
apple_pos_x = round(random.randrange(10, screen_width-10), -1)
apple_pos_y = round(random.randrange(10, screen_height-10), -1)
apple_size = 10

btn_pos_x = screen_width // 2 - 60  
btn_pos_y = screen_height // 2 + 100
btn_width = 120
btn_height = 30

font = pygame.font.Font(None, 36)
end_game_text = font.render('Game Over', 1, (255, 0, 0))
restart_btn = font.render('Restart', 1, (255, 0, 0))
restart_rect = restart_btn.get_rect(center=(screen_width // 2 - 36, screen_height // 2 + 36))
 
direction = None

# Игровой циклs
running = True
game_in_progress = True

def game_end():
    print("end")
    global game_in_progress
    global snake_pos_x
    global snake_pos_y
    global snake_size
    global snake_speed
    global direction

    game_in_progress = False
    screen.fill((0, 0, 0))  
    screen.blit(end_game_text, (screen_width // 2 - 90, screen_height // 2 - 36))
    screen.blit(restart_btn, restart_rect)

    snake_pos_x = screen_width // 2
    snake_pos_y = screen_height // 2
    snake_size = 20
    snake_speed = 10
    direction = None

    pygame.display.flip()

def game_restart():
    print("restart")
    global game_in_progress

    game_in_progress = True

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

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()

            if restart_rect.collidepoint(event.pos):
                game_restart()

            if restart_rect.collidepoint(x, y):
                game_in_progress = True

    if game_in_progress:
        # Рисуется змейка и яблоко
        pygame.draw.circle(screen, (224, 176, 255), (snake_pos_x, snake_pos_y), snake_size)
        pygame.draw.circle(screen, (255, 0, 0), (apple_pos_x, apple_pos_y), apple_size)
        pygame.display.flip()

        # Координаты углов змейки и яблока
        snake_rect = pygame.Rect(snake_pos_x - snake_size, snake_pos_y - snake_size, 2 * snake_size, 2 * snake_size)
        apple_rect = pygame.Rect(apple_pos_x - apple_size, apple_pos_y - apple_size, 2 * apple_size, 2 * apple_size)

        # При пересечения яблока и змейки
        if snake_rect.colliderect(apple_rect):
            apple_pos_x = round(random.randrange(10, screen_width-10), -1)
            apple_pos_y = round(random.randrange(10, screen_height-10), -1)

            snake_size += 10
            snake_speed += 5

        # Покрывает все черным, чтобы перерисовать все 
        screen.fill((0, 0, 0))  

        if direction == 'up':
            snake_pos_y -= snake_speed
            time.sleep(.05)
        elif direction == 'down':
            snake_pos_y += snake_speed
            time.sleep(.05)
        elif direction == 'left':
            snake_pos_x -= snake_speed
            time.sleep(.05)
        elif direction == 'right':
            snake_pos_x += snake_speed
            time.sleep(.05)

        #  Игра заканчивается 
        if snake_pos_x - snake_size / 2 < 0 or snake_pos_x + snake_size / 2 > screen_width or snake_pos_y - snake_size / 2 < 0 or snake_pos_y + snake_size / 2 > screen_height:
            game_end()

pygame.quit