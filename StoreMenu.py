import pygame
from Target import Target
from Target import red
from Target import white
from Target import win
from Menu import Menu


#instance of target class
target1 = Target(430,200,1)
pygame.init()

#class to create menu
class StoreMenu:
    def __init__(self):
        self.slingshot = Menu(target1.slingsOwned,target1.slingsPrice,'SLINGSHOT - 1 BPS', 'It will work for now',pygame.Rect((25,20),(350,100)),pygame.Rect((200,80),(170,35)),50,35,50,60,60,90,230,95)
        self.revolver = Menu(target1.revolversOwned,target1.revolversPrice,'REVOLVER - 6 BPS', 'Ol reliable six shooter.',pygame.Rect((25,120),(350,100)),pygame.Rect((200,180),(170,35)),50,135,50,160,60,190,230,195)
        self.rifle = Menu(target1.riflesOwned,target1.riflesPrice,'RIFLE - 30 BPS','SSSSSSSSSKKKKRRRAAAAAAA.',pygame.Rect((25,220),(350,100)),pygame.Rect((200,280),(170,35)),50,235,50,260,60,290,230,295)
        self.minigun = Menu(target1.minigunsOwned,target1.minigunsPrice,'MINIGUN - 100 BPS',"That's a lot of bulets.",pygame.Rect((25,320),(350,100)),pygame.Rect((200,380),(170,35)),50,335,50,360,60,390,230,395)

    #updates by drawing in each instance and updating their respective values    
    def update(self):
        self.slingshot.draw()
        self.revolver.draw()
        self.rifle.draw()
        self.minigun.draw()
        self.slingshot.stock = target1.slingsOwned
        self.slingshot.price = target1.slingsPrice
        self.revolver.stock = target1.revolversOwned
        self.revolver.price = target1.revolversPrice
        self.rifle.stock = target1.riflesOwned
        self.rifle.price = target1.riflesPrice
        self.minigun.stock = target1.minigunsOwned
        self.minigun.price = target1.minigunsPrice