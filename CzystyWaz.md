# Czysty wąż

```python
import pygame
import random


def main():
    pygame.init()
    screen_width = 600
    screen_height = 400
    screen = pygame.display.set_mode((screen_width, screen_height))
    running = True

    # Stan gry
    snake_body = [(0, 0)]
    snake_direction = "right"
    apple_x = random.randint(0, screen_width - 1)
    apple_y = random.randint(0, screen_height - 1)

    while running:
        # Obsługa zdarzeń
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    snake_direction = "right"
                elif event.key == pygame.K_LEFT:
                    snake_direction = "left"
                elif event.key == pygame.K_UP:
                    snake_direction = "up"
                elif event.key == pygame.K_DOWN:
                    snake_direction = "down"

        # Ruch węża
        head = snake_body[0]
        if snake_direction == "right":
            head[0] += 1
        elif snake_direction == "left":
            head[0] -= 1
        elif snake_direction == "up":
            head[1] -= 1
        elif snake_direction == "down":
            head[1] += 1
        snake_body.insert(0, head)
        if len(snake_body) > screen_width * screen_height:
            snake_body.pop()

        # Sprawdzenie kolizji
        if snake_body[0] == (apple_x, apple_y):
            snake_body.append((apple_x, apple_y))
            apple_x = random.randint(0, screen_width - 1)
            apple_y = random.randint(0, screen_height - 1)

        # Rysowanie
        screen.fill((0, 0, 0))
        for part in snake_body:
            pygame.draw.rect(screen, (255, 0, 0), part)
        pygame.draw.rect(screen, (0, 255, 0), (apple_x, apple_y, 10, 10))
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
```