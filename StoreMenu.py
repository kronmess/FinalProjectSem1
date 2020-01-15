import pygame
from Target import Target
from Target import white
from Target import lightBlue
from Target import crimson
from Target import red
from Target import white
from StoreItem import StoreItem
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
        self.slingshot = StoreItem()

        #REVOLVER
        self.revolver = StoreItem()

        #RIFLE
        self.rifle = StoreItem()

        #MINIGUN
        self.minigun = StoreItem()
        
    def update(self):
        #updating values for sling
        self.slingshot.make_rect(win,white,pygame.Rect((25,20),(350,100)),9)
        self.slingshot.make_rect(win,red,pygame.Rect((25,20),(350,100)))
        self.buySlingOutline = pygame.Rect((200,80),(170,35))
        self.slingshot.make_rect(win,white,self.buySlingOutline,6)
        self.slingshot.make_rect(win,red,pygame.Rect((200,80),(170,35)))
        self.slingshot.draw_text('SLINGSHOT - 1 BPS', white,50,35,18)
        self.slingshot.draw_text('It will work for now', white,55,60,14)
        self.slingshot.draw_text(str(target1.slingsOwned) + ' ' + 'Owned', white,60,90,12)
        self.slingshot.draw_text('BUY: ' + '$' +str(target1.slingsPrice),white,230,95,12)

       #updating values for revolver
        self.revolver.make_rect(win,white,pygame.Rect((25,120),(350,100)),9)
        self.revolver.make_rect(win,red,pygame.Rect((25,120),(350,100)))
        self.buyRevolverOutline = pygame.Rect((200,180),(170,35))
        self.revolver.make_rect(win,white,self.buyRevolverOutline,6)
        self.revolver.make_rect(win,red,pygame.Rect((200,180),(170,35)))
        self.revolver.draw_text('REVOLVER - 6 BPS', white,50,135,18)
        self.revolver.draw_text('Ol reliable six shooter.', white,35,160,14)
        self.revolver.draw_text(str(target1.revolversOwned) + ' ' + 'Owned', white,60,190,12)
        self.slingshot.draw_text('BUY: ' + '$' +str(target1.revolversPrice),white,230,195,12)

        #updating values for rifle
        self.revolver.make_rect(win,white,pygame.Rect((25,220),(350,100)),9)
        self.revolver.make_rect(win,red,pygame.Rect((25,220),(350,100)))
        self.buyRifleOutline = pygame.Rect((200,280),(170,35))
        self.revolver.make_rect(win,white,self.buyRifleOutline,6)
        self.revolver.make_rect(win,red,pygame.Rect((200,280),(170,35)))
        self.revolver.draw_text('RIFLE - 30 BPS', white,50,235,18)
        self.revolver.draw_text('SSSSSSSSSKKKKRRRAAAAAAA.', white,35,260,14)
        self.revolver.draw_text(str(target1.riflesOwned) + ' ' + 'Owned', white,60,290,12)
        self.slingshot.draw_text('BUY: ' + '$' +str(target1.riflesPrice),white,230,295,12)
        
        #updating values for rifle
        self.minigun.make_rect(win,white,pygame.Rect((25,320),(350,100)),9)
        self.minigun.make_rect(win,red,pygame.Rect((25,320),(350,100)))
        self.buyMinigunOutline = pygame.Rect((200,380),(170,35))
        self.revolver.make_rect(win,white,self.buyMinigunOutline,6)
        self.revolver.make_rect(win,red,pygame.Rect((200,380),(170,35)))
        self.revolver.draw_text('MINIGUN - 100 BPS', white,50,335,18)
        self.revolver.draw_text("That's a lot of bulets.", white,35,360,14)
        self.revolver.draw_text(str(target1.minigunsOwned) + ' ' + 'Owned', white,60,390,12)
        self.slingshot.draw_text('BUY: ' + '$' +str(target1.minigunsPrice),white,225,395,12)