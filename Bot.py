from Evaluate import connected, position
from Probability import *
import random
bestMoves = []

def playMove(gameState,moveToMake, opponent, possibleMovesToBePlayed, noOfMovesPlayed ):
    bestMove = 0
    computerMoveIndex = canWin(gameState,moveToMake,)
    playerMoveIndex = canWin(gameState,opponent)
    if gameState[4] == -1:
        play(4,gameState,moveToMake,possibleMovesToBePlayed)
        return

    else:
        if (computerMoveIndex != -1 or playerMoveIndex != -1):
            if(computerMoveIndex != -1):
                play(computerMoveIndex,gameState,moveToMake,possibleMovesToBePlayed)
                return
            else:
                play(playerMoveIndex,gameState,moveToMake, possibleMovesToBePlayed)
                return
        else:
            if moveToMake == 1:
                j = 0
                j2 = 0
                for i in possibleMovesToBePlayed:
                    # print(possibleMovesToBePlayed) # test
                    j = connected(gameState,i,opponent)
                    if j == 5:
                        play(i,gameState,moveToMake, possibleMovesToBePlayed) 
                        return
                    else:
                        if j >= j2:
                            bestMove = i
                            j2 = j
                # print(bestMove) # test
                # print(possibleMovesToBePlayed) # test
                play(bestMove,gameState,moveToMake, possibleMovesToBePlayed) 
            else:
                for i in possibleMovesToBePlayed:
                    j = connected(gameState,i,opponent)
                    if j >= 4 :
                        if position(arr = gameState,computer = moveToMake,player = opponent,move = i, noOfMovesPlayed=noOfMovesPlayed, possibleMovesToBePlayed=possibleMovesToBePlayed) != -1:
                            play(i, gameState, moveToMake, possibleMovesToBePlayed)
                            return
                    else:
                        if position(arr = gameState,computer = moveToMake,player = opponent,move = i, noOfMovesPlayed=noOfMovesPlayed, possibleMovesToBePlayed=possibleMovesToBePlayed) != -1:
                            play(i,gameState,moveToMake, possibleMovesToBePlayed)  
                            return                          
                        else:
                            continue
                # ctr = random.randint(0,len(bestMoves)-1)
                # play(bestMoves[ctr],gameState,moveToMake, possibleMovesToBePlayed)
                
                    

                
def play(index,gameState,playThisMove, possibleMovesToBePlayed):
    gameState[index] = playThisMove
    possibleMovesToBePlayed.remove(index)

