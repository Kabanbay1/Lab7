import pygame, datetime

WIDTH = 1400
HEIGHT = 1050

pygame.init()

def blitRotateCenter(surf, image, angle):
    
    rect = image.get_rect(center = (WIDTH//2,HEIGHT//2))
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_rect = rotated_image.get_rect(center = rect.center)
    surf.blit(rotated_image, rotated_rect)


screen=pygame.display.set_mode((WIDTH, HEIGHT))     

done = False

sec=datetime.datetime.now().second
min1=datetime.datetime.now().minute

angle1=sec*6
angle2=(min1*6)+55

min_arm=pygame.image.load("rightarm.png").convert_alpha()
sec_arm=pygame.image.load("leftarmm.png").convert_alpha()
bg=pygame.image.load("mainclock.png")

clock=pygame.time.Clock()

while not done:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            done = True

        if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                      exit()
    screen.fill("white")    

    angle1+=6
    if angle1>=360:
        angle2+=6
        angle1=0

    screen.blit(bg, (0,0))
    blitRotateCenter(screen, min_arm, -angle2)
    blitRotateCenter(screen, sec_arm, -angle1)

    pygame.display.update()

    clock.tick(15)
    pygame.time.wait(1000)