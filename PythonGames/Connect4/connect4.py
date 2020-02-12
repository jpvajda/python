import sys
import numpy as np
import pygame
import math 

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

ROW_COUNT = 6
COLUMN_COUNT = 7


#creates boards
def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board
 
#drops piece into board
def drop_piece(board, row, col, piece):
    board[row][col] = piece

# checks location validity
def is_valid_location(board, col):
    return board[ROW_COUNT -1][col] == 0

#gets next open row
def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

#prints board
def print_board(board):
    print(np.flip(board, 0))


def winning_move(board, piece):
  # checks horizontal locations for win
    for c in range(COLUMN_COUNT -3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2]\
             == piece and board[r][c+3] == piece:
                return True

  #checks vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT -3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2]\
            [c] == piece and board[r+3][c] == piece:
                return True

  # check for positively sloped diagonal
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT -3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2]\
            == piece and board[r+3][c+3] == piece:
                return True

  # check for negatively sloped diagonal
    for c in range(COLUMN_COUNT):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2]\
            == piece and board[r-3][c+3] == piece:
                return True

  # draws board         
def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZ+SQUARESIZE/2)), RADIUS)
            elif board[r][c] == 2: 
                pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS) 
    pygame.display.update()

# Main Game Loop
board = create_board()
print_board(board)
game_over = False
turn = 0

pygame.init()

SQUARESIZE = 100
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE

size = (width, height)

RADIUS = int(SQUARESIZE/2 -5)

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
                          
        if event.type == pygame.MOUSEBUTTONDOWN:
            #print(event.pos)
            # pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
        #Ask for Player 1 Input
            if turn == 0:
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)   
                    drop_piece(board, row, col, 1)

                    if winning_move(board, 1):
                        print("PLAYER 1 WINS!!!!")
                        game_over = True
        #Ask for Player 2 Input
            else:
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 2)

        print_board(board)
        draw_board(board)
      
        turn += 1
        turn = turn % 2
      