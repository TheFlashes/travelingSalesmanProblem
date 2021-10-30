import pygame

class Point:
    def __init__(self, x, y, index):
        self.x, self.y, self.index = x, y, index

    def draw(self, screen, font):
        pygame.draw.circle(screen, (255, 255, 255), (self.x + 50, self.y+ 50), 10)

        pointNo = font.render("{}".format(self.index), False, (0, 0, 0))
        if self.index < 10: screen.blit(pointNo, (self.x + 45, self.y + 38))
        else: screen.blit(pointNo, (self.x + 39, self.y + 38))