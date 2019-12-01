import math


mass = open('puzzleInput.txt', 'r')

fuelConsumption = 0

for piece in mass:
    piece = int(piece)
    pieceFuel = math.floor(piece / 3) - 2
    fuelConsumption += pieceFuel


print(fuelConsumption)
