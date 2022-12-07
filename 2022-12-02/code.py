
score_system = {
    "x": 1,
    "y": 2,
    "z": 3,
    "a": 1,
    "b": 2,
    "c": 3
}
# Part 1
lines = open('input.txt').readlines()
points = 0
for line in lines:
    opponent = line[0]
    player = line[2]
    points += score_system[player]
    scoreOfOpponent = score_system[opponent]
    scoreOfPlayer = score_system[player]
    if (scoreOfPlayer == scoreOfOpponent):  # Draw
        points += 3
    if (((scoreOfPlayer + 1) % 3) + 1 == scoreOfOpponent):  # Win
        points += 6
print(points)


# Part 2
lines = open('input.txt').readlines()
points = 0
for line in lines:
    opponent = line[0]
    scoreOfOpponent = score_system[opponent]
    gameState = line[2]
    if (gameState == 'X'):  # Lose
        player = ((scoreOfOpponent - 2) % 3) + 1
        points += player
    if (gameState == 'Y'):  # Draw
        player = scoreOfOpponent
        points += (player + 3)
    if (gameState == 'Z'):  # Win
        player = ((scoreOfOpponent + 3) % 3) + 1
        points += (player + 6)
print(points)
