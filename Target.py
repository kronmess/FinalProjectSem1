import pygame


#creating game window
win = pygame.display.set_mode((950, 600))

#target image
targetImage = pygame.image.load('target.png')

pygame.init()


#colors
black = (0,0,0)
red = (200,0,0)
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
        self.slingsOwned = int(self.text[2]) 
        self.slingsPrice = int(self.text[3])
        self.revolversOwned = int(self.text[4])
        self.revolversPrice = int(self.text[5])
        self.riflesOwned = int(self.text[6])
        self.riflesPrice = int(self.text[7])
        self.minigunsOwned = int(self.text[8])
        self.minigunsPrice = int(self.text[9]) 
        file.close()

    #draws in target values     
    def draw(self):
        win.fill(black)
        win.blit(self.targetImage,(self.x,self.y))
        self.commashotCount = '${:,}'.format(self.shotCount)
        Font = pygame.font.Font('press_start.ttf',20)
        shotCountDisplay = Font.render(self.commashotCount, True , lightBlue)
        shotcount_rect = shotCountDisplay.get_rect(center=(525,70))
        win.blit(shotCountDisplay,shotcount_rect)
        Font = pygame.font.Font('press_start.ttf',20)
        text = Font.render('MONEY:', True, lightBlue)
        win.blit(text,[475,15])
        



