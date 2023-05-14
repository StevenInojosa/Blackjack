# -*- coding: utf-8 -*-
"""
Blackjack 

@author: Steven Inojosa
"""
import random 
import pygame 
pygame.init()

SUITS = ["C", "S","H","D"]
RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10}

# Define Card Class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
            self.name = str(suit) + str(rank)
        else:
            self.suit = None
            self.rank = None
            print ("Invalid card: ", suit, rank)

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

# Define Hand class
class Hand:
    def __init__(self):
        self.hand = []	# create Hand object
        self.value = 0

    def __str__(self):
        return str( [card.suit + card.rank for card in self.hand])	# return a string representation of a hand

    def add_card(self, card):
        self.hand.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        self.value = 0
        A_in_hand = False
        for card in self.hand:
            self.value += VALUES[card.get_rank()]
            if card.get_rank() == "A":
                A_in_hand = True
        if self.value > 11:
            return self.value
        else:
            return self.value + A_in_hand*10

 
# define deck class
class Deck:    
    def __init__(self):
        self.cards = []
        
        for rank in RANKS:
            for suit in SUITS:
                self.cards.append(Card(suit, rank ))
        
    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return "Deck is empty"
    
    def __str__(self):
        return str( [card.suit + card.rank for card in self.cards])
    
class Blackjack:
    def __init__(self):
        self.in_play = True
        self.hidden_card = True
        self.deck = Deck()
        self.deck.shuffle()
        self.player_score =  0
        self.dealer_score = -1
        
        self.message = ""
        
        
    def deal(self):
        if self.in_play == True:
            self.dealer_score += 1            
            
        # Reset Hands
        self.hand_player = Hand()
        self.hand_dealer = Hand()
        
        # Deal cards
        self.hand_player.add_card(self.deck.deal_card())
        self.hand_dealer.add_card(self.deck.deal_card())
        self.hand_player.add_card(self.deck.deal_card())
        self.hand_dealer.add_card(self.deck.deal_card())
        
        self.in_play = True   
        self.message = ""
        
    def hit(self):
        if self.in_play == True:
            self.hand_player.add_card(self.deck.deal_card())
            
            if self.hand_player.get_value()>21:
                self.message = "You are busted"
                self.dealer_score += 1 
                self.in_play = False
        
    def stand(self):
        if self.in_play == True:        
            while self.hand_dealer.get_value() < 17:
                self.hand_dealer.add_card(self.deck.deal_card())
                
            if self.hand_dealer.get_value()>21:
                self.player_score += 1 
                self.message = "Dealer Busted, You win"
                
            else: 
                if self.hand_player.get_value() > self.hand_dealer.get_value():
                    self.player_score += 1 
                    self.message = "You win"
                    
                elif self.hand_player.get_value() < self.hand_dealer.get_value():
                    self.dealer_score += 1 
                    self.message = "You lose"
                    
                else:
                    self.message = "It's a tie"
                    
        self.in_play = False
        self.hidden_card = False
                         
# def upd():
#     # Display Dealer Cards
#     if blackjack.in_play == True:
#         pass
        
#     # Display Player Cards        
#         card = blackjack.hand_player
#         n = 1
#         hand_card = []
#     for card in blackjack.hand_player.hand:
#         hand_card = pygame.image.load('img/' + str(card) + '.png').convert()
#         screen.blit(hand_card, (250 + n*100, 400))
#         n += 1

# Para verificar Blackjack (almost ready)
# blackjack = Blackjack()
# print(blackjack.deck) 
# blackjack.deal()

# print("Player: ",blackjack.hand_player, blackjack.hand_player.get_value())   
# print("Dealer: ",blackjack.hand_dealer, blackjack.hand_dealer.get_value())       
   
# blackjack.hit()
# print()
# print("Player: ",blackjack.hand_player, blackjack.hand_player.get_value())  
# print("Dealer: ",blackjack.hand_dealer, blackjack.hand_dealer.get_value()) 

# blackjack.stand()
# print()
# print("Player: ",blackjack.hand_player, blackjack.hand_player.get_value()) 
# print("Dealer: ",blackjack.hand_dealer, blackjack.hand_dealer.get_value()) 

# Para verificar card (ready)
# card_test = Card("C","A")
# print(card_test)
# card_test = Card("D","5")
# print(card_test)
    
# Para verificar el Deck (ready)
# deck = Deck()
# print(deck)
# print()
# deck.shuffle()
# print(deck)
# print()
# last_card = deck.deal_card()
# print(last_card)
# print()
# print(deck)

# Para verificar Hand (ready)
# deck = Deck()
# deck.shuffle()
# hand_player = Hand()
# print(deck)
# print()
# print(hand_player)
# hand_player.add_card(deck.deal_card())
# print()
# print(deck)
# print()
# print(hand_player)
# print()
# hand_prueba = Hand()
# hand_prueba.add_card(Card("D","2"))
# hand_prueba.add_card(Card("C","3"))
# hand_prueba.add_card(Card("H","K"))
# hand_prueba.add_card(Card("S","A"))
# hand_prueba.add_card(Card("S","A"))
# print(hand_prueba)
# print(hand_prueba.get_value())