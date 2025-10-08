class TheDog:
    def __init__(self, dog,voice):
        self.dog = dog
        self.voice = voice

    def dog_voice(self):
        print(f"Собака гавкает: {self.voice}")

    def dog_name(self):
        print(f"Вид собаки: {self.dog}")
    def full_dog(self):
        print(f"Вид собаки: {self.dog}\nГолос: {self.voice}")


import pygame
pygame.init()

dis = pygame.display.set_mode((500,400))
r = pygame.Rect(50, 100, 100, 100)

dis_over=False
while not dis_over:
    for event in pygame.event.get():
        pygame.draw.rect(dis, (255, 0, 0), r, 10)
        pygame.draw.circle(dis, (200, 50, 50), (100, 70), 15)
        pygame.draw.polygon(dis, (120, 160, 50), [(100, 100), (0, 100), (50, 10)])
        pygame.display.update()
        if event.type == pygame.QUIT:
            pygame.quit()

quit()




# dis_over = False
# while not dis_over:
#     for event in pygame.event.get():
#         pygame.draw.circle(dis, (255, 255, 255), (240, 300), 50)
#         pygame.draw.circle(dis, (255, 255, 255), (240, 220), 30)
#         pygame.draw.circle(dis, (255, 255, 255), (240, 170), 20)
#         pygame.draw.circle(dis, (0, 0, 0), (240, 270), 3)
#         pygame.draw.circle(dis, (0, 0, 0), (240, 220), 3)
#         pygame.draw.circle(dis, (0, 0, 0), (232, 165), 3)
#         pygame.draw.circle(dis, (0, 0, 0), (247, 165), 3)
#         pygame.draw.lines(dis, (120, 50, 50), False, [(210, 210), (180, 300)], 5)
#         pygame.draw.lines(dis, (120, 50, 50), False, [(270, 210), (300, 300)], 5)
#         pygame.draw.polygon(dis, (255, 95, 15), [(250, 170), (230, 170), (240, 200)])
#         # pygame.draw.polygon(dis, (173, 173, 173), [(300, 170), (230, 170), (240, 200), (50, 50)])
#         pygame.display.update()
#         if event.type == pygame.QUIT:
#             pygame.quit()
#
# quit()

# buldog = TheDog("Бульдог", "Гав гав")
#
# buldog.dog_voice()
#
# buldog.dog_name()



import pygame
from pygame.colordict import THECOLORS

pygame.init()

dis = pygame.display.set_mode((600, 400))
dis.fill(THECOLORS["gray"])
font = pygame.font.SysFont("couriernew", 40)
r = pygame.Rect(100, 100 ,100 ,100)

dis_over = False
while not dis_over:
    for event in pygame.event.get():
        for x in range(1, 600, 50):
            for y in range(1, 600 ,50):
                pygame.draw.rect(dis, (255, 255, 255), (x, y, 40, 40), 1)
                text = font.render(("1"), True, THECOLORS["green"])
                dis.blit(text, (x+10, y+10))
            pygame.display.update()
            if event.type == pygame.QUIT:
                pygame.quit()

quit()

# for x in range(10, 600, 60):
#     pygame.draw.rect(dis, white_colour, (x,y, 40, 40), 0)
#     pygame.display.flip()
#     dis.blit(font, (x, y))
#
#
#     for y in range(10, 600, 60):
#         pygame.draw.rect(dis, white_colour, (x,y, 40, 40), 0)
#         dis.blit(font, (x, y))