import math

mass = open('puzzleInput.txt', 'r')


fuelConsumption = 0


def calcFuel(fuelMass):
    if math.floor(fuelMass / 3) - 2 <= 0:
        return 0
    else:
        fuelMass = math.floor(fuelMass / 3) - 2
        # print(fuelMass)
        fuelMassTotal = fuelMass + calcFuel(fuelMass)
        return fuelMassTotal


for piece in mass:
    piece = int(piece)
    pieceFuel = math.floor(piece / 3) - 2
    fuelConsumption += pieceFuel + calcFuel(pieceFuel)

print(fuelConsumption)
