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
quit_game = False
while not quit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True

    pygame.draw.rect(screen, red, [snake_x, snake_y, 20, 20])
    pygame.display.update()
pygame.quit()
quit()
