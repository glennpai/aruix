import { SlashCommandBuilder } from 'discord.js';

export const data = new SlashCommandBuilder()
	.setName('dice')
	.setDescription('Rolls a die!');
	
export async function execute(interaction) {
	await interaction.reply(`The die rolls a ${Math.floor(6 * Math.random()) + 1}!`);
}
