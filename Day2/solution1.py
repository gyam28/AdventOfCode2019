
list = open('puzzleInput.txt', 'r').read()
list = list.split(',')

input = []
for e in list:
    input.append(int(e))

print(input)


head = 0
inputA = 0
inputB = 0
output = 0

while input[head] == 1 or input[head] == 2:
    positionA = input[head+1]
    inputA = input[positionA]

    inputB = input[input[head+2]]

    result = 0
    if input[head] == 1:
        result = inputA + inputB
    else:
        result = inputA * inputB

    positionOutput = input[head+3]
    input[positionOutput] = result
    head += 4

if input[head] == 99:
    print('correct end of execution')
    print(input[0])
else:
    print('theres an error')
