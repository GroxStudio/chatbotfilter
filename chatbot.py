import discord
from discord.ext import commands
import asyncio
from discord.utils import get
import os

bad_words = 'сука', 'хуй', 'пздц', 'пиздец', 'хуёк'




@bot.event
async def on_message(message):
	await bot.process_commands(message)
	msg = message.content.lower()
	
	
	if msg in bad_words:
		await message.delete()
		await message.author.send(embed = discord.Embed(description = f'{message.author}, Не матерись на сервере!',color=0x0c0c0c)) 

        







token = os.environ.get("chatbot")
client.run(str(token))
