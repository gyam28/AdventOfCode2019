from itertools import permutations

list = open('puzzleInput.txt', 'r').read().split(',')
instruction = [int(x) for x in list]


def inCode(instruction, codeInput):

    head = 0
    inputA = 0
    inputB = 0
    output = []

    while instruction[head] != 99:
        headInfo = str(instruction[head])
        opCodeList = [ch for ch in headInfo]
        while len(opCodeList) < 4:
            opCodeList.insert(0, '0')

        opCode = int(''.join(opCodeList[-2:]))

        positionA = instruction[head+1]
        inputA = positionA if int(
            opCodeList[1]) == 1 else instruction[positionA]
        step = 0

        result = 0

        if opCode == 1:
            step = 4
            inputB = instruction[head + 2] if int(
                opCodeList[0]) == 1 else instruction[instruction[head+2]]
            result = inputA + inputB
            positionOutput = instruction[head+3]
            instruction[positionOutput] = result
        elif opCode == 2:
            step = 4
            positionB = instruction[head+2]
            inputB = positionB if int(
                opCodeList[0]) == 1 else instruction[positionB]
            result = inputA * inputB
            positionOutput = instruction[head+3]
            instruction[positionOutput] = result
        elif opCode == 3:
            step = 2
            instruction[positionA] = codeInput.pop(0)
        elif opCode == 4:
            step = 2
            output.append(inputA)
        elif opCode == 5:
            step = 3
            if inputA != 0:
                positionB = instruction[head+2]
                inputB = positionB if int(
                    opCodeList[0]) == 1 else instruction[positionB]
                head = inputB
                step = -1
        elif opCode == 6:
            step = 3
            if inputA == 0:
                positionB = instruction[head+2]
                inputB = positionB if int(
                    opCodeList[0]) == 1 else instruction[positionB]
                head = inputB
                step = -1
        elif opCode == 7:
            step = 4
            positionOutput = instruction[head+3]
            inputB = instruction[head + 2] if int(
                opCodeList[0]) == 1 else instruction[instruction[head+2]]
            if inputA < inputB:
                instruction[positionOutput] = 1
            else:
                instruction[positionOutput] = 0
        elif opCode == 8:
            step = 4
            positionOutput = instruction[head+3]
            inputB = instruction[head + 2] if int(
                opCodeList[0]) == 1 else instruction[instruction[head+2]]
            if inputA == inputB:
                instruction[positionOutput] = 1
            else:
                instruction[positionOutput] = 0

        if step != -1:
            head += step

    if instruction[head] == 99:
        print('correct end of execution')
    else:
        print('theres an error')

    return output


modes = [5, 6, 7, 8, 9]
perm = permutations(modes)

outputs = []
for mode in perm:

    inputs = 0
    for i in range(0, 5):
        inputs = inCode(instruction, [mode[i], inputs])[0]
    outputs.append(inputs)


print(max(outputs))
