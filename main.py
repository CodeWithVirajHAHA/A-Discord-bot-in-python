import discord
from discord.ext import commands
import time
client = discord.Client()

@client.event
async def on_message(message):
    message.content = message.content.lower()
    if message.author == client.user:
        return
    if message.content.startswith("hello"):
#responding to hello
        if str(message.author) == "CodeWithViraj#4138":
            await message.channel.send("Hello @CodeWithViraj#4138!")
        else:
            await message.channel.send("Hi! I am viraj-bot!")
    if message.content.startswith("hi"):

        if str(message.author) == "CodeWithViraj#4138":
            await message.channel.send("Hello @CodeWithViraj!")
        else:
            await message.channel.send("Hi! I am viraj-bot!")
            #responding to '-bot'
    if message.content.startswith("-bot"):

        if str(message.author) == "CodeWithViraj#4138":
            await message.channel.send("Yes sir?")
        elif str(message.author) == "Devmon99#3022":
            await message.channel.send("Yes sir?")
        else:
            await message.channel.send("I am sorry, I cannot respond to you... as sir\nIf you want me to respond to you as sir\nThen ask @CodeWithViraj#4138 for permission!")
    if message.content.startswith("-hack"):
        await message.channel.send("Ok.... Hacking")
        time.sleep(0.5)
        await message.channel.purge(limit=1)
        await message.channel.send("IP address: 1.192.168.80")
        time.sleep(0.5)
        await message.channel.purge(limit=1)
        await message.channel.send("Setting up Epic Games Account🎮")
        time.sleep(0.5)
        await message.channel.purge(limit=1)
        await message.channel.send("Finding DMS (If there are any...)")
        time.sleep(0.5)
        await message.channel.purge(limit=1)
        await message.channel.send("Last DM : I AM A IDIOT!!!")
        time.sleep(0.5)
        await message.channel.purge(limit=1)
        await message.channel.send("The totally safe hack is completed....")

@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'User {member} has been kicked')
client.run('Your_Token')
