import discord
from discord.ext import commands
from discord import Client
import os, psutil
from datetime import datetime
    
bot = commands.Bot(command_prefix="<")
client.remove_command('help')

TOKEN = 'your precious token'

Client = discord.Client()
    
@bot.event
async def on_ready():
    print(f"{Client.user} is on")
    
@bot.command()
async def status(ctx):
    for proc in psutil.process_iter():
        if 'enet' in proc.name():
            await ctx.send("Server is UP")
            break;
            
@bot.command()
async def online(ctx):
    player = open('online.txt').readlines()
    await ctx.send(f"{player[0]} Online")
    
@bot.command()
async def player(ctx):
    listplayer = len(os.listdir('players'))
    await ctx.send(f"{listplayer} Account created")
    
@bot.command()
async def start(ctx):
    os.system(r'"Yout enet Path"')
    await ctx.send("Your server is UP Now")
    
@bot.command()
async def stop(ctx):
    os.system("taskkill /f /im Your enet name.exe")
    await ctx.send("Your server is Down Now")

@bot.command()
async def world(ctx):
    listworld = len(os.listdir('worlds'))
    await ctx.send(f"{listworld} Created For Now")

@bot.command()
async def help(ctx):
time = datetime.now()
clock = time.strftime(' %H:%M %p')
embed = discord.Embed(color=0x00ff00, title="Help Command")
embed.add_field("world (for know how world created), player (for know how much account created), online (for know how much people on), start (for start your enet.exe), stop (for stop your enet.exe)")
embed.set_footer("GTPS Controller by Purge.")

bot.run("TOKEN")