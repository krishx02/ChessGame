""""
This is the driver file. Responsible for handling user input and displaying current GameState object.
"""

import pygame as p
from Chess import ChessEngine
#This is the creation of the board itself. Fps, dimension of the board and fps
WIDTH = HEIGHT = 512 #resolution
DIMENSION = 8 #chess board is 8x8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15 #animation
IMAGES = {}


'''
Initialize a global dictionary of images. Loading it once only b/c its expensive. 
'''
def loadImages():
    pieces = ['wp', 'wN', 'wR', 'wK', 'wQ', 'wB', 'bp', 'bN', 'bR', 'bK', 'bQ', 'bB']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))
    #can access an image by saying 'IMAGES['wp']'
'''
The driver for code. Handles user input and updates the graphics. 
'''

def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    validMoves = gs.getValidMoves()
    moveMade = False
    #Lodes in all of the images.
    loadImages() #only once, before while loop
    running = True
    sqSelected = () #no square initially. Keep track of last square the user had selected.
    playerClicks = [] # 0,1,2. Keep track of player clicks.
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            #mouse stuff
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos() #(x,y location of the mouse)
                col = location[0]//SQ_SIZE
                row = location[1]//SQ_SIZE
                if sqSelected == (row, col): #user clicked the same square twice
                    sqSelected = () #empties the square selected
                    playerClicks = [] #clears player clicks
                else:
                    sqSelected = (row, col)
                    playerClicks.append(sqSelected) #append for 1st and 2nd click
                if len(playerClicks) == 2: #after second click
                    move = ChessEngine.Move(playerClicks[0], playerClicks[1], gs.board)
                    print(move.getChessNotation())
                    if move in validMoves:
                        gs.makeMove(move)
                        moveMade = True
                        sqSelected = () #reset
                        playerClicks = []
                    else:
                        playerClicks = [sqSelected]
            #key handler
            elif e.type == p.KEYDOWN:
                if e.key == p.K_z:
                    gs.undoMove()
                    moveMade = True
        if moveMade:
            validMoves = gs.getValidMoves()
            moveMade = False

        drawGameState(screen,gs)
        clock.tick(MAX_FPS)
        p.display.flip()

'''
Responsible for all graphics for the game state 
'''

def drawGameState(screen, gs):
    drawBoard(screen) #draw squares on the voard
    #can add highlighting later
    drawPieces(screen, gs.board) #draw pieces on top of squares
#Function name says it all. You can change the color if you want, but if you have a black background it won't look good, hence grey.
def drawBoard(screen):
    colors = [p.Color("white"), p.Color("grey")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c) % 2)]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
'''
Draw the pieces on the board using the current GameState.board
'''
#puts all of the pieces in their original place from the ChessEngine class.
def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

if __name__ == "__main__":
    main()




