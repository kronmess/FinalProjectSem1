import pygame

#creating game window
win = pygame.display.set_mode((950, 600))
pygame.init()

#class to display text
class DisplayText:
    def __init__(self,message,color,x,y):
        self.message = message
        self.color = color
        self.x = x 
        self.y = y
        Font = pygame.font.Font('press_start.ttf',20)
        text = Font.render(self.message, True, self.color)
        win.blit(text,[self.x,self.y])
