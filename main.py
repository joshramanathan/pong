# import the necessary libraries
import pygame, sys

from pygame import display
 
def main():
    # initialize pygame
    pygame.init()
    pygame.font.init()
 
    # create the window that we will be drawing to
    displayWidth = 500
    displayHeight = 400
    DISPLAY = pygame.display.set_mode((displayWidth, displayHeight), 0, 32)
 
    # define some color constants
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    scoreFont = pygame.font.SysFont('Stgotic', 30)

    y1 = 200
    y2 = 250
    pixelsPerTick = 0.45
    ballVelx = -0.3
    ballVely = 0.3
    ballx = 120
    bally = 150
    p1Score = 0
    p2Score = 0
 
    while True:
        # check to see if we should quit the program
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # clear the window by filling it with white pixels
        DISPLAY.fill(BLACK)
 
        # draw the blue rectangle at the specified position in the window (x, y, w, h)
        #pygame.draw.rect(DISPLAY, WHITE, (50, y1, 10, 60))      # Left paddle
        #pygame.draw.rect(DISPLAY, WHITE, (440, y2, 10, 60))     # Right paddle
        pygame.draw.rect(DISPLAY, WHITE, (245, 0, 10, displayHeight))     # Half line
        #pygame.draw.rect(DISPLAY, WHITE, (0, 100, displayWidth, 10))     # Top line
        #pygame.draw.rect(DISPLAY, WHITE, (ballx, bally, 10, 10))    # Ball

        leftPaddle = pygame.Rect(50, y1, 10, 60)
        pygame.draw.rect(DISPLAY, WHITE, leftPaddle)

        rightPaddle = pygame.Rect(440, y2, 10, 60)
        pygame.draw.rect(DISPLAY, WHITE, rightPaddle)

        topLine = pygame.Rect(0, 100, displayWidth, 10)
        pygame.draw.rect(DISPLAY, WHITE, topLine)

        ball = pygame.Rect(ballx, bally, 10, 10)
        pygame.draw.rect(DISPLAY, WHITE, ball)

        textsurface = scoreFont.render(str(p1Score), False, WHITE)

        keyPressed = pygame.key.get_pressed()
        
        y1moveup = False
        y1movedown = False
        y2moveup = False
        y2movedown = False
        if keyPressed[pygame.K_w]:
            y1moveup = True
        if keyPressed[pygame.K_s]:
            y1movedown = True
        if keyPressed[pygame.K_UP]:
            y2moveup = True
        if keyPressed[pygame.K_DOWN]:
            y2movedown = True
        if y1moveup and y1 > 110:
            y1 -= pixelsPerTick
        if y1movedown and y1 < displayHeight - 60:
            y1 += pixelsPerTick
        if y2moveup and y2 > 110:
            y2 -= pixelsPerTick
        if y2movedown and y2 < displayHeight - 60:
            y2 += pixelsPerTick

        if pygame.Rect.colliderect(ball, topLine) or bally > displayHeight - 10:
            ballVely *= -1

        if pygame.Rect.colliderect(ball, leftPaddle) or pygame.Rect.colliderect(ball, rightPaddle):
            ballVelx *= -1
            ballVelx *= 1.1
            ballVely *= 1.1
            #ballVely *= -1

        ballx += ballVelx
        bally += ballVely


        # tell pygame to present the updated window to the user
        pygame.display.update()
 
# start the main loop
main()