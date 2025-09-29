from timeit import repeat

import pygame
from pygame.colordict import THECOLORS
from pygame.gfxdraw import filled_ellipse

with open('number.txt''r') as file:
    filled_squares = set(int(line.strip()) for line in file if line.strip().isdigit())


count = 1




pygame.init()

white_colour = (255,255,255)
red_colour = (255,0,0)
green_colour = (0,128,0)

dis = pygame.display.set_mode((600,600))
r = pygame.Rect(0,10,40,40)

font = pygame.font.SysFont('couriermew', 25)

dis_over = False
while not dis_over:
    for event in pygame.event.get():
        # pygame.draw.rect(dis,(white_colour), r ,0)
        # dis.blit(font, (10, 10))


        # while x < 600:
        #     pygame.draw.rect(dis, (white_colour), (x, 10, 40, 40), 0)
        #     x += 60


        dis.fill(THECOLORS['skyblue'])

        for  nam1 in range(10):
            for nam2 in range(10):
                x = nam1 * 60
                y = nam2 * 60
                text = font.render(f'{nam2}{nam1}', True, (green_colour))
                pygame.draw.rect(dis, (white_colour), (x + 10, y + 10 , 40, 40), 0)
                dis.blit(text, (x + 10,y + 10))


        pygame.display.update()
        if event.type == pygame.QUIT:
            pygame.quit()


quit()





