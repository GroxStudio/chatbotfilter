import discord
from discord.ext import commands
import asyncio
from discord.utils import get
import os

bot = commands.Bot(command_prefix='f.') #инициализируем бота с префиксом 'f.'

bad_words = [ 'сука', 'хуй', 'пздц', 'пиздец', 'хуёк' ]




@bot.event
async def on_message(message):
	await bot.procces_commands(message)

	msg = message.content.lower()

	if msg in bad_words:
		await message.delete()
		await message.author.send(f {message.author.name}, Не матерись на сервере!)







token = os.environ.get("chatbot")
bot.run(str(token))