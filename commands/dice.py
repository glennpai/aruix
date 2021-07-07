###
# dice.py
# Rolls one or more dice, returning 1-6 per die
# @param Message
# @return string
###

import random
from commands.common.nametools import *

def roll():
    return random.randint(1, 6)
    
def dice(message):
    author = clean_nick(message.author.nick)

    try:
        if len(message.content.split(' ')) == 1:
            result = roll()
            return(f'{author}\'s die rolls a {result}')

        elif len(message.content.split(' ')) == 2 and message.content.split(' ')[1].isdigit():
            rolls = []
            numDice = int(message.content.split(' ')[1])

            for dice in range(numDice):
                rolls.append(str(roll()))

            result = ', '.join(rolls)

            return(f'{author}\'s dice roll as follows: {result}')
        
        else:
            return('Incorrect syntax. Please try again.')

    except Exception as error:
        return(f'There was an error with the DICE module.\nError: {error}\nPlease report this to @Джин#8189')
