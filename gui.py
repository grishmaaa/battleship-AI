# pygame
import pygame

pygame.init()
pygame.display.set_caption("Battleship")

# global variables
SQ_SIZE = 45
H_MARGIN = SQ_SIZE * 4
V_MARGIN = SQ_SIZE
WIDTH = SQ_SIZE * 10 * 2 + H_MARGIN
HEIGHT = SQ_SIZE * 10 * 2 + V_MARGIN
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

# COLOR
GREY = (40, 50, 60)
WHITE = (255, 250, 250)

# pygame loop
animating = True
pausing = False
while animating:

    # tracking user interaction
    for event in pygame.event.get():

        # user closes the pygame window
        if event.type == pygame.QUIT:
            animating = False

        # user presses key on keyword
        if event.type == pygame.KEYDOWN:

            # ESCAPE KEY TO CLOSE THE ANIMATION
            if event.key == pygame.K_ESCAPE:
                animating = False

            # space bar to pause and unpause the animation
            if event.key == pygame.K_SPACE:
                pausing = not pausing
    if not pausing:
        SCREEN.fill(GREY)
        # displays
        pygame.display.flip()
