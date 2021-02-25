""" - Pong Main Program
Import section
"""
import pygame
from pygame.locals import *
from random import seed, randint

seed(a=None, version=2)

screenheight = 500  # max y value
screenWidth = 800  # max x value


class Game():

    def justToNotGetError(self):
        print("I do nothing")


class Player:

    def __init__(self, x, y, color, playerOne):
        self.y = y
        self.x = x
        self.color = color
        self.speed = 6
        self.lineHeight = 50
        self.lineWidth = 7
        self.playerOne = playerOne

    def move(self):
        keys = pygame.key.get_pressed()
        if self.playerOne:
            if self.y >= 360 or self.y <= 100:
                self.setPlayerBackOnGame()
            else:
                if keys[pygame.K_w]:
                    self.y -= self.speed

                if keys[pygame.K_s]:
                    self.y += self.speed
        else:
            if self.y >= 360 or self.y <= 100:
                self.setPlayerBackOnGame()
            else:
                if keys[pygame.K_UP]:
                    self.y -= self.speed

                if keys[pygame.K_DOWN]:
                    self.y += self.speed

    def drawPlayerLine(self, screen):
        pygame.draw.line(screen, self.color, (self.x, self.y), (self.x, self.y + self.lineHeight), self.lineWidth)

    def setPlayerBackOnGame(self):
        if self.y >= 360:
            self.y = 359
        else:
            self.y = 101


class Ball:
    def __init__(self):
        self.color = (209, 38, 38)
        self.y = 250
        self.x = 395
        self.xSpeed = 0
        self.ySpeed = 0
        self.gameInit = True

    def firstTouch(self):
        auxX = 0
        auxY = 0
        dir = randint(1, 6)
        if dir == 1:  # going on an HORIZONTAL line through player 1
            auxX = -4
            auxY = 0
        elif dir == 2:  # going on an HORIZONTAL line through player 2
            auxX = 4
            auxY = 0
        elif dir == 3:  # going on an DIAGONAL Y- line through player 1
            auxX = -4
            auxY = -4
        elif dir == 4:  # going on an DIAGONAL Y line through player 1
            auxX = -4
            auxY = 4
        elif dir == 5:  # going on an DIAGONAL Y- line through player 2
            auxX = 4
            auxY = -4
        elif dir == 6:  # going on an DIAGONAL Y line through player 1
            auxX = 4
            auxY = 4

        self.xSpeed = auxX
        self.ySpeed = auxY
        self.ySpeed = 4
        self.gameInit = False

    def updatePos(self):
        self.x += self.xSpeed
        self.y += self.ySpeed

    def moveBall(self, screen, p1, p2):
        if self.gameInit:
            self.firstTouch()
        else:
            str = self.hitBoard()
            if str == "Game Over Player 2" or str == "Game Over Player 1":
                return str

        self.hitPlayer(p1, p2)

        self.updatePos()
        pygame.draw.rect(screen, self.color, (self.x, self.y, 10, 10))

    def hitBoard(self):
        if self.y < 100:
            self.ySpeed = -1 * self.ySpeed
            return "Keep Going"
        elif self.y > 387:
            self.ySpeed = -1 * self.ySpeed
            return "Keep Going"
        if self.x > 670:
            return "Game Over Player 2"
        elif self.x < 130:
            return "Game Over Player 1"

    def hitPlayer(self, p, p2):
        # if self.xSpeed < 0: # going towards player 1
        if 156 >= self.x >= 143:
            if p.y - 1 <= self.y <= p.y + p.lineHeight + 1:
                self.setSpeedAfterPlayerImpact()
        # elif self.xSpeed > 0: # going towards player 2
        if 653 >= self.x >= 647:
            if p2.y - 1 <= self.y <= p2.y + p.lineHeight + 1:
                self.setSpeedAfterPlayerImpact()

    def setSpeedAfterPlayerImpact(self):
        ball.xSpeed *= -1
        if randint(1, 2) == 1:
            ball.ySpeed *= -1
            if ball.xSpeed > 0:
                ball.xSpeed = 6
            else:
                ball.xSpeed = -6
            if ball.ySpeed > 0:
                ball.ySpeed = 6
            else:
                ball.ySpeed = -6
        else:
            if ball.xSpeed > 0:
                ball.xSpeed = 4
            else:
                ball.xSpeed = -4
            if ball.ySpeed > 0:
                ball.ySpeed = 4
            else:
                ball.ySpeed = -4


p = Player(150, 230, (255, 0, 255), True)
p2 = Player(650, 230, (255, 255, 0), False)
ball = Ball()


def main():
    run = True
    pygame.init()  # initialize

    screen = pygame.display.set_mode((screenWidth, screenheight))
    clock = pygame.time.Clock()





    while run:
        clock.tick(70)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False

                elif event.type == QUIT:
                    run = False


        p.move()
        p2.move()

        gameIsOverStr = updateWindow(screen, p, p2, ball)

        if gameIsOverStr == "Game Over Player 1" or gameIsOverStr == "Game Over Player 2":
            run = False

        pygame.display.flip()

    pygame.quit()


def updateWindow(screen, p, p2, ball):
    screen.fill((0, 0, 0))
    for i in range(10):
        pygame.draw.line(screen, (255, 255, 255), (400, 100 + i * 30), (400, 110 + i * 30), 5)

    gameOverString = ball.moveBall(screen, p, p2)
    if gameOverString == "Game Over Player 1" or gameOverString == "Game Over Player 2":
        return gameOverString

    font = pygame.font.Font("freesansbold.ttf", 16)
    pygame.display.set_caption("PONG GAME - RENATO BARBOSA")
    text = font.render("PONG GAME", True, (255, 255, 255))
    textRect = text.get_rect()
    textRect.center = (400, 50)
    screen.blit(text, textRect)

    p.drawPlayerLine(screen)  # line of the player
    p2.drawPlayerLine(screen)

    # display de game board rectangle
    pygame.draw.rect(screen, (255, 255, 255), (100, 100, 600, 300), 5)  # width = 3
    # screen , color, rect -> x,y, x distance, y distance, width

    pygame.display.update()
    return "Keep going"


if __name__ == "__main__":
    main()
