import discord
from discord.ext import commands
import asyncio
from discord.utils import get
import os

bad_words = 'сука', 'хуй', 'пздц', 'пиздец', 'хуёк', 'бля', 'блядь', 'блять', 'блядина', 'шалава', 'шлюха', 'пидорас', 'pidor', 'пидор', 'хуйня', 'хуила', 'пидрилла', 'пидр', 'пидрила'


bot = commands.Bot(command_prefix = "*")


@bot.event
async def on_ready(*args):
    type = discord.ActivityType.Streaming
    activity = discord.Activity(name = "Удаляет маты 24на7.. Процесс...", type = type)
    status = discord.Status.online
    await bot.change_presence(activity = activity, status = status)
    print('Онлайн')




@bot.event
async def on_message(message):
	await bot.process_commands(message)
	msg = message.content.lower()
	
	
	if msg in bad_words:
		await message.delete()
		await message.author.send(embed = discord.Embed(description = f'{message.author}, Не матерись на сервере!',color=0x0c0c0c)) 

        







token = os.environ.get("chatbot")
bot.run(str(token))
