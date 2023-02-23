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
score_font = pygame.font.Font("snake_chan.zip", 20)
exit_font = pygame.font.Font("freesansbold.ttf", 30)
msg_font = pygame.font.SysFont("arialblack", 20)

clock = pygame.time.Clock()   #Sets the speed of the snake moving


def player_score(score, score_colour):
    display_score = score_font.render(f"Score: {score}", True, score_colour)
    screen.blit(display_score, (800, 20))  # cordinates for top right


def draw_sanke(snake_list):
    print(f"Sanke lists: {snake_list}")  # for testing purposes
    for i in snake_list:
        pygame.draw.rect(screen, red, [i[0], i[1], 20, 20])


def message(msg, txt_colour, bkgd_colour):
    txt = msg_font.render(msg, True, txt_colour, bkgd_colour)

    # centre of rectangle : 1000/2 500 600/2 300
    text_box = txt.get_rect(center=(500, 300))
    screen.blit(txt, text_box)


def main_game_loop():
    quit_game = False
    game_over = False



    # snake will be 20 x 20 pixcle
    snake_x = 480
    snake_y = 280

    snake_x_change = 0
    snake_y_change = 0
    snake_list = []
    snake_length = 1

    # set the random position which the food will appear
    food_x = round(random.randrange(20, 1000-20)/20)*20
    food_y = round(random.randrange(20, 600-20)/20)*20


    quit_game = False
    while not quit_game:
        # Give the user the choice to quit or play the game again when they die
        while game_over:
            screen.fill(white)
            message("you died! Press Q to quit or Press A to play again", black, white)
            pygame.display.update()

            # Check if user wants to quit (Q) or play gain (A)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        quit_game = True
                        game_over = False
                    if event.key == pygame.K_a:
                        main_game_loop()  # Restart the game loop if they want to replay

        # Original set up for arrow keys to move the snake
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                instructions = "Exit: X to quit, Space to resume or R to restart"
                message(instructions, white, black)
                pygame.display.update()

                end = False
                while not end:
                    for event in pygame.event.get():
                        # If the user press X button the game quits
                        if event.type == pygame.QUIT:
                            quit_game = True
                            end = True
                            # If user press R the game loop restart
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_r:
                                    end = True, main_game_loop()
                            # If the user press space the game will continue
                            if event.key == pygame.K_SPACE:
                                end = True
                            # If the user press Q the game quits
                            if event.key == pygame.K_q:
                                quit_game = True
                                end = True
                            


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
            game_over = True

        snake_y += snake_y_change
        snake_x += snake_x_change

        screen.fill(green)  # Changes screen to green

        # create the snake(replaces simple rectangle with previous version
        snake_head = [snake_x, snake_y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_over = True

        draw_sanke(snake_list)

        # Keeping track of the player score
        score = snake_length - 1  # Score exludes the snake head
        player_score(score, black)



        # Using a sprite (instead of circle as previously)
        food = pygame.Rect(food_x, food_y, 20, 20)
        apple = pygame.image.load("apple_3.png").convert_alpha()
        resized_apple = pygame.transform.smoothscale(apple, [20, 20])
        screen.blit(resized_apple, food)
        pygame.display.update()

        # Print line are for testing
        print(f"Snake x: {snake_x}")
        print(f"Food x : {food_x}")
        print(f"Snake Y: {snake_y}")
        print(f"Food y: {food_y}")
        print("\n\n")

        # collision detection (test if the snake touches the food)
        if snake_x == food_x and snake_y == food_y:
            # Set a new position for the food to occur again
            food_x = round(random.randrange(20, 1000-20)/20)*20
            food_y = round(random.randrange(20, 600-20)/20)*20
            # For testing purposes
            print("got it!")
            # Increase the length of the snake whenever it touches the food
            snake_length += 1

        clock.tick(5)  # set the speed which the snake is moving at which iteration of the game loop
        # Runs in frames per second 5fps
    pygame.quit()
    quit()

# Main routine
main_game_loop()
