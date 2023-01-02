# Aruix

## Author
Christopher Glenn
chglenn20@gmail.com

## Purpose
An attempt at making a Discord bot to do my bidding. Usually just one-off commands I want to try or someone's feature request. This code is constantly changing and is by no means production-grade. 

## Disclaimer
**I (the author) hold no responsibility for and provide no warranty or support for this project**. This project as a whole, the "bot" and its underlying code, and any subsequent documentation serve **ONLY** as reference to my learning experience. By copying, downloading, cloning, or otherwise replicating this project, **YOU** assume all responsibility for any interactions with the bot or any effects from using the bot.

May include boilerplate from https://discordjs.guide.

## Getting Started
1. Clone repository to desired location
1. Duplicate 'config.json.template' as 'config.json'
1. Populate 'config.json' with appropriate values
1. Deploy slash commands to your server using `npm run deploy`
1. Start the bot using `npm run start`

## Development
### Adding Commands
1. Create a `*.js` file under `./commands`
1. Develop command, complete with data and execution instructions
1. Deploy command to your server using `npm run deploy`

## TODO
1. Add Docker
1. Add docs
1. Add tests
1. Add pretty embeds to replies
