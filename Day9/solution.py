list = open('puzzleInput.txt', 'r').read().split(',')
instruction = [int(x) for x in list]


class Memory:
    def __init__(self, input):
        self.memory = dict()
        for index in range(0, len(input)):
            self.memory[index] = input[index]

    def get(self, position):
        if position not in self.memory.keys():
            self.memory[position] = 0

        return self.memory[position]

    def set(self, position, value):
        self.memory[position] = value


class Intcode:
    def __init__(self, input):
        self.memory = Memory(input)
        self.head = 0
        self.relativeBase = 0
        self.output = []

    def getParam(self, opCode, paramCount, hasOutput):
        params = []
        for el in range(self.head, self.head + paramCount):
            value = self.memory.get(el)
            power = el-self.head + 2
            div = pow(10, power)

            mode = int((opCode / div) % 10)
            if mode == 0:
                params.append(value) if hasOutput and (
                    (el - self.head) == (paramCount-1)) else params.append(self.memory.get(value))
            elif mode == 1:
                params.append(value)
            elif mode == 2:
                params.append(self.relativeBase + value) if hasOutput and (
                    (el - self.head) == (paramCount-1)) else params.append(self.memory.get(value+self.relativeBase))

        return params

    def execute(self, input):
        self.head = 0
        self.output = []

        while self.memory.get(self.head) != 99:
            opCode = self.memory.get(self.head)
            self.head += 1
            step = 3

            result = 0

            if opCode % 100 == 1:
                params = self.getParam(opCode, 3, True)
                result = params[0] + params[1]
                self.memory.set(params[2], result)
            elif opCode % 100 == 2:
                params = self.getParam(opCode, 3, True)
                result = params[0] * params[1]
                self.memory.set(params[2], result)
            elif opCode % 100 == 3:
                params = self.getParam(opCode, 1, True)
                step = 1
                self.memory.set(params[0], input.pop(0))
            elif opCode % 100 == 4:
                params = self.getParam(opCode, 1, True)
                step = 1

                self.output.append(self.memory.get(params[0]))
            elif opCode % 100 == 5:
                params = self.getParam(opCode, 2, False)
                step = 2
                if params[0] != 0:
                    self.head = params[1]
                    step = -1
            elif opCode % 100 == 6:
                params = self.getParam(opCode, 2, False)
                step = 2
                if params[0] == 0:
                    self.head = params[1]
                    step = -1
            elif opCode % 100 == 7:
                params = self.getParam(opCode, 3, True)
                if params[0] < params[1]:
                    self.memory.set(params[2], 1)
                else:
                    self.memory.set(params[2], 0)
            elif opCode % 100 == 8:
                params = self.getParam(opCode, 3, True)
                if params[0] == params[1]:
                    self.memory.set(params[2], 1)
                else:
                    self.memory.set(params[2], 0)
            elif opCode % 100 == 9:
                step = 1
                params = self.getParam(opCode, 1, False)
                self.relativeBase += params[0]

            if step != -1:
                self.head += step
        return self.output


machine = Intcode(instruction)
print(machine.execute([1]))
print(machine.execute([2]))
