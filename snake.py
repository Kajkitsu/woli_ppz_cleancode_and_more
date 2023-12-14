import pygame
import time
import random

pygame.init()

# Ustawienia gry
width, height = 600, 400
# Inicjalizacja okna gry
game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Inicjalizacja zegara
clock = pygame.time.Clock()

# Główna funkcja gry
def game_loop():
    game_over = False
    game_close = False

    # Początkowe położenie głowy węża
    lead_x = width / 2
    lead_y = height / 2

    # Początkowa zmiana położenia głowy węża
    lead_x_change = 0
    lead_y_change = 0

    snake_list = []
    snake_length = 1

    # Początkowe położenie jedzenia
    food_x = round(random.randrange(0, width - 20) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - 20) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            game_display.fill((0, 0, 0))
            font = pygame.font.SysFont(None, 25)
            screen_text = font.render("Przegrałeś! Naciśnij C-Nowa gra lub Q-Wyjście", True, (255, 0, 0))
            game_display.blit(screen_text, [width / 4, height / 2 + -50])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -20
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = 20
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -20
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = 20
                    lead_x_change = 0

        if lead_x >= width or lead_x < 0 or lead_y >= height or lead_y < 0:
            game_close = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        game_display.fill((0, 0, 0))
        pygame.draw.rect(game_display, (255, 0, 0), [food_x, food_y, 20, 20])

        snake_head = []
        snake_head.append(lead_x)
        snake_head.append(lead_y)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        for segment in snake_list:
            pygame.draw.rect(game_display, (255, 255, 255), [segment[0], segment[1], 20, 20])

        pygame.display.update()

        if any(food_x + i == lead_x for i in range(-20, 20)) and any(food_y + i == lead_y for i in range(-20, 20)):
            food_x = round(random.randrange(0, width - 20) / 10.0) * 10.0
            food_y = round(random.randrange(0, height - 20) / 10.0) * 10.0
            snake_length += 1

        clock.tick(15)

    pygame.quit()
    quit()


game_loop()
