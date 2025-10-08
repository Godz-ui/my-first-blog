# /////// First Ex ///////
import pygame
# with open("new.txt", "w") as myfile:
#     myfile.write(" bye bye txt")

# from Class_Dog import TheDog
#
# buldog = TheDog("Бульдог", "Гав гав")
#
# buldog.dog_voice()
#
# buldog.full_dog()

import pygame
from django.contrib.admin import display

pygame.init()


dis = pygame.display.set_mode((1000,800))
# r = pygame.Rect(190,170,150,110)
# q = pygame.Rect(200,180,130,90)

a = pygame.Rect(190,170,150,110)
b = pygame.Rect(200,180,130,90)
c = pygame.Rect(190,270,150,140)
d = pygame.Rect(380,170,100,100)
# el = pygame.Rect(700, 190,100,100)



dis_over = False
while not dis_over:
    for event in pygame.event.get():
        # pygame.draw.rect(dis, (255, 0, 0), a, 10)
        # pygame.draw.rect(dis, (204, 2, 102), b, 10)
        # pygame.draw.rect(dis, (255, 0, 0), c, 10)
        # pygame.draw.rect(dis, (204, 2, 102), d, 10)
        # pygame.draw.line(dis, (204, 100, 102),[150,100],[10,200])
        pygame.draw.circle(dis,(232, 190, 172), (700, 190), 150)
        pygame.draw.circle(dis,(255,255,255), (630, 165), 45)
        pygame.draw.circle(dis,(0,0,0), (630, 165), 20)
        pygame.draw.circle(dis,(255,255,255), (760, 165), 45)
        pygame.draw.circle(dis,(0,0,0), (760, 165), 20)
        pygame.draw.line(dis, (204, 100, 190),[700,200],[800,200])
        # pygame.draw.ellipse(dis,(232, 190, 172), el,0)

        pygame.display.update()
        if event.type == pygame.QUIT:
            pygame.quit()



quit()

# ///////          ////////