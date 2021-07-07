###
# teams.py
# Create two equal-ish teams based on the members present in the voice channel
# @param Message
# @return string
###

import random
from commands.common.nametools import *

def teams(message):
    try:
        if message.author.voice.channel is None:
            return('No valid voice channel found.\nPlease connect to a voice channel and try again.')

        team1 = []
        team2 = []

        for member in message.author.voice.channel.members:
            team1.append(clean_nick(member.nick))

        if len(team1) == 1:
            return(f'Team one: {team1[0]}')

        elif len(team1) == 2:
            return(f'Team one: {team1[0]}\nTeam two: {team1[1]}')
        # Create teams based on what I call "duck duck goose" selection
        # Super inefficient but I wanted this done in an interesting way
        else:
            half = len(team1)/2
            if half % 2 == 0:
                while len(team2) < half:
                    for member in team1:
                        if (random.randint(0,2) == 2):
                            team2.append(team1.pop(team1.index(member)))
            else: 
                while len(team2) < half - 1:
                    for member in team1:
                        if (random.randint(0,2) == 2):
                            team2.append(team1.pop(team1.index(member)))

            teamOne = ', '.join(team1)
            teamTwo = ', '.join(team2)
            return(f'Team one: {teamOne}\nTeam two: {teamTwo}')

    except Exception as error:
        return(f'There was an error with the TEAMS module.\nError: {error}\nPlease report this to @Джин#8189')
