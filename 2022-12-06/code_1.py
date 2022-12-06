from collections import deque
line = open('input.txt').readline()
data_list = deque([], maxlen=4)
for index, char in enumerate(line):
    data_list.append(char)
    if (len(data_list) == len(set(data_list)) == data_list.maxlen):
        print(index+1)
        break
