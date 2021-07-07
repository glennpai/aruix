###
# nametools.py
# Collection of name functions that might be used across command modules
# @return string
###

import re

# Clean (...) portions of user nicknames
def clean_nick(nickname):
    try:
        return re.sub('\(.*?\)', '', nickname).strip()

    except Exception as error:
        return(f'There was an error with the COMMON.NAMETOOLS.CLEAN_NICK function.\nError: {error}\nPlease report this to @Джин#8189')
