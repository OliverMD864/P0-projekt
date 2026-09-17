import pygame
import cv2 as cv
import numpy as np
import os

pos = [(0,0),(1,0),(2,0),(3,0),(4,0),(0,1),(1,1),(2,1),(3,1),(4,1),(0,2),(1,2),(2,2),(3,2),(4,2),(0,3),(1,3),(2,3),(3,3),(4,3),(0,4),(1,4),(2,4),(3,4),(4,4)]
image_num = 0
right_button_was_pressed = False
wrong_button_was_pressed = False

margin=2
image_path = r"KingDominoTestsaet\74.jpg"

# Main function containing the backbone of the program
def main():
    
    if not os.path.isfile(image_path):
        print("Image not found")
        return
    image = cv.imread(image_path)
    tiles = get_tiles(image)
# Break a board into tiles
def get_tiles(image):
    tiles = []
    for y in range(5):
        tiles.append([])
        for x in range(5):
            tiles[-1].append(image[y*100:(y+1)*100, x*100:(x+1)*100])
    return tiles
terrain = ""
# Determine the type of terrain in a tile
def get_terrain(tile):
    hsv_tile = cv.cvtColor(tile, cv.COLOR_BGR2HSV)
    hue, saturation, value = np.median(hsv_tile, axis=(0,1))

    if (23-margin) <= hue <= (43+margin) and (40-margin) <= saturation <= (155+margin) and (29.5-margin) <= value <= (47+margin):
        return "Mine"
    if (23-margin) <= hue <= (26+margin) and (223-margin) <= saturation <= (255+margin) and (145-margin) <= value <= (205+margin):
        return "Field"
    if (23-margin) <= hue <= (66+margin) and (65-margin) <= saturation <= (222+margin) and (37-margin) <= value <= (68+margin):
        return "Forest"
    if (104-margin) <= hue <= (108+margin) and (232-margin) <= saturation <= (255+margin) and (123-margin) <= value <= (191+margin):
        return "Lake"
    if (37-margin) <= hue <= (51+margin) and (156-margin) <= saturation <= (238+margin) and (92-margin) <= value <= (166+margin):
        return "Grassland"
    if (20-margin) <= hue <= (25+margin) and (62-margin) <= saturation <= (157+margin) and (33-margin) <= value <= (130+margin):
        return "Swamp"
    if (17-margin) <= hue <= (38+margin) and (41-margin) <= saturation <= (128+margin) and (64-margin) <= value <= (123+margin):
        return "Home"
    else:
        return "Unknown"

if __name__ == "__main__":
    main()


pygame.init()
screen = pygame.display.set_mode((200, 200))
clock = pygame.time.Clock()

def show_pic(x, y ):
    rect = pygame.Rect(x * 100, y * 100, 100, 100) # størrelsen er altid 100, 100 for hver tile
    sprite = full_image.subsurface(rect)

    return sprite

run_flag = True
while run_flag:
    

    for i in range(25):
        screen.fill((255, 255, 255))
        full_image = pygame.image.load(image_path).convert()

        # aner ik hvad * gør
        pic_sprite = show_pic(*pos[image_num])

        keys = pygame.key.get_pressed()

        screen.blit(pic_sprite, (50,0))

        # write gettarrain to the screen
        font = pygame.font.Font(None, 36)
        terrain_text = font.render(get_terrain(*pos[image_num]*100), True, (0, 0, 0))
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
                with open("right_and_wrong_txt.txt", "a") as f:
                    f.write(str(pos[image_num]) + "rigtig\n")
                image_num += 1
                if image_num > 24:
                    image_num = 0   

        # check if the wrong button is pressed
        if wrong_button.collidepoint(pygame.mouse.get_pos()) and not wrong_button_was_pressed:
            if pygame.mouse.get_pressed()[0]:
                # save the image number to a file
                with open("right_and_wrong_txt.txt", "a") as f:
                    f.write(str(pos[image_num]) + "forkert\n")
                image_num += 1
                if image_num > 24:
                    image_num = 0


        
        right_button_was_pressed = right_button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]
        wrong_button_was_pressed = wrong_button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]

        pygame.display.flip()
        

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_flag = False


pygame.quit()