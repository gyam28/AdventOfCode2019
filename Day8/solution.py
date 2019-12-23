list = open('puzzleInput.txt', 'r').read()


imgWidth = 25
imgHeight = 6

imgList = []
layerList = []
smallestZero = -1
zeros = 0
ones = 0
twos = 0
count = 0
smallestCounter = 0

for num in list:
    if len(imgList) < (imgWidth*imgHeight):
        imgList.append(num)
        if num == '0':
            zeros += 1

    elif len(imgList) == (imgWidth*imgHeight):
        layerList.append(imgList)
        imgList = [num]
        if smallestZero == -1:
            smallestZero = zeros
        if zeros < smallestZero:
            smallestZero = zeros
            smallestCounter = count
        zeros = 1 if num == 0 else 0
        count += 1

layerList.append(imgList)

if zeros < smallestZero:
    smallestZero = zeros
    smallestCounter = count

for elem in layerList[smallestCounter]:

    if elem == '1':
        ones += 1

    if elem == '2':
        twos += 1
totals = ones * twos
print(totals)

result = []
line = []
string = ''

for index in range(0, (imgHeight*imgWidth)):
    line.append('2')
    for layer in layerList:
        if layer[index] < line[index]:
            line[index] = layer[index]
            break

result.append(line)


finalRes = ''
for index in range(0, len(line)):
    if line[index] == '0':
        finalRes += ' '
    else:
        finalRes += '1'
    if index % imgWidth == 0:
        finalRes += '\n'

print(finalRes)
