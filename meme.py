import discord
from discord.ext import commands

description = '''esto es un programa donde vincula a discord con studio code para lanzar imagenes'''

intents = discord.Intents.default()
intents.members=True
intents.message_content=True

bot= commands.Bot(command_prefix='$',description=description,intents=intents)

@bot.event
async def on_ready():
    print(f'logeado como {bot.user} (ID: {bot.user.id})')

@bot.event
async def on_message(message):
    if message.author==bot.user:
        return 
    
    if message.content.lower()=='$meme1':
        with open('meme1.jpeg', 'rb') as f:
            picture = discord.File(f)
            await message.channel.send(content="Aqui esta un meme de programadores",file=picture)

bot.run("ingresa tu token")
