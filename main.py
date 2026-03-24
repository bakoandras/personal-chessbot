import pygame

from gamestate import GameState
from gamestate import Move
from pieces import pieceImages

WIDTH, HEIGHT = 512, 512
DIMENSION = 8
SQ_SIZE = WIDTH // DIMENSION
MAX_FPS = 15
COLOURS = [pygame.Color("coral"), pygame.Color("coral4")]
GAME_IMAGE = pygame.image.load('images/sakkicon.PNG')

IMAGES = {}

def draw_board(screen):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            colour = COLOURS[(c + r) % 2]
            pygame.draw.rect(screen, colour, pygame.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))

def main():
    pygame.init()
    screen = pygame.display.set_caption("Chess")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_icon(GAME_IMAGE)
    clock = pygame.time.Clock()
    load_images()
    gs = GameState()

    sqSelected = ()
    playerClicks = []

    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            elif e.type == pygame.MOUSEBUTTONDOWN:
                selection = pygame.mouse.get_pos()
                col = selection[0] // SQ_SIZE
                row = selection[1] // SQ_SIZE
                
                if sqSelected == (row, col):
                    sqSelected = ()
                    playerClicks = []
                else:
                    sqSelected = (row, col)
                    playerClicks.append(sqSelected)
                if len(playerClicks) == 2:
                    move = Move(playerClicks[0], playerClicks[1], gs.board)
                    gs.makeMove(move)
                    sqSelected = ()
                    playerClicks = []

        draw_game_state(screen, gs)
        clock.tick(MAX_FPS)
        pygame.display.flip()
    
    pygame.quit()

def load_images():
    pieces = ['wP', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bP', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
        IMAGES[piece] = pygame.image.load(pieceImages[piece])
        IMAGES[piece] = pygame.transform.scale(pygame.image.load(pieceImages[piece]), (SQ_SIZE, SQ_SIZE))

def draw_game_state(screen, gs):
    draw_board(screen)
    draw_pieces(screen, gs.board)
    draw_valid_moves()

def draw_pieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "__":
                screen.blit(IMAGES[piece], pygame.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))

def draw_valid_moves():
    pass

if __name__ == "__main__":
    main()