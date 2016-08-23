import pygame
import sys
from pygame.locals import *
from datetime import datetime


pygame.init()

screen = pygame.display.set_mode((800,500))

pygame.display.set_caption('States Through Time')
pygame.display.set_icon(pygame.image.load('icon.png'))

pygame.mixer.music.load('music.mp3')
pygame.mixer.music.set_volume(10)
pygame.mixer.music.play(-1, 0.0)

class State():
    def __init__(self, name, yearJoined):
        self.name = name
        self.yearJoined = yearJoined
        self.image = pygame.image.load('images/' + self.name + '.png')
        self.toDraw = False
    def draw(self):
        screen.blit(self.image, (50,55))

def basicText(text, color):
    textSurf = pygame.font.Font('freesansbold.ttf',30).render(text, True, color)
    return textSurf
def basicButton(text, location):
    buttonSurf = pygame.Surface((400, 100))
    buttonSurf.fill((190,190,190))
    textSurf = pygame.font.Font('freesansbold.ttf', 60).render(text, True, (255,255,255), (190,190,190))

    buttonSurf.blit(textSurf, (buttonSurf.get_width()/2-textSurf.get_width()/2, buttonSurf.get_height()/2-textSurf.get_height()/2))
    buttonRect = buttonSurf.get_rect()
    buttonRect.topleft = (location[0], location[1])
    return (buttonSurf, buttonRect)

stateList = [
    State('delaware', 1787),
    State('pennsylvania', 1787),
    State('newJersey', 1787),
    State('georgia', 1788),
    State('connecticut', 1788),
    State('massachusetts', 1788),
    State('maryland', 1788),
    State('southCarolina', 1788),
    State('newHampshire', 1788),
    State('virginia', 1788),
    State('newYork', 1788),
    State('northCarolina', 1789),
    State('rhodeIsland', 1790),
    State('vermont', 1791),
    State('kentucky', 1792),
    State('tennessee', 1796),
    State('ohio', 1803),
    State('louisiana', 1812),
    State('indiana', 1816),
    State('mississippi', 1817),
    State('illinois', 1818),
    State('alabama', 1819),
    State('maine', 1820),
    State('missouri', 1821),
    State('arkansas', 1836),
    State('michigan', 1837),
    State('florida', 1845),
    State('texas', 1845),
    State('iowa', 1846),
    State('wisconsin', 1848),
    State('california', 1850),
    State('minnesota', 1851),
    State('oregon', 1859),
    State('kansas', 1861),
    State('westVirginia', 1863),
    State('nevada', 1864),
    State('nebraska', 1867),
    State('colorado', 1876),
    State('northDakota', 1889),
    State('southDakota', 1889),
    State('montana', 1889),
    State('washington', 1889),
    State('idaho', 1890),
    State('wyoming', 1890),
    State('utah', 1896),
    State('oklahoma', 1907),
    State('newMexico', 1912),
    State('arizona', 1912),
    State('alaska', 1959),
    State('hawaii', 1959)]

year = 1785
paused = False
menueUp = True
mouseCoords = [0,0]
yearsPerSecond = 60
stateTotal = 0

startSurf, startRect = basicButton('Start!', (200,300))
anotherStateSurf = basicText('Will there ever be another state?',(0,0,0))
skip1 = basicText('Fast foward 44 years to 1958.',(100,100,100))
skip2 = basicText('Two more states join America.',(100,100,100))
skip3 = basicText('The grand total is now 50!',(100,100,100))
textSurf1 = basicText('Are you ready to see the states as they',(255,255,255))
textSurf2 = basicText('entered the union?  I hope so!  When',(255,255,255))
textSurf3 = basicText('your\'re ready click start!',(255,255,255))
textSurf4 = basicText('At any time you can press SPACE to pause',(255,255,255))
textSurf5 = basicText('during your adventure.',(255,255,255))

fpsClock = pygame.time.Clock()
while True:
    screen.fill((0,0,0))
    stateTotalSurf = basicText('Total number of states: ' + str(stateTotal),(255,255,255))
    yearSurf = basicText('Year: ' + str(year),(255,255,255))
    if menueUp == False:
        for i in stateList:
            if i.toDraw == True:
                i.draw()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    if paused: paused = False
                    else: paused = True
                    
        if paused == False:
            if year != int(datetime.now().strftime('%Y')):
                year += 1
            if year == int(datetime.now().strftime('%Y')):
                screen.blit(anotherStateSurf,(screen.get_width() / 2 - anotherStateSurf.get_width() / 2, screen.get_height() / 2 - anotherStateSurf.get_height() / 2))

            statesToDrawNext = 0
            for i in stateList:
                if i.yearJoined == year:
                    statesToDrawNext += 1
            if statesToDrawNext == 0:
                yearsPerSecond = 4
            if statesToDrawNext > 1:
                yearsPerSecond = 1

            if year == 1913:
                screen.blit(skip1,(screen.get_width() / 2 - skip1.get_width() / 2, 200))
                screen.blit(skip2,(screen.get_width() / 2 - skip2.get_width() / 2, screen.get_height() / 2 - skip2.get_height() / 2))
            if year == 1914:
                year = 1958
                pygame.time.wait(4000)
            if year == 1960:
                screen.blit(skip1,(screen.get_width() / 2 - skip1.get_width() / 2, 200))
                screen.blit(skip2,(screen.get_width() / 2 - skip2.get_width() / 2, screen.get_height() / 2 - skip2.get_height() / 2))
                screen.blit(skip3,(screen.get_width() / 2 - skip3.get_width() / 2, 270))
                pygame.display.flip()
                pygame.time.wait(4000)
                
            
            for i in stateList:
                if i.yearJoined == year:
                    i.toDraw = True
                    stateTotal += 1
        screen.blit(stateTotalSurf, (400, 10))
        screen.blit(yearSurf, (10,10))
        
    if menueUp == True:
        screen.blit(textSurf1, (60,20))
        screen.blit(textSurf2, (60,60))
        screen.blit(textSurf3, (60,100))
        screen.blit(textSurf4, (60,140))
        screen.blit(textSurf5, (60,180))
        screen.blit(startSurf, startRect)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit(); sys.exit()
            if event.type == MOUSEMOTION:
                mouseCoords[0], mouseCoords[1] = event.pos
            if event.type == MOUSEBUTTONDOWN:
                if startRect.collidepoint((mouseCoords[0], mouseCoords[1])):
                    menueUp = False
                    yearsPerSecond = 4

    pygame.display.flip()
    fpsClock.tick(yearsPerSecond)
