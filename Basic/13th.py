import pygame
from django.template.defaultfilters import random
from pygame.colordict import THECOLORS

from twelve import dis_over

dis = pygame.display.set_mode((600,600))
a = pygame.Rect(190,170,150,110)
el1 = pygame.Rect(280, 240,25,40)
el2 = pygame.Rect(180, 245,30,45)



font = pygame.font.SysFont('couriernew',40)
tex = font.render('Snow', True, (255,0,0))

num = 0
snowflake = []

for _ in range(300):
    x.random.randint(0,600)
    y.random.randint(-600, 0)
    snowflake.append([x,y])

while not dis_over:
    for event in pygame

dis_over = False
while not dis_over:
    for event in pygame.event.get():
        # Тело:
        pygame.draw.circle(dis, (255, 255, 255), (240, 400), 100)
        pygame.draw.circle(dis, (255, 255, 255), (240, 250), 60)
        pygame.draw.circle(dis, (255, 255, 255), (240, 155), 40)
        # Пуговицы:
        pygame.draw.circle(dis, (0,0,0), (240, 270), 7)
        pygame.draw.circle(dis, (0,0,0), (240, 250), 7)
        pygame.draw.circle(dis, (0,0,0), (240, 230), 7)
        # Шляпа:
        pygame.draw.polygon(dis, (128, 0, 0), [(280, 125), (200, 125), (240, 20)])
        pygame.draw.circle(dis, (150,0,0), (240, 25), 15)
        # Голова:

        # pygame.draw.polygon(dis, (255, 0, 0), [(10, 100), (10,10), (100, 200)])

        # Глаза:
        pygame.draw.circle(dis, (0, 0,0), (225, 150), 7)
        pygame.draw.circle(dis, (0, 0,0), (255, 150), 7)
        # Руки:
        # pygame.draw.ellipse(dis, (255,250,250), el1, 0)
        # pygame.draw.ellipse(dis, (255,250,250), el2, 0)
        pygame.draw.line(dis,(137, 81, 41), (186,278), (100,220), 3)
        pygame.draw.line(dis,(137, 81, 41), (396,216), (300,263), 3)
        pygame.display.update()
        dis.fill(THECOLORS["lightblue"])

        for snowflake in snowflakes:
            pygame.draw.circle(dis, (0, 0, 0), (snowflake[0], snowflake[1]), 5, 0)
            snowflake[1] += 15

            if snowflake[1] > 600:
                snowflake[1] = random.randint(-50, 0)
                snowflake[0] = random.randint(0, 600)

        dis.blit(text, (num, 46))
        num += 5

        pygame.display.flip()
        pygame.time.delay(38)
            pygame.quit()

quit()

# for snowflake in snowflakes:
#     pygame.draw.circle(dis,(0,0,0), (snowflake[0], snowflake[1]),5,0)
#     snowflake[1] +=15
#
#     if snowflake[1] > 600:
#         snowflake[1] = random.randint(-50,0)
#         snowflake[0] = random.randint(0, 600)
#
# dis.blit(text,(num,46))
# num += 5
#
# pygame.display.flip()
# pygame.time.delay(38)