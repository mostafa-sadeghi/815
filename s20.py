import pygame
pygame.init()


size = (700, 500)
screen = pygame.display.set_mode(size)
xposition = 0
yposition = 0
done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), [xposition, yposition, 50, 50])
    xposition += 1
    yposition += 1
    pygame.display.flip()
