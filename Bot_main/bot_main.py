import discord
import os
import random
from discord.ext import commands
from discord.ext.commands import Bot

client = commands.Bot(command_prefix='!')

def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()
token = read_token()

dclient = Bot('!')
# client = discord.Client()

@client.event # Toimii
async def on_ready():
    print(f'{client.user.name} is online!')

@client.command() # Toimii
async def bot_info(ctx):
    embed = discord.Embed(title="DnD-Bot", description="Making DnD easier :)")
    embed.add_field(name="Commands I react to:", value="!phb, !roll d4....")
    await ctx.send(embed=embed)

@client.command()
async def phb(ctx):
    await ctx.send("A link to the player's handbook: http://orc-news.ru/dnd5eng.pdf")

@client.command() # TOIMII
async def gheotak(ctx):
    await ctx.send(random.choice(['Evil! :>', 'Made a few deals...', 'Loves Hilda']))

@client.command() # TOIMII
async def d4(ctx):
    d4 = list(range(1,5))
    await ctx.send(random.choice(d4))

@client.command() # TOIMII
async def d6(ctx):
    d6 = list(range(1,7))
    await ctx.send(random.choice(d6))

@client.command() # TOIMII
async def d8(ctx):
    d8 = list(range(1,9))
    await ctx.send(random.choice(d8))

@client.command() # TOIMII
async def d10(ctx):
    d10 = list(range(1,11))
    await ctx.send(random.choice(d10))

@client.command() # TOIMII
async def d12(ctx):
    d12 = list(range(1,13))
    await ctx.send(random.choice(d12))

@client.command() # TOIMII
async def d20(ctx):
    d20 = list(range(1,21))
    await ctx.send(random.choice(d20))

@client.command() # TOIMII
async def d100(ctx):
    d100 = list(range(1,101))
    await ctx.send(random.choice(d100))

client.run(token)
