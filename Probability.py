winningPositions = [
    (0, 1, 2), (0, 2, 1), (1, 2, 0), (3, 4, 5), (4, 5, 3), (3, 5, 4), (6, 7, 8), (7, 8, 6),
    (6, 8, 7), (0, 6, 3), (0, 3, 6), (3, 6, 0), (1, 4, 7), (4, 7, 1), (1, 7, 4), (2, 5, 8),
    (5, 8, 2), (2, 8, 5), (0, 4, 8), (0, 8, 4), (4, 8, 0), (2, 4, 6), (2, 6, 4), (6, 4, 2)
]

def canWin(gameState, player):
    for winningPosition in winningPositions:
        if  ((gameState[winningPosition[0]] == gameState[winningPosition[1]]) and gameState[winningPosition[2]] == -1  and gameState[winningPosition[0]] == player):
            return winningPosition[2]

    return -1

