import pygame
from Target import Target
from Target import white
from Target import lightBlue
from Target import crimson
from Target import red
from Target import white
#creating game window
win = pygame.display.set_mode((950, 600))

#instance of target class
target1 = Target(430,200,1)
pygame.init()




class StoreMenu:
    def __init__(self):
        self.menuRectFill = pygame.Rect((25,20),(350,400))
        self.menuRectOutline = pygame.Rect((25,20),(350,400))

        #SLINGSHOT
        self.slingsOwned = 0
        self.slingsPrice = 15
        self.slingbps = 1
        self.slingsOwned = int(target1.text[2])
        self.slingsPrice = int(target1.text[3])
        self.slingOutline = pygame.Rect((25,20),(350,100))

        #REVOLVER
        self.revolversOwned = 0
        self.revolversPrice = 100
        self.revolverbps = 6
        self.revolversOwned = int((target1.text[4]))
        self.revolversPrice = int((target1.text[5]))
        self.revolverOutline = pygame.Rect((25,120),(350,100))

        #RIFLE
        self.riflesOwned = 0
        self.riflesPrice = 5000
        self.riflebps = 15
        self.riflesOwned = int((target1.text[6]))
        self.riflesPrice = int((target1.text[7]))
        self.rifleOutline = pygame.Rect((25,220),(350,100))
        
        #MINIGUN
        self.minigunsOwned = 0
        self.minigunsPrice = 30000
        self.minigunbps = 100
        self.minigunsOwned = int((target1.text[8]))
        self.minigunsPrice = int((target1.text[9]))
        self.minigunOutline = pygame.Rect((25,320),(350,100))

        #Sling text display
        self.slingTitleFont = pygame.font.Font('press_start.ttf',18)
        self.slingDescFont = pygame.font.Font('press_start.ttf',14)
        self.slingsOwnedFont = pygame.font.Font('press_start.ttf',12)
        self.slingTitle = self.slingTitleFont.render('SLINGSHOT - 1 BPS', True, white)
        self.slingTitleRect = self.slingTitle.get_rect(center = ((205,45)))
        self.slingDesc = self.slingDescFont.render('It will work for now.',True,white)
        self.slingDescRect = self.slingDesc.get_rect(center = ((205,70)))
        self.buySlingOutline = pygame.Rect((200,82),(170,35))
        

        #Revolver text display
        self.revolverTitleFont = pygame.font.Font('press_start.ttf',18)
        self.revolverDescFont = pygame.font.Font('press_start.ttf',14)
        self.revolversOwnedFont = pygame.font.Font('press_start.ttf',12)
        self.revolverTitle = self.slingTitleFont.render('REVOLVER - 6 BPS', True, white)
        self.revolverTitleRect = self.slingTitle.get_rect(center = ((205,140)))
        self.revolverDesc = self.slingDescFont.render('Ol reliable six shooter.',True,white)
        self.revolverDescRect = self.slingDesc.get_rect(center = ((185,165)))
        self.buyRevolverOutline = pygame.Rect((200,180),(170,35))
        

        #Rifle text display
        self.rifleTitleFont = pygame.font.Font('press_start.ttf',18)
        self.rifleDescFont = pygame.font.Font('press_start.ttf',14)
        self.riflesOwnedFont = pygame.font.Font('press_start.ttf',12)
        self.rifleTitle = self.slingTitleFont.render('RIFLE - 30 BPS', True, white)
        self.rifleTitleRect = self.slingTitle.get_rect(center = ((205,240)))
        self.rifleDesc = self.slingDescFont.render('SSSSSSSSSKKKKRRRAAAAAAA.',True,white)
        self.rifleDescRect = self.slingDesc.get_rect(center = ((185,265)))
        self.buyRifleOutline = pygame.Rect((200,280),(170,35))
       

        #Minigun text display 
        self.minigunTitleFont = pygame.font.Font('press_start.ttf',18)
        self.minigunDescFont = pygame.font.Font('press_start.ttf',14)
        self.minigunsOwnedFont = pygame.font.Font('press_start.ttf',12)
        self.minigunTitle = self.minigunTitleFont.render('MINIGUN - 100 BPS', True, white)
        self.minigunTitleRect = self.minigunTitle.get_rect(center = ((205,340)))
        self.minigunDesc = self.minigunDescFont.render("That's a lot of bullets.",True,white)
        self.minigunDescRect = self.minigunDesc.get_rect(center = ((205,365)))
        self.buyMinigunOutline = pygame.Rect((200,380),(170,35))
        


    def update(self):
        pygame.draw.rect(win,red, self.menuRectFill)
        pygame.draw.rect(win,white, self.menuRectOutline, 5)

        #updating values for sling
        self.slingsOwnedText = self.slingsOwnedFont.render(str(self.slingsOwned) + ' ' + "Owned", True , white)
        self.slingsOwnedRect = self.slingsOwnedText.get_rect(center=((110,100)))
        self.buySlingText = self.slingsOwnedFont.render('BUY: ' + '$' +str(self.slingsPrice),True, white)
        self.buySlingRect = self.buySlingText.get_rect(center = ((285,100)))
        pygame.draw.rect(win,white,self.slingOutline, 5)
        pygame.draw.rect(win,white,self.buySlingOutline, 5)
        win.blit(self.slingTitle,self.slingTitleRect)
        win.blit(self.slingDesc,self.slingDescRect)
        win.blit(self.slingsOwnedText,self.slingsOwnedRect)
        win.blit(self.buySlingText,self.buySlingRect)
        
        #updating values for revolver
        self.revolversOwnedText = self.revolversOwnedFont.render(str(self.revolversOwned) + ' ' + "Owned", True , white)
        self.revolversOwnedRect = self.slingsOwnedText.get_rect(center=((110,200)))
        self.buyRevolverText = self.slingsOwnedFont.render('BUY: ' + '$' +str(self.revolversPrice),True, white)
        self.buyRevolverRect = self.buyRevolverText.get_rect(center = ((285,200)))
        pygame.draw.rect(win,white,self.revolverOutline, 5)
        pygame.draw.rect(win,white,self.buyRevolverOutline, 5)
        win.blit(self.revolverTitle,self.revolverTitleRect)
        win.blit(self.revolverDesc,self.revolverDescRect)
        win.blit(self.revolversOwnedText,self.revolversOwnedRect)
        win.blit(self.buyRevolverText,self.buyRevolverRect)
           

        #updating values for rifle
        self.riflesOwnedText = self.riflesOwnedFont.render(str(self.riflesOwned) + ' ' + "Owned", True , white)
        self.riflesOwnedRect = self.riflesOwnedText.get_rect(center=((110,300)))
        self.buyRifleText = self.riflesOwnedFont.render('BUY: ' + '$' +str(self.riflesPrice),True, white)
        self.buyRifleRect = self.buyRifleText.get_rect(center = ((285,300)))
        pygame.draw.rect(win,white,self.rifleOutline, 5)
        pygame.draw.rect(win,white,self.buyRifleOutline, 5)
        win.blit(self.rifleTitle,self.rifleTitleRect)
        win.blit(self.rifleDesc,self.rifleDescRect)
        win.blit(self.riflesOwnedText,self.riflesOwnedRect)
        win.blit(self.buyRifleText,self.buyRifleRect) 

        #updating values for minigun
        self.minigunsOwnedText = self.minigunsOwnedFont.render(str(self.riflesOwned) + ' ' + "Owned", True , white)
        self.minigunsOwnedRect = self.minigunsOwnedText.get_rect(center=((110,400)))
        self.buyMinigunText = self.minigunsOwnedFont.render('BUY: ' + '$' +str(self.minigunsPrice),True, white)
        self.buyMinigunRect = self.buyMinigunText.get_rect(center = ((285,400)))
 
        pygame.draw.rect(win,white,self.minigunOutline, 5)
        pygame.draw.rect(win,white,self.buyMinigunOutline, 5)
        win.blit(self.minigunTitle,self.minigunTitleRect)
        win.blit(self.minigunDesc,self.minigunDescRect)
        win.blit(self.minigunsOwnedText,self.minigunsOwnedRect)
        win.blit(self.buyMinigunText,self.buyMinigunRect) 
