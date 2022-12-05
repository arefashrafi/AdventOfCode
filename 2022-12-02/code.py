                             
scoresystem = { 
        "x": 1,  
        "y": 2,  
        "z": 3,
        "a": 1,
        "b": 2,
        "c": 3
    }                               
# Part 1
with open('input.txt') as f:
    lines = f.readlines()
    points = 0
    for line in lines: 
        opponent = line[0] 
        player = line[2] 
        points += scoreSystem[player]
        scoreOfOpponent = scoreSystem[opponent]
        scoreOfPlayer = scoreSystem[player]
        if(scoreOfPlayer == scoreOfOpponent): #Draw
            points += 3
        if(((scoreOfPlayer + 1) % 3) + 1 == scoreOfOpponent): #Win
            points += 6
    print(points)


# Part 2 
with open('input.txt') as f:
    lines = f.readlines()
    points = 0
    for line in lines:
        opponent = line[0]
        scoreOfOpponent = scoreSystem[opponent]
        gameState = line[2]
        if(gameState == 'X'): #Lose
          player = ((scoreOfOpponent - 2) % 3) + 1
          points += player 
        if(gameState == 'Y'): #Draw
          player = scoreOfOpponent
          points += (player + 3)
        if(gameState == 'Z'): #Win
          player = ((scoreOfOpponent + 3) % 3) + 1
          points += (player + 6)
    print(points)
