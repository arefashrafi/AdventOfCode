import math


def main():
    lines = open('input.txt').readlines()
    score, groupScore, divider = 0, 0, 0
    for line in lines:
        char = findDuplicate(line)
        score += calculatePriority(char)
        if (divider % 3 == 0):
            commonChar = findCommonDuplicate(lines[divider:divider + 3])
            groupScore += calculatePriority(commonChar)
        divider += 1
    print(score)
    print(groupScore)


def findCommonDuplicate(value):
    a, b, c = value[0].strip(), value[1].strip(), value[2].strip()
    elements_in_all = list(set.intersection(*map(set, [a, b, c])))
    return elements_in_all[0]


def calculatePriority(value):
    if (value.isupper()):
        return ord(value) - 65 + 27
    else:
        return ord(value) - 97 + 1


def findDuplicate(value):
    line = list(value.strip())
    i = math.ceil(len(line) / 2)
    j = i - 1
    left, right = dict({}), dict({})
    while j >= 0:
        left[line[i]] = line[i]
        right[line[j]] = line[j]
        i += 1
        j -= 1
    shared_items = {k: left[k]
                    for k in left if k in right and left[k] == right[k]}
    return list(shared_items.keys())[0]


main()
