""""
Class is responsible for storing all of the information about the current state of the chess game.
Also be responsible for determining the valid moves at the current state. Also keep a move log.
"""
class GameState():
    def __init__(self):
        #Its a 2d 8x8 list. each element of the list has 2 characters. The first character represents the color of the
        #piece. Second character represents the type of the piece. King, Queen, Rook, Bishop, Knight, Pawn.
        # "--" this represents an empty space with no piece.
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]
        self.whiteToMove  = True
        self.moveLog = []

