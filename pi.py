import pygame
import random

pygame.init()
running = True
screen = pygame.display.set_mode((600,600))
i = 0
total = 1000
count = 0


points = []

for i in range(total):
        randompointx = random.randint(0,600)
        randompointy = random.randint(0,600)

        points.append((randompointx,randompointy))

        distance = ((randompointx - 300)**2 + (randompointy - 300)**2)**0.5
        if distance <= 300:
           count += 1

        
        pygame.draw.circle(screen, (0,255,0), (randompointx, randompointy), 5)
        i += 1

pi = (count/total)*4

print('the amount of points that landed in the circle is ' ,count)
print('to calculate pi, we just multiply the ratio of points in the circle to out of the circle' \
'by 4. in our case it would be ', count, '/', total, ' * 4 = ', pi)

while running:
    randompointx = random.randint(0,600)
    randompointy = random.randint(0,600)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    

    pygame.draw.circle(screen, (255,0,0), (300,300), 300, 5)
    pygame.display.update()

pygame.quit()