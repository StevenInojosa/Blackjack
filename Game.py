"""
Pygame Data

@author: Steven Inojosa
"""
import pygame 
import sys
import time

from Blackjack import *


CARD_SIZE = (72,96)
CARD_CENTER = (36, 48)

CARD_BACK_SIZE = (72,96)
CARD_BACK_CENTER = (36, 48)

# Display size
display_width = 1000
display_height = 600

# Colors available (https://www.cdmon.com/es/apps/tabla-colores)
darkgreen     = (0,100,0)  
beige         = (245, 245, 220)
black         = (0,0,0)
red           = (255,0,0)
cadetblue     = (95, 158, 160)
darkslategrey = (47, 79, 79)
gold          = (255, 215, 0)


pygame.init()

# Letters font
font      = pygame.font.SysFont("Arial",20)
textfont  = pygame.font.SysFont("Arial",20)
title     = pygame.font.SysFont("Arial",26)
# game_end  = pygame.font.SysFont("Arial",20)
# blackjack = pygame.font.SysFont("Arial",20)

clock = pygame.time.Clock()

screen = pygame.display.set_mode((display_width, display_height))
screen.fill(darkgreen)
pygame.display.set_caption('BlackJack')

pygame.draw.rect(screen, beige, pygame.Rect(0, 0, display_width/4, display_height))

###########################################

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

#button display
def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h))
        if click[0] == 1 != None:
            action()
    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))

    TextSurf, TextRect = text_objects(msg, font, black)
    TextRect.center = ((x + (w/2)), (y + (h/2)))
    screen.blit(TextSurf, TextRect)
    

blackjack = Blackjack()
blackjack.deal()

# Run until the user asks to quit
running = True

def update_screen():
    screen.fill(darkgreen)
    pygame.draw.rect(screen, beige, pygame.Rect(0, 0, display_width/4, display_height))

    # Display Dealer Cards
    TextSurf, TextRect = text_objects("Dealer", title, beige)
    screen.blit(TextSurf, (350,110))
    if blackjack.hidden_card == True:
        card = blackjack.hand_dealer.hand[0]
        dealer_card = pygame.image.load('img/' + str(card) + '.png').convert()
        back_card = pygame.image.load('img/' + "BACK" + '.png').convert()
        screen.blit(dealer_card, (350 , 150))
        screen.blit(back_card, (450 , 150))
        
    else:
        m = 1
        for card in blackjack.hand_dealer.hand:
            dealer_card = pygame.image.load('img/' + str(card) + '.png').convert()
            screen.blit(dealer_card, (250 + m*100, 150))
            m += 1
            
    # Display Player Cards  
    TextSurf, TextRect = text_objects("Player", title, beige)
    screen.blit(TextSurf, (350,360))
    n = 1
    for card in blackjack.hand_player.hand:
        player_cards = pygame.image.load('img/' + str(card) + '.png').convert()
        screen.blit(player_cards, (250 + n*100, 400))
        n += 1
        
    # Print messages
    TextSurf, TextRect = text_objects(blackjack.message, title, gold)
    screen.blit(TextSurf, (350,60))
    
    # Print scores
    TextSurf, TextRect = text_objects("Dealer Score: " + str(blackjack.dealer_score), title, gold)
    screen.blit(TextSurf, (800,60))
    
    TextSurf, TextRect = text_objects("Player Score: " + str(blackjack.player_score), title, gold)
    screen.blit(TextSurf, (800,90))
    
    
def exit_game():
    pygame.quit()
    sys.exit
    
    
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit
            running = False
            
        update_screen()
    
        button("Deal" , 30, 100, 150, 50, cadetblue, darkslategrey, blackjack.deal)
        button("Hit"  , 30, 200, 150, 50, cadetblue, darkslategrey, blackjack.hit)
        button("Stand", 30, 300, 150, 50, cadetblue, darkslategrey, blackjack.stand)
        button("EXIT" , 30, 500, 150, 50, cadetblue, darkslategrey, exit_game ) 
        
        
    pygame.display.flip()
    

