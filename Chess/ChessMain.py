""""
This is the driver file. Responsible for handling user input and displaying current GameState object.
"""

import pygame as p
from Chess import ChessEngine

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
    loadImages() #only once, before while loop
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
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

def drawBoard(screen):
    colors = [p.Color("white"), p.Color("grey")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c) % 2)]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
'''
Draw the pieces on the board using the current GameState.board
'''
def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

if __name__ == "__main__":
    main()




