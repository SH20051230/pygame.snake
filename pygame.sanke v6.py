import pygame
import time
import random
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
yellow = (255, 255, 0)

# fonts used
score_font = pygame.font.SysFont("arialblack", 20)
exit_font = pygame.font.Font("freesansbold.ttf", 30)
msg_font = pygame.font.SysFont("arialblack", 20)

def message(msg, txt_colour, bkgd_colour):
    txt = msg_font.render(msg, True, txt_colour, bkgd_colour)

    # centre of rectangle : 1000/2 500 600/2 300
    text_box = txt.get_rect(center=(500, 300))
    screen.blit(txt, text_box)


# snake will be 20 x 20 pixcle
snake_x = 490
snake_y = 290

snake_x_change = 0
snake_y_change = 0

# set the random position which the food will appear
food_x = round(random.randrange(20, 1000-20)/20)*20
food_y = round(random.randrange(20, 600-20)/20)*20

clock = pygame.time.Clock()   #Sets the speed of the snake moving
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

    # create the sanke
    pygame.draw.rect(screen, red, [snake_x, snake_y, 20, 20])
    pygame.display.update()

    # create the circle
    pygame.draw.circle(screen, yellow, [food_x, food_y], 10)
    pygame.display.update()

    # collision detection (test if the snake touches the food)
    if snake_x == food_x - 10 and snake_y == food_y - 10:
        # Set a new position for the food to occur again
        food_x = round(random.randrange(20, 1000-20)/20)*20
        food_y = round(random.randrange(20, 600-20)/20)*20

    clock.tick(5)  # set the speed which the snake is moving at which iteration of the game loop
    # Runs in frames per second 5fps
message("you died!", black, white)
pygame.display.update()
time.sleep(3)
pygame.quit()
quit()
