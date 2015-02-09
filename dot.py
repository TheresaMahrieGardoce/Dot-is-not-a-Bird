__author__ = 'Renaldo Valente'

import random
from random import randint

import sys
from time import sleep

import pygame
from pygame.locals import *

class Player:

    def __init__(self):
        self.size = 10
        self.x = screenWidth / 2
        self.y = screenHeight / 3
        self.rectangle = Rect(0, 0, self.size, self.size)
        self.rectangle.center = (self.x, self.y)
        self.upSpeed = 0
        self.gravity = .4
        self.downSpeed = 10
        self.jumpSpeed = 6.3
        self.score = 0
        self.isAlive = True
        self.time = 0

    def move(self):
        self.upSpeed -= self.gravity
        if abs(self.upSpeed) >= self.downSpeed:
            self.upSpeed =- self.downSpeed
        self.rectangle.y -= self.upSpeed
        if self.time != 0:
            self.time += 1
            if self.time >= 6:
                self.time = 0
        if self.rectangle.top > screenHeight or self.rectangle.top < 0:
            sounds['hit'].play()
            self.isAlive = False
            sounds['die'].play()
            return
        for dot in obstacles:
            if self.rectangle.colliderect(dot.rectangle1) or self.rectangle.colliderect(dot.rectangle2):
                sounds['hit'].play()
                self.isAlive = False
                sounds['die'].play()                
                randTaunt = random.randint(0, len(taunt) - 1)
                msgSurfaceObj = fontObj.render(taunt[randTaunt], False, white)
                msgRectObj = msgSurfaceObj.get_rect()
                msgRectObj.center = (screenWidth / 2, 120)
                windowSurfaceObj.blit(msgSurfaceObj, msgRectObj)

    def startJump(self):
        if self.time == 0:
            self.upSpeed = self.jumpSpeed
            self.time += 1

    def getRect(self):
        return (self.rectangle.x, self.rectangle.y, self.rectangle.width, self.rectangle.height)


class Obstacles:

    def __init__(self):
        self.notPassed = True
        self.x = screenWidth
        self.width = 5
        self.gapSize = 50
        self.y = randint(screenHeight * 2 // 7, screenHeight * 5 // 7)
        self.rectangle1 = Rect(self.x, 0, self.width, self.y)
        self.rectangle2 = Rect(self.x, self.y + self.gapSize, self.width, screenHeight - self.gapSize - self.y)

    def move(self):
        self.rectangle1.x -= 2
        self.rectangle2.x -= 2

    def getRect(self):
        return [(self.rectangle1.x, self.rectangle1.y, self.rectangle1.width, self.rectangle1.height),
                (self.rectangle2.x, self.rectangle2.y, self.rectangle2.width, self.rectangle2.height)]

pygame.init()
fpsClock = pygame.time.Clock()
screenWidth = 600
screenHeight = 300

sounds = {}
sounds['die'] = pygame.mixer.Sound('assets/wav/die.wav')
sounds['hit'] = pygame.mixer.Sound('assets/wav/hit.wav')
sounds['point'] = pygame.mixer.Sound('assets/wav/point.wav')
sounds['wing'] = pygame.mixer.Sound('assets/wav/wing.wav')

windowSurfaceObj = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Python Game by Renaldo Valente')
fontObj = pygame.font.Font('assets/ttf/04B_19__.ttf', 30)

taunt = (
        "Todo na 'yun?",
        "Seryoso?",
        "Wahahaha, talo!",
        "Wala ito. Puro lang porma.",
        "Ano, kaya pa?",
        "Kanina ka pa ah",
        "Yan score mo? edi Wow!",
        "Boom, Panes!",
        "Palakpakan!",
        "Akala mo Flappy Bird?",
        "Sapul sa mukha",
        "Try and Fly til you die?",
        "Concentrate",
        "Focus",
        "Isa pa?",
        "Ngumiti ka naman",
        "Psst, pwede huminga",
        "Better than Flappy Bird",
        "I'm not a bird",
        "Better than Toper",
        "Bigyan ng jacket",
        "Nakita ko yun, haha!",
        "Yabang!",
        "Kaya yan, tiwala lang",
        "Magaling pa si Toper",
    )

white = pygame.Color(255,255,255)
black = pygame.Color(0,0,0)
red = pygame.Color(255,51,102)
green = pygame.Color(51,204,102)
blue = pygame.Color(51,204,255)
yellow = pygame.Color(255,204,102)

while True:

    obstacles = []
    started = False
    spawnCount = 10
    player = Player()
    pygame.event.clear()

    while player.isAlive:
        windowSurfaceObj.fill(yellow)

        if started:

            if spawnCount >= 80:
                spawnCount = 0
                obstacles.append(Obstacles())
            spawnCount += 1

            player.move()
            pygame.draw.rect(windowSurfaceObj, red, player.getRect())
            for dot in obstacles:
                dot.move()
                if dot.rectangle1.right < 0:
                    if dot in obstacles:
                        obstacles.remove(dot)
                    continue
                if dot.notPassed and dot.rectangle1.centerx <= player.rectangle.x:
                    dot.notPassed = False
                    player.score += 1
                    sounds['point'].play()
                pygame.draw.rect(windowSurfaceObj, white, dot.getRect()[0])
                pygame.draw.rect(windowSurfaceObj, white, dot.getRect()[1])
            msgSurfaceObj = fontObj.render(str(player.score), False, red)
            msgRectObj = msgSurfaceObj.get_rect()
            msgRectObj.center = (screenWidth / 2, 30)
            windowSurfaceObj.blit(msgSurfaceObj, msgRectObj)
        else:
            pygame.draw.rect(windowSurfaceObj, red, player.getRect())
            msgSurfaceObj = fontObj.render('Dot is not a Bird', False, red)
            msgRectObj = msgSurfaceObj.get_rect()
            msgRectObj.center = (screenWidth / 2, screenHeight / 2)
            windowSurfaceObj.blit(msgSurfaceObj, msgRectObj)

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                started = True
                sounds['wing'].play()
                player.startJump()
            elif event.type == MOUSEBUTTONDOWN:
                started = True
                sounds['wing'].play()
                player.startJump()

        pygame.display.update()
        fpsClock.tick(60)
    sleep(3)
