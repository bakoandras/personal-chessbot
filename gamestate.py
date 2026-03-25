class GameState():
    def __init__(self):
        self.board = [
            ["bR","bN","bB","bQ","bK","bB","bN","bR"],
            ["bP","bP","bP","bP","bP","bP","bP","bP"],
            ["__","__","__","__","__","__","__","__"],
            ["__","__","__","__","__","__","__","__"],
            ["__","__","__","__","__","__","__","__"],
            ["__","__","__","__","__","__","__","__"],
            ["wP","wP","wP","wP","wP","wP","wP","wP"],
            ["wR","wN","wB","wQ","wK","wB","wN","wR"]
        ]
        self.whiteToMove = True
        self.moveLog = []

    def makeMove(self, move:Move):
        self.board[move.startRow][move.startCol] = "__"
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.whiteToMove = not self.whiteToMove

    def getPawnMoves(self, r, c, moves):
        if self.whiteToMove:
            if self.board[r - 1][c] == "__":
                moves.append(Move((r, c), (r - 1, c), self.board))
                if r == 6 and self.board[r - 2][c] == "__":
                    moves.append(Move((r, c), (r - 2, c), self.board))

            if c - 1 >= 0:
                if self.board[r - 1][c - 1] != "__" and self.board[r - 1][c - 1][0] != "w":
                    moves.append(Move((r, c), (r - 1, c - 1), self.board))

            if c + 1 <= 7:
                if self.board[r - 1][c + 1] != "__" and self.board[r - 1][c + 1][0] != "w":
                    moves.append(Move((r, c), (r - 1, c + 1), self.board))
        else:
            if self.board[r + 1][c] == "__":
                moves.append(Move((r, c), (r + 1, c), self.board))
                if r == 1 and self.board[r + 2][c] == "__":
                    moves.append(Move((r, c), (r + 2, c), self.board))

            if c - 1 >= 0:
                if self.board[r + 1][c - 1] != "__":
                    moves.append(Move((r, c), (r + 1, c - 1), self.board))

            if c + 1 <= 7:
                if self.board[r + 1][c + 1] != "__":
                    moves.append(Move((r, c), (r + 1, c + 1), self.board))

    def getKnightMoves(self, r, c, moves):
        knight_moves = [
            (1, 2),(1, -2),(-1, 2),(-1, -2),
            (2, 1),(2, -1),(-2, 1),(-2, -1)
        ]

        allyColor = "w" if self.whiteToMove else "b"

        for move in knight_moves:
            endRow = r + move[0]
            endCol = c + move[1]

            if 0 <= endRow < 8 and 0 <= endCol < 8:
                endPiece = self.board[endRow][endCol]
                if endPiece[0] != allyColor:
                    moves.append(Move((r, c), (endRow, endCol), self.board))

    def getKingMoves(self, r, c, moves):
        kingMoves = [
            (1, 0),(-1, 0),(0, 1),(0, -1),
            (1, 1),(-1, 1),(1, -1),(-1, -1)
        ]

        allyColor = "w" if self.whiteToMove else "b"

        for i in range(8):
            endRow = r + kingMoves[i][0]
            endCol = c + kingMoves[i][1]

            if 0 <= endRow < 8 and 0 <= endCol < 8:
                endPiece = self.board[endRow][endCol]
                if endPiece[0] != allyColor:
                    moves.append(Move((r, c), (endRow, endCol), self.board))

    def getValidMoves(self):
        moves = []
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                turn = self.board[r][c][0]
                if (turn == 'w' and self.whiteToMove) or (turn == 'b' and not self.whiteToMove):
                    piece = self.board[r][c][1]
                    if piece == 'P':
                        self.getPawnMoves(r, c, moves)
                    #elif piece == 'R':
                        #self.getRookMoves(r, c, moves)
                    elif piece == 'N':
                        self.getKnightMoves(r, c, moves)
                    #elif piece == 'B':
                        #self.getBishopMoves(r, c, moves)
                    #elif piece == 'Q':
                        #self.getQueenMoves(r, c, moves)
                    elif piece == 'K':
                        self.getKingMoves(r, c, moves)

        return moves

class Move():
    def __init__(self, startSq, endSq, board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]

    def __eq__(self, other):
        if isinstance(other, Move):
            return (self.startRow == other.startRow and 
                    self.startCol == other.startCol and 
                    self.endRow == other.endRow and 
                    self.endCol == other.endCol)
        return False
