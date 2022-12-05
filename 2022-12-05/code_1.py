import re


def main():
    # Part 1
    with open('input.txt') as f:
        lines = f.readlines()
        table = get_table_structure(lines[:9])
        for line in lines[10:]:
            task = re.findall(r'\b\d+\b', line)
            fromIndex = int(task[1]) - 1
            amountIndex = int(task[0])
            toIndex = int(task[2]) - 1
            take = table[fromIndex][::-1][:amountIndex]
            for _ in range(0, amountIndex):
                table[fromIndex].pop()
            table[toIndex].extend(take)
        print_result(table)
    f.close()

    # Part 2
    with open('input.txt') as f:
        lines = f.readlines()
        table = get_table_structure(lines[:9])
        for line in lines[10:]:
            task = re.findall(r'\b\d+\b', line)
            fromIndex = int(task[1]) - 1
            amountIndex = int(task[0])
            toIndex = int(task[2]) - 1
            take = table[fromIndex][::-1][:amountIndex]
            for _ in range(0, amountIndex):
                table[fromIndex].pop()
            table[toIndex].extend(take[::-1])
        print_result(table)
    f.close()


def get_table_structure(structure: list):
    table: list = [''] * len(structure)
    for index in range(0, len(structure)):
        result = [x.replace('    ', ' ').split(' ')[index].strip()
                  for x in structure[::-1] if x.replace('    ', ' ').split(' ')[index].strip()]
        table[index] = result
    return table


def print_result(table: list):
    print([x[-1] for x in table])


main()
