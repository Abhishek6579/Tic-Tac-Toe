winPositions = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)
  ]

COL = {
	0 : 0,
	1 : 1,
	2 : 2,
 	3 : 0,
	4 : 1,
	5 : 2,
 	6 : 0,
	7 : 1,
	8 : 2,  
}

ROW = {
	0 : 0,
	1 : 0,
	2 : 0,
 	3 : 1,
	4 : 1,
	5 : 1,
 	6 : 2,
	7 : 2,
	8 : 2, 
}

def checkWinnerDinner(gameState, computer):
    for winPosition in winPositions:
        if gameState[winPosition[0]] == gameState[winPosition[1]] and gameState[winPosition[1]] == gameState[winPosition[2]] and gameState[winPosition[1]] != -1 :
            if gameState[winPosition[1]] == computer:
                return True
            else:
                return True
    return False


rowWinPosition = [(0, 1, 2), (3, 4, 5), (6, 7, 8)]
def checkWinnerGetRow(gameState, player):
    for winPosition in rowWinPosition:
        if gameState[winPosition[0]] == gameState[winPosition[1]] and gameState[winPosition[1]] == gameState[winPosition[2]] and gameState[winPosition[1]] == player :
            return ROW[winPosition[0]]
    return -1

colWinPosition = [(0, 3, 6), (1, 4, 7), (2, 5, 8)]
def checkWinnerGetColumn(gameState, player):
    for winPosition in colWinPosition:
        if gameState[winPosition[0]] == gameState[winPosition[1]] and gameState[winPosition[1]] == gameState[winPosition[2]] and gameState[winPosition[1]] == player :
            return COL[winPosition[0]]
    return -1

diagonal = [(0, 4, 8), (2, 4, 6)]
def checkWinnerGetDiag(gameState, player):
    for winPosition in diagonal:
        if gameState[winPosition[0]] == gameState[winPosition[1]] and gameState[winPosition[1]] == gameState[winPosition[2]] and gameState[winPosition[1]] == player :
            return winPosition[0]
    return -1



rowWinPosition = [(0, 1, 2), (3, 4, 5), (6, 7, 8)]
def checkWinnerGetRowWin(gameState, player):
    for winPosition in rowWinPosition:
        if gameState[winPosition[0]] == gameState[winPosition[1]] and gameState[winPosition[1]] == gameState[winPosition[2]] and gameState[winPosition[1]] == player :
            return True
    return False

colWinPosition = [(0, 3, 6), (1, 4, 7), (2, 5, 8)]
def checkWinnerGetColumnWin(gameState, player):
    for winPosition in colWinPosition:
        if gameState[winPosition[0]] == gameState[winPosition[1]] and gameState[winPosition[1]] == gameState[winPosition[2]] and gameState[winPosition[1]] == player :
            return True
    return False

diagonal = [(0, 4, 8), (2, 4, 6)]
def checkWinnerDiagWin(gameState, player):
    for winPosition in diagonal:
        if gameState[winPosition[0]] == gameState[winPosition[1]] and gameState[winPosition[1]] == gameState[winPosition[2]] and gameState[winPosition[1]] == player :
            return True
    return False