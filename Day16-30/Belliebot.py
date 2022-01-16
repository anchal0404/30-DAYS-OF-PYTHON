
from discord import client
import nextcord
from nextcord.ext import commands
import detoken
import aiohttp
import random

clients = commands.Bot(command_prefix="#")

@clients.command()
async def ping(ctx):
    await ctx.reply("hehe")

@clients.command()
async def hello(ctx):
    await ctx.reply("Hey! I am {0.user}".format(clients))
    await ctx.reply("How are you?")


@clients.command()
async def fine(ctx):
    await ctx.reply("That's Great")
    await ctx.reply("Nice to meet you")

@clients.command()
async def same(ctx):
    await ctx.reply(":)")

@clients.command(pass_context=True)
async def meme(ctx):
     embed = nextcord.Embed(title="", description="")

     async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)  
   
                


clients.run(detoken.TOKEN)