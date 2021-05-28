from Probability import canWin
obj = 0
__setOfConnected = [
    (0, 1, 2, 3, 6),
    (1, 0, 2, 4, 7),
    (2, 0, 1, 5, 8),
    (3, 0, 4, 5, 6),
    (4, 1, 3, 5, 7),
    (5, 2, 3, 4, 8),
    (6, 0, 3, 7, 8),
    (7, 1, 4, 6, 8),
    (8, 2, 5, 6, 7)
  ]

def connected(gameState1, move, opponent):
    noOfConnected = 0
    for arr in __setOfConnected:
        if arr[0] != move:
            continue
        else:
            for i in arr:
                if gameState1[i] != opponent:
                    noOfConnected += 1
            if move % 2 == 0 and gameState1[4] != opponent:
                return noOfConnected
            else:
                return noOfConnected-1
    return -1

def position(arr, computer, player, move, noOfMovesPlayed, possibleMovesToBePlayed):
    objComp = computer
    objPlay = player
    gameState = arr.copy()
    gameState[move] = computer  # Computer makes The Given Move
    noOfMoves = noOfMovesPlayed + 1

    while noOfMoves <= 9 :
        temp = computer
        computer = player
        player = temp
        playMove(gameState,computer,player, possibleMovesToBePlayed, noOfMovesPlayed)
        if checkWinner(gameState, player):
            return -1
        noOfMoves += 1

    computer = objComp
    player = objPlay
    if checkWinner(gameState,player):
        return -1
    else:
        return 0



# Private
def playMove(gameState1,moveToMake, opponent , possibleMovesToBePlayed, noOfMovesPlayed):
    bestMove = 0
    computerMoveIndex = canWin(gameState1,moveToMake,)
    playerMoveIndex = canWin(gameState1,opponent)
    if gameState1[4] == -1:
        gameState1[4] = moveToMake
        return
    else:
        if (computerMoveIndex != -1 or playerMoveIndex != -1):
            if(computerMoveIndex != -1):
                gameState1[computerMoveIndex] = moveToMake
                return

            else:
                gameState1[playerMoveIndex] = moveToMake
                return
        else:
            if moveToMake == 1:
                j = 0
                j2 = 0
                for i in possibleMovesToBePlayed:
                    j = connected(gameState1,i,opponent)
                    if j >= 4:
                        gameState1[i]  = moveToMake
                        return
                    else:
                        if j >= j2:
                            bestMove = j
                            j2 = j
                gameState1[i]  = moveToMake
                return
            # else:
            #     for i in possibleMovesToBePlayed:
            #         j = connected(gameState1,i,opponent)
            #         if j > 4:
            #             gameState1[i]  = moveToMake
            #             return
            #         else:
            #             if position(arr = gameState1,computer = moveToMake,player = opponent,move = i, noOfMovesPlayed=noOfMovesPlayed, possibleMovesToBePlayed=possibleMovesToBePlayed) != -1:
            #                 gameState1[i]  = moveToMake
            #                 return                          
            #             else:
            #                 continue


winPositions = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)
  ]
def checkWinner(gameState, player):
    for winPosition in winPositions:
        if gameState[winPosition[0]] == gameState[winPosition[1]] and gameState[winPosition[1]] == gameState[winPosition[2]] and gameState[winPosition[1]] == player :
            return True
    return False
