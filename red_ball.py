import pygame
pygame.init()
screen = pygame.display.set_mode((480, 320))
done = False
x = 30
y = 30
clock = pygame.time.Clock()
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_ESCAPE]: done=True
        if pressed[pygame.K_UP]: y -= 3
        if pressed[pygame.K_DOWN]: y += 3
        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3
        if x>=480-23: x-=3
        if x<=0+23: x+=3
        if y>=320-23: y-=3
        if y<=0+23: y+=3
        screen.fill((255,255,255))
        pygame.draw.circle(screen,(255,0,0),(x,y), 25)
        pygame.display.flip()
        clock.tick(60)
