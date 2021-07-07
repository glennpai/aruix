# Aruix
#### Version 0.0.2

## Author
* Christopher Glenn
* chglenn20@gmail.com

## Purpose
A semi-modular Discord.py bot that serves as a testing ground for anything and everything I want a bot to do. 
I have had several iterations of Discord bots over time and wanted to create one flexible enough to drop in commands at a whim without maintaining monolithic Python code. This bot is not focused on speed or performance but rather the ability to add and remove features in an instant.
This project will primarily be a Discord.py bot but may eventually be ported to Discord.JS as another project.

## Disclaimer
I (the author) hold no responsibility for and provide no warranty or support for this bot. This project serves only as a sandbox for my creation. By copying, downloading, cloning, or otherwise replicating my project, you assume all responsibility for any interactions with the bot.

## Installation
1. Clone repository to desired location
1. Duplicate '.env-template' as '.env'
1. Populate '.env' with **DISCORD_TOKEN**, **DISCORD_GUILD**, and **COMMAND_PREFIX** values
1. Run the bot using `python3 bot.py`

## Development
* Adding Commands
1. Create a '*.py' module under '/commands/'
1. Add `from {module} import *` import statement to 'bot.py'
1. Add the necessary checks under the message event handler for your command

## Help
commands/help.md (todo)

## To Do
* Create useful help docs
* Dockerize
* Implement skaffolding
* Dynamically import modules in bot.py