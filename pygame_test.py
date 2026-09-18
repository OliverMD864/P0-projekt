import pygame
import cv2 as cv
import numpy as np
import os

pos = [(0,0),(1,0),(2,0),(3,0),(4,0),(0,1),(1,1),(2,1),(3,1),(4,1),(0,2),(1,2),(2,2),(3,2),(4,2),(0,3),(1,3),(2,3),(3,3),(4,3),(0,4),(1,4),(2,4),(3,4),(4,4)]
image_num = 0
right_button_was_pressed = False
wrong_button_was_pressed = False

margin=2
image = 74
image_path = rf"KingDominoTestsaet\{image}.jpg"
answers_path = open(f"answer{image}.txt", "r").readlines()
answers_len = len(answers_path)


pygame.init()
screen = pygame.display.set_mode((200, 200))
clock = pygame.time.Clock()

def show_pic(x, y ):
    rect = pygame.Rect(x * 100, y * 100, 100, 100) # størrelsen er altid 100, 100 for hver tile
    sprite = full_image.subsurface(rect)

    return sprite


done = False
run_flag = True
while run_flag:
    

    if not done and image_num < len(pos):
        screen.fill((255, 255, 255))
        full_image = pygame.image.load(image_path).convert()

        
        pic_sprite = show_pic(*pos[image_num])

        keys = pygame.key.get_pressed()

        screen.blit(pic_sprite, (50,0))

        # write answer to the screen
        font = pygame.font.Font(None, 36)
        terrain_text = font.render(answers_path[image_num], True, (0, 0, 0))

        screen.blit(terrain_text, (50, 100))


        # make a button for the right image
        right_button = pygame.Rect(150, 150, 50, 50)
        pygame.draw.rect(screen, (0, 255, 0), right_button)

        # make a button for the wrong image
        wrong_button = pygame.Rect(0, 150, 50, 50)
        pygame.draw.rect(screen, (255, 0, 0), wrong_button)

        # check if the button is pressed
        if right_button.collidepoint(pygame.mouse.get_pos()) and not right_button_was_pressed:
            if pygame.mouse.get_pressed()[0]:
                # save the image number to a file
                with open("right_and_wrong_74.txt", "a") as f:
                    f.write(str(pos[image_num]) + "rigtig\n")
                image_num += 1
                   

        # check if the wrong button is pressed
        if wrong_button.collidepoint(pygame.mouse.get_pos()) and not wrong_button_was_pressed:
            if pygame.mouse.get_pressed()[0]:
                # save the image number to a file
                with open("right_and_wrong_74.txt", "a") as f:
                    f.write(str(pos[image_num]) + "forkert\n")
                image_num += 1


        
        right_button_was_pressed = right_button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]
        wrong_button_was_pressed = wrong_button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]

        if image_num == 25:
         # udregn procent af rigtige  
            with open("right_and_wrong_74.txt","r") as f:
                lines = f.readlines()[-25:]
                right = 0 
                wrong = 0
                for line in lines: 
                    if "rigtig" in line: 
                        right += 1
                    elif "forkert" in line: 
                        wrong += 1
                procent = right*4
                procent_text = font.render(str(procent) + "%", True, (0, 0, 0))
                screen.blit(procent_text, (140, 100))
                with open("procent rigtige.txt", "a") as f:
                    f.write(f"Nr.{image} {procent}% rigtig\n")

        pygame.display.flip()



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_flag = False


pygame.quit()