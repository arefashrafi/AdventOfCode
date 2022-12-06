with open('input.txt') as f:
    line = f.readline()
    print(line)
    count = 0
    set_table = []
    data = list(line)
    for char in data:
        set_table.extend(char)
        if (len(set_table) > 14):
            set_table.pop(0)
        if (len(set_table) == 14 and len(set_table) == len(set(set_table))):
            print(set_table)
            print(count+1)
            break
        count += 1
