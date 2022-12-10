
import math
from time import sleep
import numpy as np


direction = {
    'U': (0, 1),
    'D': (0, -1),
    'L': (-1, 0),
    'R': (1, 0),
}


def main():
    lines = open('input.txt').readlines()
    h_loc = (0, 0)
    t_loc = (0, 0)
    body_loc = [(0, 0) for _ in range(8)]
    tail_positions = {t_loc}
    for line in lines:
        move = line.strip().split(' ')[0]
        steps = line.strip().split(' ')[1]
        movement = np.array(direction[move])
        for _ in range(int(steps)):
            h_loc = (h_loc[0] + movement[0], h_loc[1] + movement[1])
            prev_location = h_loc
            for i in range(8):
                if math.dist(prev_location, body_loc[i]) >= 2:
                    distance = np.subtract(prev_location, body_loc[i])
                    b_loc = tuple(np.add(body_loc[i], np.sign(distance)))
                    body_loc[i] = b_loc
                prev_location = body_loc[i]

            if math.dist(prev_location, t_loc) >= 2:
                distance = np.subtract(prev_location, t_loc)
                t_loc = tuple(np.add(t_loc, np.sign(distance)))
                tail_positions.add(t_loc)
    print(len(body_loc))
    print(len(tail_positions))


main()
