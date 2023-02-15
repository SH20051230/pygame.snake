import pygame
import time
pygame.init()

screen = pygame.display.set_mode((1000, 600))
game_icon = pygame.image.load("snake_icon.png")
pygame.display.set_icon(game_icon)
pygame.display.set_caption("snake game - by Steven")
# Colours will be used in games
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (188, 227, 199)

# fonts used
score_font = pygame.font.SysFont("arialblack", 20)
exit_font = pygame.font.Font("freesansbold.ttf", 30)

# snake will be 20 x 20 pixcle
snake_x = 490
snake_y = 290

snake_x_change = 0
snake_y_change = 0

clock = pygame.time.Clock()  #Sets the speed of the snake moving
quit_game = False
while not quit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_x_change = -20
                snake_y_change = 0
            elif event.key == pygame.K_RIGHT:
                snake_x_change = 20
                snake_y_change = 0
            elif event.key == pygame.K_UP:
                snake_x_change = 0
                snake_y_change = -20
            elif event.key == pygame.K_DOWN:
                snake_x_change = 0
                snake_y_change = 20
    if snake_x >= 1000 or snake_x < 0 or snake_y >= 600 or snake_y < 0:
        quit_game = True

    snake_y += snake_y_change
    snake_x += snake_x_change

    screen.fill(green)  # Changes screen to green


    pygame.draw.rect(screen, red, [snake_x, snake_y, 20, 20])
    pygame.display.update()
    clock.tick(5)  # set the speed which the snake is moving at which iteration of the game loop
    # Runs in frames per second 5fps
pygame.quit()
quit()
