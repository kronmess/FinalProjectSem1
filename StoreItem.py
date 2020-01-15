import pygame
pygame.init()
win = pygame.display.set_mode((950, 600))
red = (255,0,0)
class StoreItem():
        
    
    def draw_text(self,message,color,x,y,font_size):
        Font = pygame.font.Font('press_start.ttf',font_size)
        text = Font.render(message, True, color)
        win.blit(text,[x,y])

    def make_rect(self,surface,color,rectangle,thickness= 0):
        pygame.draw.rect(surface,color,rectangle,thickness)
