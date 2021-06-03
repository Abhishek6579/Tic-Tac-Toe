from WinnerWinnerChickenDinner import *
import pygame
from Bot import *
from WinnerWinnerChickenDinner import checkWinnerDinner
pygame.init()

# ---------
# CONSTANTS
# ---------
WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
WIN_LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = 200
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 55
# rgb: red green blue
RED = (255, 0, 0)
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)
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



gameState = [-1,-1,-1,-1,-1,-1,-1,-1,-1]
possibleMoves = [0,1,2,3,4,5,6,7,8]
whoseMove = 1
nod = 0

# ------
# SCREEN
# ------
screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption( 'TIC TAC TOE' )
screen.fill( BG_COLOR )

# Game Over
# over_font = pygame.font.Font('freesansbold.ttf', 64)

# ---------
# FUNCTIONS
# ---------
def draw_lines():
	# 1 horizontall̥
	pygame.draw.line( screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH )
	# 2 horizontal
	pygame.draw.line( screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH )

	# 1 vertical
	pygame.draw.line( screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH )
	# 2 vertical
	pygame.draw.line( screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH )

# def game_over_text(int):
# 	if int == 1:
# 		over_text = over_font.render("Over !!", True, (255, 0, 0))
# 		screen.blit(over_text, (200, 250))
# 	else:
# 		over_text = over_font.render("Draw !!", True, (255, 0, 0))
# 		screen.blit(over_text, (200, 250))

def draw_figures():
	for i in range(0,9):
		if gameState[i] == 0:
			pygame.draw.circle( screen, CIRCLE_COLOR, (int( COL[i] * SQUARE_SIZE + SQUARE_SIZE//2 ), int( ROW[i] * SQUARE_SIZE + SQUARE_SIZE//2 )), CIRCLE_RADIUS, CIRCLE_WIDTH )
		else:
			if gameState[i] == 1:
				pygame.draw.line( screen, CROSS_COLOR, (COL[i] * SQUARE_SIZE + SPACE, ROW[i] * SQUARE_SIZE + SQUARE_SIZE - SPACE), (COL[i] * SQUARE_SIZE + SQUARE_SIZE - SPACE, ROW[i] * SQUARE_SIZE + SPACE), CROSS_WIDTH )
				pygame.draw.line( screen, CROSS_COLOR, (COL[i] * SQUARE_SIZE + SPACE, ROW[i] * SQUARE_SIZE + SPACE), (COL[i] * SQUARE_SIZE + SQUARE_SIZE - SPACE, ROW[i] * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH )

	return

def getPositionalBlock(tuple_location):
	if tuple_location[1] >= 2 and tuple_location[1] <= 190:
		if tuple_location[0] >=2 and tuple_location[0] <=188:
			return 0
		elif tuple_location[0] >=200 and tuple_location[0] <=386:
			return 1
		else:
			return 2
	elif tuple_location[1] >= 200 and tuple_location[1] <= 380:
		if tuple_location[0] >=2 and tuple_location[0] <=188:
			return 3
		elif tuple_location[0] >=200 and tuple_location[0] <=386:
			return 4
		else:
			return 5
	else:
		if tuple_location[0] >=2 and tuple_location[0] <=188:
			return 6
		elif tuple_location[0] >=200 and tuple_location[0] <=386:
			return 7
		else:
			return 8
	return


def draw_horizontal_winning_line(row, player):
	posY = row * SQUARE_SIZE + SQUARE_SIZE//2

	if player == 0:
		color = CIRCLE_COLOR
	elif player == 1:
		color = CROSS_COLOR

	pygame.draw.line( screen, color, (15, posY), (WIDTH - 15, posY), WIN_LINE_WIDTH )

def draw_vertical_winning_line(col, player):
	posX = col * SQUARE_SIZE + SQUARE_SIZE//2

	if player == 0:
		color = CIRCLE_COLOR
	elif player == 1:
		color = CROSS_COLOR

	pygame.draw.line( screen, color, (posX, 15), (posX, HEIGHT - 15), WIN_LINE_WIDTH )


def draw_asc_diagonal(player):
	if player == 0:
		color = CIRCLE_COLOR
	elif player == 1:
		color = CROSS_COLOR

	pygame.draw.line( screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), WIN_LINE_WIDTH )

def draw_desc_diagonal(player):
	if player == 0:
		color = CIRCLE_COLOR
	elif player == 1:
		color = CROSS_COLOR

	pygame.draw.line( screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), WIN_LINE_WIDTH )
    
    

def check_win(player):
	# vertical win check

	if checkWinnerGetRowWin(gameState, player):
		draw_horizontal_winning_line((checkWinnerGetRow(gameState, player)), player)
		return True

	# horizontal win check

	if checkWinnerGetColumnWin(gameState, player):
		draw_vertical_winning_line((checkWinnerGetColumn(gameState, player)), player)
		return True
		

	# asc diagonal win check
	if checkWinnerDiagWin(gameState, player):
		if checkWinnerGetDiag(gameState, player) == 0:
			draw_desc_diagonal(player)
			return True
		else:
			draw_asc_diagonal(player)
			return True



ctr = 0
player = random.randint(1,1000)
computer = 0
whoseMove2 = 0
if player % 2 == 0:
	computer = 1
	player = 0
else:
	computer = 0
	player = 1
computer = 0 # Testing
player = 1 # Testing
draw_lines()
running = True
while running:
	pygame.display.update()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
				running = False
				continue
		# Player first
		if player == 1:
			if nod >= 9:
				ctr+=1
				continue
			else:
				if not checkWinnerDinner(gameState = gameState, computer = 0):
					
					if event.type == pygame.MOUSEBUTTONDOWN and whoseMove == 1:
						position = getPositionalBlock(pygame.mouse.get_pos())
						try:
							possibleMoves.remove(position)
							gameState[position] = 1
							nod += 1
						except:							
							continue
						whoseMove = 0
					elif  whoseMove == 0:
						playMove(gameState,moveToMake= computer, opponent = player, possibleMovesToBePlayed=possibleMoves, noOfMovesPlayed = nod)
						whoseMove  = 1
						nod+=1
		else:
			if nod >= 9:
				ctr+=1
				continue
			else:
				if not checkWinnerDinner(gameState = gameState, computer = computer):
					
					if event.type == pygame.MOUSEBUTTONDOWN and whoseMove2 == 1:
						position = getPositionalBlock(pygame.mouse.get_pos())
		
						try:
							possibleMoves.remove(position)
							gameState[position] = player
							nod+=1
						except:
							# print("Dont cheat!!")
							continue
						whoseMove2 = 0
					elif  whoseMove2 == 0:
						# print(gameState)
						playMove(gameState,moveToMake = computer, opponent = player, possibleMovesToBePlayed=possibleMoves, noOfMovesPlayed = nod)
						whoseMove2  = 1
						nod+=1

		
				
		
	draw_figures()
	check_win(0)
	check_win(1)

