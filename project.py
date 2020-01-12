#imports
import pygame
import os.path
from os import path
import math
from Target import Target
from Target import lightBlue
from Target import targetImage
from DisplayText import DisplayText
from StoreMenu import StoreMenu
from StoreMenu import target1

pygame.init()
win = pygame.display.set_mode((950, 600))
pygame.display.set_caption('Shoot the Target')
running = True
clock = pygame.time.Clock()
timecounter = 0
pygame.display.set_icon(targetImage)


#SFX
click_effect = pygame.mixer.Sound('sounds/pew.wav')
buy_effect = pygame.mixer.Sound('sounds/chaching.wav')

#instance of store menu 
storemenu1 = StoreMenu()

#Definition of BPS
BPS = 0
BPS = int(target1.text[1])
commaBPS = '{:,}'.format(BPS)
BPSFont = pygame.font.Font('press_start.ttf',20)
BPSDisplay = BPSFont.render(commaBPS , True, lightBlue)
BPSRect = BPSDisplay.get_rect(center=(525,100))
win.blit(BPSDisplay,BPSRect)

 
# Main Game Loop           
while running:
    x = pygame.mouse.get_pos()[0]
    y = pygame.mouse.get_pos()[1]

    sqx = (x - 525)**2
    sqy = (y -300)**2 
    target1.draw()
    storemenu1.update()
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            newFile = open('btarget.txt','w')
            newFile.write('MONEY: ' + str(target1.shotCount) + '\n')
            newFile.write('BPS: ' + str(BPS) + '\n')
            newFile.write('SLINGS: ' + str(storemenu1.slingsOwned) + '\n')
            newFile.write('SLINGS_PRICE: ' + str(storemenu1.slingsPrice) + '\n')
            newFile.write('REVOLVERS: '  + str(storemenu1.revolversOwned) + '\n')
            newFile.write('REVOLVERS_PRICE: ' + str(storemenu1.revolversPrice) + '\n')
            newFile.write('RIFLES: '  + str(storemenu1.riflesOwned) + '\n')
            newFile.write('RIFLES_PRICE: ' + str(storemenu1.riflesPrice) + '\n')
            newFile.write('MINIGUNS: '  + str(storemenu1.minigunsOwned) + '\n')
            newFile.write('MINIGUNS_PRICE: ' + str(storemenu1.minigunsPrice) + '\n')
            newFile.close()
            running = False

        #counter goes up when target is clicked
        if event.type == pygame.MOUSEBUTTONUP:
            if math.sqrt(sqx + sqy) < 90:
                target1.shotCount += target1.targetValue
                click_effect.play()
                
                
        #when the buy sling button is clicked
        if event.type == pygame.MOUSEBUTTONUP and storemenu1.buySlingOutline.collidepoint(pygame.mouse.get_pos()):
            if storemenu1.slingsPrice <= target1.shotCount:
                target1.shotCount -= storemenu1.slingsPrice
                storemenu1.slingsOwned += 1
                BPS += storemenu1.slingbps
                storemenu1.slingsPrice += int(storemenu1.slingsPrice // (4/100 * storemenu1.slingsPrice))
                buy_effect.play()

        #when the buy revolver button is clicked
        if event.type == pygame.MOUSEBUTTONUP and storemenu1.buyRevolverOutline.collidepoint(pygame.mouse.get_pos()):
            if storemenu1.revolversPrice <= target1.shotCount:
                target1.shotCount -= storemenu1.revolversPrice
                storemenu1.revolversOwned += 1
                BPS += storemenu1.revolverbps
                storemenu1.revolversPrice += int(storemenu1.revolversPrice // 6.5/100 * storemenu1.revolversPrice)
                buy_effect.play()

        #when the buy rifle button is clicked
        if event.type == pygame.MOUSEBUTTONUP and storemenu1.buyRifleOutline.collidepoint(pygame.mouse.get_pos()):
            if storemenu1.riflesPrice <= target1.shotCount:
                target1.shotCount -= storemenu1.riflesPrice
                storemenu1.riflesOwned += 1
                BPS += storemenu1.riflebps
                storemenu1.riflesPrice += int(storemenu1.riflesPrice // 90/100 * storemenu1.riflesPrice)
                buy_effect.play()

        #when the buy minigun button is clicked
        if event.type == pygame.MOUSEBUTTONUP and storemenu1.buyMinigunOutline.collidepoint(pygame.mouse.get_pos()):
            if storemenu1.minigunsPrice <= target1.shotCount:
                target1.shotCount -= storemenu1.minigunsPrice
                storemenu1.minigunsOwned += 1
                BPS += storemenu1.minigunbps
                storemenu1.minigunsPrice += int(storemenu1.minigunsPrice // 600/100 * storemenu1.minigunsPrice)
                buy_effect.play()

    #counter used to count bps
    timecounter += clock.tick()
    if timecounter >= 1000:
        target1.shotCount += BPS
        timecounter = 0       

               
    pygame.display.update()                 
pygame.quit()

      
