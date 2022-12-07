lines = open('input.txt').readlines()
file_sizes = {}
current_directory = []
for raw in lines:
    line = raw.strip().split(' ')

    if ".." in raw:
        current_directory.pop()
    elif "$ cd /" in raw:
        current_directory = ["root"]
        file_sizes["root"] = 0
    elif not line[0].isdigit() and "$ cd " in raw and not "$ ls" in raw:
        current_directory.append('/'.join([current_directory[-1], line[-1]]))
        file_sizes[current_directory[-1]] = 0
    elif line[0].isdigit():
        for file in current_directory:
            file_sizes[file] += int(line[0])
print(file_sizes)

p1 = sum([value for name, value in file_sizes.items() if value < 100000])
print(p1)

required_size = 30000000 - (70000000 - file_sizes.get('root', 0))
p2 = min([value for name, value in file_sizes.items() if value >= required_size])
print(p2)
