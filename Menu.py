import pygame
from Target import red
from Target import white
from Target import win

def draw_text(message,color,x,y,font_size):
    Font = pygame.font.Font('press_start.ttf',font_size)
    text = Font.render(message, True, color)
    win.blit(text,[x,y])

def make_rect(surface,color,rectangle,thickness= 0):
    pygame.draw.rect(surface,color,rectangle,thickness)

class Menu:
    def __init__(self,stock,price,name,description,base,buybase,title_x,title_y,description_x,description_y,stock_x,stock_y,price_x,price_y):
        self.stock = stock
        self.price = price
        self.name = name
        self.description = description
        self.base = base
        self.buybase = buybase
        self.title_x = title_x
        self.title_y = title_y
        self.description_x = description_x
        self.description_y = description_y
        self.stock_x = stock_x
        self.stock_y = stock_y
        self.price_x = price_x
        self.price_y = price_y
    def draw(self):
        make_rect(win,white,self.base,9)
        make_rect(win,red,self.base)
        make_rect(win,red,self.buybase)
        make_rect(win,white,self.buybase,7)
        draw_text(f'{self.name}', white,self.title_x,self.title_y,18)
        draw_text(f'{self.description}', white,self.description_x,self.description_y,14)
        draw_text(str(self.stock) + ' ' + 'Owned', white,self.stock_x,self.stock_y,12)
        draw_text('BUY: ' + '$' +str(self.price),white,self.price_x,self.price_y,12)
