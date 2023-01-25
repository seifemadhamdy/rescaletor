import math


def scale(screenDimension):
    scaledScreenDimension = screenDimension * (i / 100)
    return scaledScreenDimension - (scaledScreenDimension % 2)


screenWidth = int(input("Enter your screen's width: "))
screenHeight = int(input("Enter your screen's height: "))

for i in range(100, -5, -5):
    if i < 100 and i > 0:
        print(
            str(i)
            + "% Render scale is "
            + str(int(scale(screenWidth)))
            + " x "
            + str(int(scale(screenHeight)))
        )
        
