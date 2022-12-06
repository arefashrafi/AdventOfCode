line = open('input.txt').readline()
data_list = []
for index, char in enumerate(line):
    data_list.append(char)
    if (len(data_list) > 4):
        data_list.pop(0)
    if (len(data_list) == len(set(data_list)) == 4):
        print(index+1)
        break
