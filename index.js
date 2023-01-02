import { readFileSync, readdirSync } from 'fs';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';
import { Client, Collection, Events, GatewayIntentBits } from 'discord.js';

const config = JSON.parse(readFileSync("./config.json"));

const client = new Client({ intents: [GatewayIntentBits.Guilds] });
client.commands = new Collection();

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const commandsPath = join(__dirname, 'commands');
const commandFiles = readdirSync(commandsPath).filter(file => file.endsWith('.js'));

// Add each command to the client object
for (const file of commandFiles) {
	const filePath = join(commandsPath, file);
	const command = await import(filePath);
	client.commands.set(command.data.name, command);
}

// Executes on server event such as a message or slash command
client.on(Events.InteractionCreate, async interaction => {
	if (!interaction.isChatInputCommand()) return;

	const command = interaction.client.commands.get(interaction.commandName);

	if (!command) {
		console.error(`No command matching ${interaction.commandName} was found.`);
		return;
	}

	try {
		await command.execute(interaction);
	} catch (error) {
		console.error(error);
		await interaction.reply({ content: 'There was an error while executing this command!', ephemeral: true });
	}
});

// Executes once on startup to let us know the bot's ready
client.once(Events.ClientReady, c => {
	console.log(`Ready! Logged in as ${c.user.tag}`);
});

// Log in as client user
client.login(config.token);
