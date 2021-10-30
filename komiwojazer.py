from src.point import Point
from src.drawMatrix import drawMatrix
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
        self.font = pygame.font.SysFont('Verdana', 17)

        self.points = []
        self.distances = []
        self.randomPoints()

        while 1:
            self.gameLoop()

    def randomPoints(self):
        self.points = []
        for i in range(0, self.noOfPoints):
            self.points.append(Point(
                index=i,
                x=randint(0, self.width),
                y=randint(0, self.width)
            ))
        self.calculateDistances()

    def calculateDistances(self):
        self.distances = []
        for x in range(0, len(self.points)):
            row = []
            for y in range(0, len(self.points)):
                row.append(self.distanceBetweenPoints(
                    self.points[x],
                    self.points[y]
                ))
            self.distances.append(row)
        drawMatrix(self.noOfPoints, self.distances)

    def distanceBetweenPoints(self, point1, point2):
        return ((point1.x - point2.x)**2 + (point1.y - point2.y)**2)**.5

    def gameLoop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.randomPoints()

        self.screen.fill((2, 119, 189))

        pygame.draw.rect(self.screen, (255, 255, 255), (50, 50, self.width, self.height), 1)

        for point in self.points:
            point.draw(self.screen, self.font)

        debugInfo = self.font.render("Odległość między 0 i 1: {}".format(
            self.distanceBetweenPoints(self.points[0], self.points[1])), False, (0, 0, 0))
        self.screen.blit(debugInfo, (0, 0))

        pygame.display.flip()

        self.clock.tick(40)


komiwojazer = Komiwojazer(
    width=500,
    height=500,
    noOfPoints=10
)
