init = 130254
end = 678275

totals = 0


def validate(list):
    duplicate = {}
    for index in range(0, len(list)-1):
        if list[index] == list[index+1]:
            key = list[index]
            if key in duplicate.keys():
                duplicate[key] = duplicate[key]+1
            else:
                duplicate[key] = 1
        elif list[index] > list[index+1]:
            return False
    return 1 in duplicate.values()


while init < end:
    list = []
    for d in map(int, str(init)):
        list.append(d)

    if validate(list):
        totals += 1
    init += 1
print(totals)
