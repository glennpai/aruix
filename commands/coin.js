import { SlashCommandBuilder } from 'discord.js';

export const data = new SlashCommandBuilder()
	.setName('coin')
	.setDescription('Flips a coin!');
	
export async function execute(interaction) {
	const result = Math.random() < 0.5 ? 'heads' : 'tails'
	await interaction.reply(`The coin lands on ${result}!`);
}
