import discord

client = discord.Client()

@client.event
async def on_message(message):
    if message.content.find("hi") != -1:
        await message.channel.send("Hi :) Keep up the positive mindset!")
        print(message.content)
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
