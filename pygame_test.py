import pygame

pos = [(0,0),(1,0),(2,0),(3,0),(4,0),(0,1),(1,1),(2,1),(3,1),(4,1),(0,2),(1,2),(2,2),(3,2),(4,2),(0,3),(1,3),(2,3),(3,3),(4,3),(0,4),(1,4),(2,4),(3,4),(4,4)]
image_num = 0
right_button_was_pressed = False
wrong_button_was_pressed = False



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
        full_image = pygame.image.load(r"KingDominoTestsaet\4.jpg")

        # aner ik hvad * gør
        pic_sprite = show_pic(*pos[image_num])

        keys = pygame.key.get_pressed()

        screen.blit(pic_sprite, (50,0))

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