def main():
    lines = open('input').readlines()
    intersected_assignments, no_intersection = 0, 0
    for line in lines:
        value = line.strip().split(',')
        a = set(get_range(value[0]))
        b = set(get_range(value[1]))
        if ((a | b) == a or (a | b) == b):
            intersected_assignments += 1
        elif ((a & b) == set()):
            no_intersection += 1
    print(intersected_assignments)
    print(len(lines) - no_intersection)


def get_range(range_string):
    range_array = range_string.split('-')
    start, end = range_array[0], range_array[1]
    return [*range(int(start), int(end) + 1, 1)]


main()
