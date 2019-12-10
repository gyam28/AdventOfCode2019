from collections import deque

list = open('puzzleInput.txt', 'r').readlines()


def createOrbitMap(input):
    orbitMap = {}
    for e in input:

        obj = e.split(')')
        obj[1] = obj[1].replace('\n', '')

        if obj[0] not in orbitMap.keys():
            orbitMap[obj[0]] = {'parent': [], 'child': [obj[1]]}
        else:
            value = orbitMap[obj[0]]
            value['child'].append(obj[1])
            orbitMap[obj[0]] = value
        if obj[1] not in orbitMap.keys():
            orbitMap[obj[1]] = {'parent': [obj[0]], 'child': []}
        else:
            value = orbitMap[obj[1]]
            value['parent'].append(obj[0])
            orbitMap[obj[1]] = value
    return orbitMap


def orbitsTotal(orbitMap):
    counter = 0
    for item in orbitMap.keys():
        obj = orbitMap[item]
        totalOrbits = 0
        while len(obj['parent']) != 0:
            totalOrbits += 1
            obj = orbitMap[obj['parent'][0]]
        counter += totalOrbits
    return counter


finalMap = createOrbitMap(list)
# print(orbitsTotal(finalMap)) for part 1


def shortestRoute(finalMap, start, finish):
    search_queue = deque()

    search_queue += [start]
    searched = []
    path = []
    parentNode = {}
    while search_queue:
        orbit = search_queue.popleft()
        if not orbit in searched:
            path.append(orbit)
            if orbit == finish:
                searched.append(orbit)
                return searched
            else:
                newvalues = finalMap[orbit]['parent']
                newvalues.extend(finalMap[orbit]['child'])
                for v in newvalues:
                    parentNode[v] = orbit

                search_queue += newvalues
                searched.append(orbit)
                path.remove(orbit)

    return []


def getEdges(orbit):
    edges = orbit['parent']
    edges.extend(orbit['child'])
    return edges


visited = shortestRoute(finalMap, 'YOU', 'SAN')


nodes = []
value = visited.pop(-1)
while value != 'YOU':
    edges = getEdges(finalMap[value])
    possibleParent = visited.pop(-1)
    if possibleParent in edges:
        nodes.append(possibleParent)
        value = possibleParent

print(len(nodes)-2)
