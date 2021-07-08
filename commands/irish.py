###
# irish.py
# An instance of Irish poker, a popular drinking card game
# @param Message
# @return string
###

from commands.common.nametools import * 
from collections import namedtuple
import random

def irish(message):
    try:
        Card = namedtuple('Card', ['value', 'suit'])
        face_values = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']
        suits = ['hearts', 'diamonds', 'spades', 'clubs']
        cards = [Card(value, suit) for value in face_values for suit in suits]
        # for card in cards:
        #     print(f'{card.value.title()} of {card.suit.title()}')

        hand = []

        for card in range(4):
            hand.append(cards[random.randint(0,len(cards))])
            print(f'{hand[card].value} of {hand[card].suit}')
        print('\n\n')

        hand.clear()

        return 0

    except Exception as error:
        return(f'There was an error with the IRISH module.\nError: {error}\nPlease report this to @Джин#8189')
