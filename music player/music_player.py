import pygame
pygame.font.init()
playlist=["audio.mp3","bwa.mp3", "lepr.mp3","night.mp3","sunf.mp3"]
screen = pygame.display.set_mode((800, 600))
done = False
mus=False
i=0
bg = (0, 0, 0)
tc = (43, 159, 140)
pygame.display.set_caption('Music Player')
fontObj = pygame.font.Font(None, 32)
textSufaceObj = fontObj.render('Tab - Play|Right Arrow - Next Song|Left Arrow - Previous Song|Space - Stop', True, tc, None)
screen.fill(bg)
screen.blit(textSufaceObj, (0, 0))
pygame.display.update()
pygame.mixer.init()
while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                      exit()
                if event.key == pygame.K_TAB:
                            pygame.mixer.music.load(playlist[i])
                            pygame.mixer.music.play(0)
                            mus=True
                if event.key ==pygame.K_RIGHT and mus==True:
                    i+=1
                    if i>len(playlist)-1:
                        i=0
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(playlist[i])
                    pygame.mixer.music.play()
                if event.key ==pygame.K_LEFT and mus==True:
                    i-=1
                    if i<0:
                        i=len(playlist)-1
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(playlist[i])
                    pygame.mixer.music.play()
                if event.key ==pygame.K_SPACE:
                    pygame.mixer.music.stop()