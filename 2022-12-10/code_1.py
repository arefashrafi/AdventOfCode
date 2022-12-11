import numpy as np

rawlines = open('input.txt').readlines()
lines = [line.strip().split(' ') for line in rawlines]
value_count: int = 1
cycle_count: int = 0
check_on = [20, 60, 100, 140, 180, 220]
screen = ['.' for i in range(240)]

sprite_position = 0
sum_check_values = 0
for line in lines:
    op = line[0]
    op_cost = 1
    value = 0
    if op == "addx":
        op_cost = 2
    if len(line) > 1:
        value = int(line[1])
    for _ in range(op_cost):
        cycle_count += 1
        if sprite_position + 3 > cycle_count % 40 >= sprite_position:
            screen[cycle_count-1] = '#'

        if cycle_count in check_on:
            sum_check_values += cycle_count * value_count
    if "addx" in op:
        value_count += value
        sprite_position = value_count

print('\n'.join([' '.join([str(cell) for cell in row])
                 for row in np.reshape(screen, (-6, 40))]))

print(sum_check_values)
