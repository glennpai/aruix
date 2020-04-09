const Discord = require('discord.js');
const client = new Discord.Client();
const fs = require ("fs");
const auth = fs.readFileSync("./auth.json");
const key = JSON.parse(auth);

function delay(ms){
    return new Promise(resolve => setTimeout(resolve, ms));
}

client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
});

client.on('message', msg => {
  if (msg.content.startsWith('!simp')) {
    msg.channel.send(`${msg.author.username} is a simp.`);
  }
});

client.on('message', msg => {
    if (msg.content.startsWith('!move')) {
        const args = msg.content.slice(msg.length).split(' '); 
        const command = args.shift().toLowerCase();

        if (args && args.length){
            const member = msg.guild.member(msg.author);
            msg.guild.me.setNickname(`${member.nickname} [MOVED]`, '');
            const channel = member.guild.channels.cache.find(ch => ch.name === args[0]);
            delay(100).then(() => { channel.send('test'); });
            delay(100).then(() => { msg.guild.me.setNickname('Aruix', ''); });
        }
        else {
            return;
        }
    }
});

client.login(key.token);