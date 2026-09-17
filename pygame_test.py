import pygame

pos = [(0,0),(1,0),(2,0),(3,0),(4,0),(0,1),(1,1),(2,1),(3,1),(4,1),(0,2),(1,2),(2,2),(3,2),(4,2),(0,3),(1,3),(2,3),(3,3),(4,3),(0,4),(1,4),(2,4),(3,4),(4,4)]
image_num = 0
left_was_pressed = False


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

        screen.blit(pic_sprite, (25, 25))

        # FIKS MIG
        if keys[pygame.K_LEFT] and not left_was_pressed:
            image_num += 1

        left_was_pressed = keys[pygame.K_LEFT]

        pygame.display.flip()
        clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_flag = False


pygame.quit()