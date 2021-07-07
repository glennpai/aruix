###
# echo.py
# Echo what the author said as an easy way to test if the bot is alive
# @param Message
# @return string
###

from commands.common.nametools import * 

def echo(message):
    try:
        return(f'{clean_nick(message.author.nick)} says:\n{message.content[6:]}')

    except Exception as error:
        return(f'There was an error with the ECHO module.\nError: {error}\nPlease report this to @Джин#8189')
