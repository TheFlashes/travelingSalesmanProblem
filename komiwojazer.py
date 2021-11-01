from src.point import Point
from src.drawMatrix import drawMatrix
from random import randint
import time
import pygame

class Komiwojazer:
    def __init__(self, width, height, noOfPoints):
        self.width, self.height, self.noOfPoints = width, height, noOfPoints

        pygame.init()
        pygame.display.set_caption('Jak będzie w grafach hamiltonowskich? - sekcja Komiwojażera')

        self.screen = pygame.display.set_mode((self.width + 100, self.height + 100))
        self.clock = pygame.time.Clock()

        pygame.font.init()
        self.font = pygame.font.SysFont('Verdana', 17)

        self.reset()

        while 1:
            self.gameLoop()

    #=============================Wstępne obliczenia=============================
    def reset(self):
        print("\n\n\n\n")
        self.points = []
        self.distances = []
        self.randomPoints()
        self.calculateDistances()
        self.heldKrapParents = {}
        self.pointToCalcuate = []
        self.route = []
        self.noOfOperations = 0
        for i in range(0, self.noOfPoints):
            self.heldKrapParents[i] = {}
        for i in range(1, self.noOfPoints):
            self.pointToCalcuate.append(i)
        drawMatrix(self.noOfPoints, self.distances)

    def randomPoints(self):
        self.points = []
        for i in range(0, self.noOfPoints):
            self.points.append(Point(
                index=i,
                x=randint(0, self.width),
                y=randint(0, self.width)
            ))

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

    def distanceBetweenPoints(self, point1, point2):
        return ((point1.x - point2.x)**2 + (point1.y - point2.y)**2)**.5
    #=============================Wstępne obliczenia=============================

    #=============================Właściwy algorytm==============================
    def startAlgorithm(self):
        print(f"Obliczanie najkrótszej drogi miedzy {self.noOfPoints} punktami...")
        tic = time.perf_counter()
        komiwojazer_data = self.heldKrapFun(0, self.pointToCalcuate)
        self.findRoute(0, self.pointToCalcuate)
        toc = time.perf_counter()
        print(f"Najkrótsza droga wynosi: {komiwojazer_data}\nNajkrótsza ścieżka: {self.route}\nObliczenia zajęły: {toc - tic:0.4f}s\nLiczba operacji: {self.noOfOperations}")

    def heldKrapFun(self, startPoint, pointsCollection):
        parentStartID = startPoint
        parentArrayID = f"{pointsCollection}"

        if parentStartID in self.heldKrapParents:
            if parentArrayID in self.heldKrapParents[parentStartID]:
                return self.heldKrapParents[parentStartID][parentArrayID]["distance"]

        self.noOfOperations += 1

        if len(pointsCollection) == 0:
            self.heldKrapParents[parentStartID][parentArrayID] = {
                "parent": 0,
                "distance": self.distances[0][startPoint]
            }
            return self.distances[0][startPoint]
        else:
            distances = []
            for idx, pt in enumerate(pointsCollection):
                heldKrapResult = self.heldKrapFun(pt, pointsCollection[:idx] + pointsCollection[idx+1 :])
                distances.append(
                    self.distances[pt][startPoint] +
                    heldKrapResult
                )
            min_value = min(distances)
            parent = pointsCollection[distances.index(min_value)]
            self.heldKrapParents[parentStartID][parentArrayID] = {
                "parent": parent,
                "distance": min_value
            }
            return min_value

    def findRoute(self, startPoint, pToCalculate):
        if pToCalculate == []:
            self.route.append(0)
        else:
            lastParent  = self.heldKrapParents[startPoint][f"{pToCalculate}"]['parent']
            self.route.append(lastParent)
            pToCalculate.remove(lastParent)
            self.findRoute(lastParent, pToCalculate)
    #=============================Właściwy algorytm==============================

    #==============================Pętla z ekranem===============================
    def gameLoop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.reset()
                if event.key == pygame.K_RETURN:
                    self.startAlgorithm()
                if event.key == pygame.K_UP:
                    self.noOfPoints += 1
                    self.reset()
                if event.key == pygame.K_DOWN:
                    if self.noOfPoints > 1: self.noOfPoints -= 1
                    self.reset()

        self.screen.fill((2, 119, 189))

        infoText = self.font.render(f"Liczba punktów: {self.noOfPoints}", False, (255, 255, 255))
        self.screen.blit(infoText, (5, 5))

        pygame.draw.rect(self.screen, (255, 255, 255), (50, 50, self.width, self.height), 2)

        for idx, r in enumerate(self.route):
            secondIndex = idx+1 if idx < len(self.route)-1 else 0
            pygame.draw.line(self.screen, (255, 255, 255), 
                (self.points[r].x + 50, self.points[r].y + 50), 
                (self.points[self.route[secondIndex]].x + 50, self.points[self.route[secondIndex]].y + 50),
                width=1
            )

        for point in self.points:
            point.draw(self.screen, self.font)

        pygame.display.flip()
        self.clock.tick(40)
    #==============================Pętla z ekranem===============================


komiwojazer = Komiwojazer(
    width=500,
    height=500,
    noOfPoints=10
)
