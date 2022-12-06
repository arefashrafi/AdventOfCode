line = open('input.txt').readline()
set_table = []
data = list(line)
for index, char in enumerate(data):
    set_table.extend(char)
    if (len(set_table) > 14):
        set_table.pop(0)
    if (len(set_table) == 14 and len(set_table) == len(set(set_table))):
        print(index+1)
        break
