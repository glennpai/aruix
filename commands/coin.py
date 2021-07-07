###
# coin.py
# Flips one or more coins, returning Heads or Tails once per coin
# @param Message
# @return string
###

import random
from commands.common.nametools import *

def flip():
    if (random.randint(0,1) == 1):
        return('Heads')
    else: 
        return('Tails')

def coin(message):
    author = clean_nick(message.author.nick)

    try:
        if len(message.content.split(' ')) == 1:
            result = flip()
            return(f'{author}\'s coin shows: {result}')

        elif len(message.content.split(' ')) == 2 and message.content.split(' ')[1].isdigit():
            flips = []
            numCoins = int(message.content.split(' ')[1])

            for coin in range(numCoins):
                flips.append(str(flip()))

            result = ', '.join(flips)
            
            return(f'{author}\'s coins flip as follows: {result}')
        
        else:
            return('Incorrect syntax. Please try again.')

    except Exception as error:
        return(f'There was an error with the COIN module.\nError: {error}\nPlease report this to @Джин#8189')
