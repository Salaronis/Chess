import pygame

pygame.init()
WIDTH = 1000
HEIGHT = 900
screen = pygame.display.set_mode([WIDTH, HEIGHT])
font = pygame.font.Font('freesansbold.ttf', 20)
pygame.display.set_caption('Chess')
big_font = pygame.font.Font('freesansbold.ttf', 50)
timer = pygame.time.Clock()
fps = 60

white_pieces = ['rook' , 'knight' , 'bishop' , 'queen', 'king', 'bishop' , 'knight', 'rook', 
                'pawn','pawn','pawn','pawn','pawn','pawn','pawn','pawn']
white_locations = [(0,0) , (1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (7,0) , (0,1),(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1)]
black_pieces = ['rook' , 'knight' , 'bishop' , 'queen', 'king', 'bishop' , 'knight', 'rook', 
                'pawn','pawn','pawn','pawn','pawn','pawn','pawn','pawn']
black_locations = [(0,7) , (1,7), (2,7), (3,7), (4,7), (5,7), (6,7), (7,7) , (0,6),(1,6),(2,6),(3,6),(4,6),(5,6),(6,6),(7,6)]

captured_white = []
captured_black = []


run  = True
while run:
    timer.tick(fps)
    screen.fill('dark gray')
    #event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()