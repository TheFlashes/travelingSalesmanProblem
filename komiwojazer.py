
from random import randint
from random import seed
import pygame

seed(1)


class Komiwojazer:
    def __init__(self, width, height, noOfPoints):
        self.width, self.height, self.noOfPoints = width, height, noOfPoints

        pygame.init()

        pygame.display.set_caption('Jak będzie w grafach hamiltonowskich? - sekcja Komiwojażera')

        self.screen = pygame.display.set_mode((self.width + 100, self.height + 100))
        self.clock = pygame.time.Clock()

        pygame.font.init()
        self.font = pygame.font.SysFont('Arial', 17)

        self.randomPoints()

        while 1:
            self.gameLoop()
    
    def randomPoints(self):
        self.points = []
        for i in range(0, self.noOfPoints):
            self.points.append({
                "index": i,
                "x": randint(0, self.width),
                "y": randint(0, self.height)
            })

    def drawPoint(self, point):
        pygame.draw.circle(self.screen, (255, 255, 255), (point['x'] + 50, point['y']+ 50), 10)

        pointNo = self.font.render("{}".format(point['index']), False, (0, 0, 0))
        if point['index'] < 10: self.screen.blit(pointNo, (point['x'] + 47, point['y'] + 40))
        else: self.screen.blit(pointNo, (point['x'] + 42, point['y'] + 40))

    def gameLoop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.randomPoints()

        self.screen.fill((0, 0, 255))

        pygame.draw.rect(self.screen, (255, 255, 255), (50, 50, self.width, self.height), 1)

        for point in self.points:
            self.drawPoint(point)

        pygame.display.flip()

        self.clock.tick(40)


komiwojazer = Komiwojazer(
    width=500,
    height=500,
    noOfPoints=10
)
