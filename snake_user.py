import pygame
import random
import os

def user_snake():
        x=200
        y=200
        os.environ['SDL_VIDEO_WINDOW_POS']= "%d,%d"%(x,y)
        pygame.init()  # initialize pygame all events

        # colors to describe for game
        red = (255, 0, 0)
        white = (255, 255, 255)
        black = (0, 0, 0)
        blue=[0,0,255]

        screen_width = 420
        screen_height = 420

        # creating gaming window
        gameWindow = pygame.display.set_mode((screen_width, screen_height))
        # Game title
        pygame.display.set_caption("SNAKE BY SHIVAM")
        pygame.display.update()

        background=pygame.image.load("Game_Files/snake_game_project/img/background.png")

        clock = pygame.time.Clock()  # to update frames on time as per requirement, we have to control events on clock
        # to show score on screen:
        font = pygame.font.SysFont(None, 23)


        def text_screen(text, color,x,y):# this function is for (what to put on screen, what color for it, what position of x, what position of y)
            screen_text = font.render(text, True,color) #it is function of pygame. its first arguement is what to put on screen, 2nd arguement= Anti-aliasing. In this, we put high resolution to resolution
            gameWindow.blit(screen_text,(x,y)) #this will update the screen for score
        #We have to try to write minimum possible code in loop as it reduce slow processing issues.

        # this part is to add rectangle when snake eats the list
        def plot_snake(gameWindow, color,snk_list, snake_size):
            for x,y in snk_list:
                pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

        def gameloop():
            exit_game = False
            game_over = False
            snake_x = 55
            snake_y = 55
            velocity_x = 0  # initially speed of snake in x direction. wanna know why, then run previous one program
            velocity_y = 0  # initially speed of snake in x direction
            snake_size = 20
            fps = 30
            # random module is to be used to give food for snake
            food_x = random.randint(20, abs((screen_width*10) / 42))
            food_y = random.randint(20, abs((screen_height*10) / 42))

            score = 0
            init_velocity =5 

            # Now,for increasing size of snake:
            snk_list = []
            snk_length =1

            # to always know the best score exist in game:
            with open("hiscore.txt", "r") as f:
                hiscore = f.read()

            while not exit_game:
                
                if game_over:
                    with open("hiscore.txt", "w") as f:
                        f.write(str(hiscore))
                    
                    gameWindow.fill(white)
                    
                    text_screen("GAME OVER!!", red, screen_width/3,screen_height/4)
                    text_screen("Press Enter to continue.", red, screen_width / 4, screen_height / 3)

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            exit_game = True
                    
                        if event.type == pygame.KEYDOWN:
                            if event.key==pygame.K_RETURN:
                                gameloop()
                else:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            exit_game = True

                        if event.type == pygame.KEYDOWN:  # when pressed doen
                            if event.key == pygame.K_RIGHT:  # when right arrow key
                                velocity_x = init_velocity # snake moves 10 step at a time in x
                                velocity_y=0     # velocity_y=0

                            if event.key == pygame.K_LEFT:  # when left arrow key
                                velocity_x = - init_velocity  # snake moves 10 step at a time
                                velocity_y = 0

                            if event.key == pygame.K_UP:  # when Up arrow key
                                velocity_y = - init_velocity  # snake moves 10 step at a time
                                velocity_x = 0

                            if event.key == pygame.K_DOWN:  # when Down arrow key
                                velocity_y = init_velocity  # snake moves 10 step at a time
                                velocity_x = 0

                    # here, we gave the velocity to snake.
                    snake_x = snake_x + velocity_x
                    snake_y = snake_y + velocity_y

                    if abs(snake_x - food_x)<10 and abs(snake_y - food_y)<10:
                        score+=10
                        food_x = random.randint(50, screen_width/2)
                        food_y=random.randint(50,screen_height/2)
                        snk_length+=5
                        if score> int(hiscore):
                            hiscore=score

                    gameWindow.fill(white)
                    gameWindow.blit(background,(0,0))
                    #this code is to show score on gameWindow
                    text_screen("Score: "+str(score)+ "  HiScore: " + str(hiscore), red, 25, 25)
                    # this code is for food of snake.
                    pygame.draw.rect(gameWindow, blue, [food_x, food_y, snake_size, snake_size])
                    # Here, we draw the head of snake using rectangle pygame.draw.rect(where to draw, what color of head, [position in x, position in y, size of snake,size of snake])

                    #head list contains additional head values to increase its size by adding more heads on it and start the snake initially.
                    head = []
                    head.append(snake_x)
                    head.append(snake_y)
                    snk_list.append(head)

                    if len(snk_list)>snk_length:
                        del snk_list[0]

                    # this part is to handle collision of snake with itself. If, the head coordinate is lying in list, then game over.
                    if head in snk_list[:-1]:
                        game_over = True

                    #if snake touches any side of gameWindow.
                    if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                        game_over=True

                    #This will plot the snake size
                    plot_snake(gameWindow, red, snk_list, snake_size)
                pygame.display.update()  # To see any changes in game we have to run this.
                clock.tick(fps)

            pygame.quit()
            quit()
        gameloop()

