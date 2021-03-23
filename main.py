#/usr/bin/python3.8
import pygame
import time
import random

pygame.init()

black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)
red = (255,0,0)
yellow = (255, 255, 102)
green = (0, 255, 0)
grey = (170,170,170)
dark_grey = (100,100,100)

dis_width = 800
dis_height = 600

snake_block = 15

clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 50)

dis = pygame.display.set_mode((dis_width, dis_height))

pygame.display.update()
pygame.display.set_caption('Snake game')

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color, x, y):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [x, y])

def displayScore(sc, color):
    mesg = font_style.render("Score: " + str(sc), True, color)
    dis.blit(mesg, [15, 15])

def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1
    score = 0

    difficulty = 0
    
    foodx = round(random.randint(0+snake_block, dis_width-snake_block))
    foody = round(random.randint(0+snake_block, dis_height-snake_block))

    while difficulty == 0:
        for event in pygame.event.get():
            dis.fill(blue)
            message("Choose difficulty:", white, dis_width/100, 10)
            mouse = pygame.mouse.get_pos()

            #button 1
            if dis_width/20 <= mouse[0] <= dis_width/20+50 and dis_height/2 <= mouse[1] <= dis_height/2+50: 
                pygame.draw.rect(dis, grey, [dis_width/20, dis_height/2, 50, 50])
                dif_text = font_style.render("1", True, red)
                dis.blit(dif_text, (dis_width/20+15, dis_height/2+10))

                if event.type == pygame.MOUSEBUTTONDOWN:
                    difficulty = 1

          
            else: 
                pygame.draw.rect(dis, dark_grey, [dis_width/20, dis_height/2, 50, 50]) 
                dif_text = font_style.render("1", True, white)
                dis.blit(dif_text, (dis_width/20+15, dis_height/2+10))

            #button 2
            if dis_width/20+75 <= mouse[0] <= dis_width/20+125 and dis_height/2 <= mouse[1] <= dis_height/2+50: 
                pygame.draw.rect(dis, grey, [dis_width/20+75, dis_height/2, 50, 50])
                dif_text = font_style.render("2", True, red)
                dis.blit(dif_text, (dis_width/20+90, dis_height/2+10))

                if event.type == pygame.MOUSEBUTTONDOWN:
                    difficulty = 2
          
            else: 
                pygame.draw.rect(dis, dark_grey, [dis_width/20+75, dis_height/2, 50, 50]) 
                dif_text = font_style.render("2", True, white)
                dis.blit(dif_text, (dis_width/20+90, dis_height/2+10))
            
            #button 3
            if dis_width/20+150 <= mouse[0] <= dis_width/20+200 and dis_height/2 <= mouse[1] <= dis_height/2+50: 
                pygame.draw.rect(dis, grey, [dis_width/20+150, dis_height/2, 50, 50])
                dif_text = font_style.render("3", True, red)
                dis.blit(dif_text, (dis_width/20+165, dis_height/2+10))

                if event.type == pygame.MOUSEBUTTONDOWN:
                    difficulty = 3
            
            else: 
                pygame.draw.rect(dis, dark_grey, [dis_width/20+150, dis_height/2, 50, 50]) 
                dif_text = font_style.render("3", True, white)
                dis.blit(dif_text, (dis_width/20+165, dis_height/2+10))
            
            #button 4
            if dis_width/20+225 <= mouse[0] <= dis_width/20+275 and dis_height/2 <= mouse[1] <= dis_height/2+50: 
                pygame.draw.rect(dis, grey, [dis_width/20+225, dis_height/2, 50, 50])
                dif_text = font_style.render("4", True, red)
                dis.blit(dif_text, (dis_width/20+240, dis_height/2+10))

                if event.type == pygame.MOUSEBUTTONDOWN:
                    difficulty = 4
          
            else: 
                pygame.draw.rect(dis, dark_grey, [dis_width/20+225, dis_height/2, 50, 50]) 
                dif_text = font_style.render("4", True, white)
                dis.blit(dif_text, (dis_width/20+240, dis_height/2+10))
            
            #button 5
            if dis_width/20+300 <= mouse[0] <= dis_width/20+350 and dis_height/2 <= mouse[1] <= dis_height/2+50: 
                pygame.draw.rect(dis, grey, [dis_width/20+300, dis_height/2, 50, 50])
                dif_text = font_style.render("5", True, red)
                dis.blit(dif_text, (dis_width/20+315, dis_height/2+10))

                if event.type == pygame.MOUSEBUTTONDOWN:
                    difficulty = 5
          
            else: 
                pygame.draw.rect(dis, dark_grey, [dis_width/20+300, dis_height/2, 50, 50]) 
                dif_text = font_style.render("5", True, white)
                dis.blit(dif_text, (dis_width/20+315, dis_height/2+10))

            #button 6
            if dis_width/20+375 <= mouse[0] <= dis_width/20+425 and dis_height/2 <= mouse[1] <= dis_height/2+50: 
                pygame.draw.rect(dis, grey, [dis_width/20+375, dis_height/2, 50, 50])
                dif_text = font_style.render("6", True, red)
                dis.blit(dif_text, (dis_width/20+390, dis_height/2+10))

                if event.type == pygame.MOUSEBUTTONDOWN:
                    difficulty = 6
          
            else: 
                pygame.draw.rect(dis, dark_grey, [dis_width/20+375, dis_height/2, 50, 50]) 
                dif_text = font_style.render("6", True, white)
                dis.blit(dif_text, (dis_width/20+390, dis_height/2+10))

            #button 7
            if dis_width/20+450 <= mouse[0] <= dis_width/20+500 and dis_height/2 <= mouse[1] <= dis_height/2+50: 
                pygame.draw.rect(dis, grey, [dis_width/20+450, dis_height/2, 50, 50])
                dif_text = font_style.render("7", True, red)
                dis.blit(dif_text, (dis_width/20+465, dis_height/2+10))

                if event.type == pygame.MOUSEBUTTONDOWN:
                    difficulty = 7
          
            else: 
                pygame.draw.rect(dis, dark_grey, [dis_width/20+450, dis_height/2, 50, 50]) 
                dif_text = font_style.render("7", True, white)
                dis.blit(dif_text, (dis_width/20+465, dis_height/2+10))

            #button 8
            if dis_width/20+525 <= mouse[0] <= dis_width/20+575 and dis_height/2 <= mouse[1] <= dis_height/2+50: 
                pygame.draw.rect(dis, grey, [dis_width/20+525, dis_height/2, 50, 50])
                dif_text = font_style.render("8", True, red)
                dis.blit(dif_text, (dis_width/20+540, dis_height/2+10))

                if event.type == pygame.MOUSEBUTTONDOWN:
                    difficulty = 8
          
            else: 
                pygame.draw.rect(dis, dark_grey, [dis_width/20+525, dis_height/2, 50, 50]) 
                dif_text = font_style.render("8", True, white)
                dis.blit(dif_text, (dis_width/20+540, dis_height/2+10))
            
            #button 9
            if dis_width/20+600 <= mouse[0] <= dis_width/20+650 and dis_height/2 <= mouse[1] <= dis_height/2+50: 
                pygame.draw.rect(dis, grey, [dis_width/20+600, dis_height/2, 50, 50])
                dif_text = font_style.render("9", True, red)
                dis.blit(dif_text, (dis_width/20+615, dis_height/2+10))

                if event.type == pygame.MOUSEBUTTONDOWN:
                    difficulty = 9
          
            else: 
                pygame.draw.rect(dis, dark_grey, [dis_width/20+600, dis_height/2, 50, 50]) 
                dif_text = font_style.render("9", True, white)
                dis.blit(dif_text, (dis_width/20+615, dis_height/2+10))
            
            #button 10
            if dis_width/20+675 <= mouse[0] <= dis_width/20+725 and dis_height/2 <= mouse[1] <= dis_height/2+50: 
                pygame.draw.rect(dis, grey, [dis_width/20+675, dis_height/2, 50, 50])
                dif_text = font_style.render("10", True, red)
                dis.blit(dif_text, (dis_width/20+680, dis_height/2+10))

                if event.type == pygame.MOUSEBUTTONDOWN:
                    difficulty = 10
          
            else: 
                pygame.draw.rect(dis, dark_grey, [dis_width/20+675, dis_height/2, 50, 50]) 
                dif_text = font_style.render("10", True, white)
                dis.blit(dif_text, (dis_width/20+680, dis_height/2+10))

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            pygame.display.update()

    snake_speed = difficulty * 5
    snake_direction = ""

    while not game_over:
        while game_close == True:
            dis.fill(white)
            message("Looser! Press Q-Quit or C-Play Again", red, dis_width/100, 10)
            message("End score: "+str(score), red, dis_width/100, 50)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False

                    if event.key == pygame.K_c:
                        gameLoop()
                
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if snake_direction != "right":
                        x1_change = -snake_block
                        y1_change = 0
                        snake_direction = "left"

                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if snake_direction != "left":
                        x1_change = snake_block
                        y1_change = 0
                        snake_direction = "right"
            
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    if snake_direction != "down":
                        x1_change = 0
                        y1_change = -snake_block
                        snake_direction = "up"

                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if snake_direction != "up":
                        x1_change = 0
                        y1_change = snake_block
                        snake_direction = "down"

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        
        if x1 >= dis_width - snake_block*1.5 and snake_direction == "right":
            clock.tick(snake_speed/2)
        
        elif x1 <= 0 + snake_block*1.5 and snake_direction == "left":
            clock.tick(snake_speed/2)

        elif y1 >= dis_height - snake_block*1.5 and snake_direction == "down":
            clock.tick(snake_speed/2)
        
        elif y1 <= 0 + snake_block*1.5 and snake_direction == "up":
            clock.tick(snake_speed/2)

        x1 += x1_change
        y1 += y1_change

        dis.fill(blue)

        pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        
        our_snake(snake_block, snake_List)

        displayScore(score, white)

        if x1 <= foodx + 13 and x1 >= foodx -13 and y1 <= foody + 13 and y1 >= foody - 13:
            foodx = round(random.randint(0+snake_block, dis_width-snake_block))
            foody = round(random.randint(0+snake_block, dis_height-snake_block))

            Length_of_snake += 1
            score += difficulty

        pygame.display.update()
        clock.tick(snake_speed)

    dis.fill(blue)
    message("Looser", red, 10, 10)
    pygame.display.update()
    time.sleep(1.5)

    pygame.quit()
    quit()

gameLoop()