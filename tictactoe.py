import pygame,sys
import numpy as np

pygame.init()

L=660
B=L
BG_PURP=(189,140,195)
L_PURP=(167,88,162)
CIRCLE_COLOR=(233,219,232)
CROSS_COLOR=(131,55,127)
CROSS_WIDTH = 25
SPACE = 55

scr=pygame.display.set_mode((L,B))
pygame.display.set_caption("Let's play TIC TAC TOE !!!")
scr.fill(BG_PURP)

#console board
brd=np.zeros((3,3))


def place_marker(row, col, player):
	brd[row][col] = player

def available_square(row, col):
	return brd[row][col] == 0

def fullboard_check():
	for r in range(3):
		for c in range(3):
			if brd[r][c] == 0:
				return False

	return True
def draw_marks():
	for r in range(3):
		for c in range(3):
			if brd[r][c] == 1:
				pygame.draw.circle( scr, CIRCLE_COLOR, (int( c * 220 + 220//2 ), int( r * 220 + 220//2 )), 63, 15 )
			elif brd[r][c] == 2:
				pygame.draw.line( scr, CROSS_COLOR, (c * 220 + SPACE, r * 220 + 220 - SPACE), (c * 220 + 220 - SPACE, r * 220 + SPACE), CROSS_WIDTH )	
				pygame.draw.line( scr, CROSS_COLOR, (c * 220 + SPACE, r * 220 + SPACE), (c * 220 + 220 - SPACE, r * 220 + 220 - SPACE), CROSS_WIDTH )

def check_win(player):
	# vertical win check
	for c in range(3):
		if brd[0][c] == player and brd[1][c] == player and brd[2][c] == player:
			draw_vert_line(c, player)
			return True

	# horizontal win check
	for r in range(3):
		if brd[r][0] == player and brd[r][1] == player and brd[r][2] == player:
			draw_hor_line(r, player)
			return True

	# asc diagonal win check
	if brd[2][0] == player and brd[1][1] == player and brd[0][2] == player:
		draw_dia2(player)
		return True

	# desc diagonal win chek
	if brd[0][0] == player and brd[1][1] == player and brd[2][2] == player:
		draw_dia1(player)
		return True

	return False
def draw_vert_line(col, player):
	posX = col * 220 + 220//2

	if player == 1:
		color = CIRCLE_COLOR
	elif player == 2:
		color = CROSS_COLOR

	pygame.draw.line( scr, color, (posX, 30), (posX, L - 30), 15)

def draw_hor_line(row, player):
	posY = row * 220 + 220//2

	if player == 1:
		color = CIRCLE_COLOR
	elif player == 2:
		color = CROSS_COLOR

	pygame.draw.line( scr, color, (30, posY), (L - 30, posY), 15 )

def draw_dia2(player):
	if player == 1:
		color = CIRCLE_COLOR
	elif player == 2:
		color = CROSS_COLOR

	pygame.draw.line( scr, color, (30, L - 30), (L - 30, 30), 15 )

def draw_dia1(player):
	if player == 1:
		color = CIRCLE_COLOR
	elif player == 2:
		color = CROSS_COLOR

	pygame.draw.line( scr, color, (30, 30), (L - 30, L - 30), 15 )

def restart():
	scr.fill( BG_PURP )
	drw_lines()
	for r in range(3):
		for c in range(3):
			brd[r][c] = 0

#cross lines
def drw_lines():
	pygame.draw.line(scr,L_PURP,(220,30),(220,630),10)
	pygame.draw.line(scr,L_PURP,(440,30),(440,630),10)
	pygame.draw.line(scr,L_PURP,(30,230),(630,230),10)
	pygame.draw.line(scr,L_PURP,(30,430),(630,430),10)

drw_lines()
player=1
g_over=False
while True:
	for i in pygame.event.get():
		if i.type == pygame.QUIT:
			sys.exit()
		if i.type == pygame.MOUSEBUTTONDOWN and not g_over :

			mX = i.pos[0] # x
			mY = i.pos[1] # y
			c_r = int(mY // 220)
			c_c = int(mX // 220)

			if available_square( c_r, c_c ):
				if player==1:
					place_marker(c_r,c_c,1)
					if(check_win(player)):
						g_over=True
					player=2
				elif player==2:
					place_marker(c_r,c_c,2)
					if (check_win(player)):
						g_over=True
					player=1

				draw_marks()
		if i.type == pygame.KEYDOWN:
			if i.key == pygame.K_a:
				restart()
				player = 1
				g_over = False
			

	pygame.display.update()