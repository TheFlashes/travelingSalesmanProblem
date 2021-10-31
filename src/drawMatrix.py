def drawMatrix(noOfPoints, distances):
    def getS(num):
        num = str(int(num))
        if len(num) > 3:
            num = num[0:3]
        if len(num) == 2:
            num = " " + num
        if len(num) == 1:
            num = " " + num + " "
        return num

    def drawBorder(output):
        for i in range(0, 4 * (noOfPoints + 1)):
            output += "-"
        output += "\n"
        return output

    output = "Dystanse między punktami:\n   |"

    for i in range(0, noOfPoints):
        output += "{}|".format(getS(i))
    output += "\n"
    output = drawBorder(output)

    for y in range(0, noOfPoints):
        output += "{}|".format(getS(y))
        for x in range(0, noOfPoints):
            output += "{}|".format(getS(distances[y][x]))
        output += "\n"
        output = drawBorder(output)

    print(output)
