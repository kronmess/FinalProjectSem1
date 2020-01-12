import pygame
from DisplayText import DisplayText

#creating game window
win = pygame.display.set_mode((950, 600))

#target image
targetImage = pygame.image.load('target.png')

pygame.init()


#colors
black = (0,0,0)
lightBlue = (0,0,255)
red = (200,0,0)
crimson = (153,0,0)
white = (255,255,255)

#class to create target object
class Target():
    def __init__(self,x,y,targetValue):
        self.x = x
        self.y = y
        self.shotCount = 0
        self.targetImage = targetImage
        self.targetValue = targetValue
        self.shotCounter()
        self.draw()
    
    #function used to create the incremental counter
    def shotCounter(self):
        file = open('btarget.txt','r')
        self.text = file.read()
        self.text = self.text.split('\n')
        self.text = [line.replace('MONEY: ', '') for line in self.text]
        self.text = [line.replace('BPS: ', '') for line in self.text]
        self.text = [line.replace('SLINGS: ', '') for line in self.text]
        self.text = [line.replace('SLINGS_PRICE: ', '') for line in self.text]
        self.text = [line.replace('REVOLVERS: ', '') for line in self.text]
        self.text = [line.replace('REVOLVERS_PRICE: ', '') for line in self.text]
        self.text = [line.replace('RIFLES: ', '') for line in self.text]
        self.text = [line.replace('RIFLES_PRICE: ', '') for line in self.text]
        self.text = [line.replace('MINIGUNS: ', '') for line in self.text]
        self.text = [line.replace('MINIGUNS_PRICE: ', '') for line in self.text]
        self.shotCount = int(self.text[0]) 
        file.close()
         
    def draw(self):
        win.fill(black)
        win.blit(self.targetImage,(self.x,self.y))
        self.commashotCount = '${:,}'.format(self.shotCount)
        Font = pygame.font.Font('press_start.ttf',20)
        shotCountDisplay = Font.render(self.commashotCount, True , lightBlue)
        shotcount_rect = shotCountDisplay.get_rect(center=(525,70))
        win.blit(shotCountDisplay,shotcount_rect)
        money_shot_text = DisplayText('MONEY:',lightBlue,475,15)



