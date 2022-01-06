from discord import client
import nextcord
from nextcord.ext import commands
import estoken
clients = commands.Bot(command_prefix="!")

@clients.command()
async def ping(ctx):
    await ctx.reply("hatt!!")

@clients.command()
async def hello(ctx):
    await ctx.reply("Hey! I am {0.user}".format(clients))
    await ctx.reply("KEM CHO!")


@clients.command()
async def fine(ctx):
    await ctx.reply("That's Great")
    await ctx.reply("Nice to meet you")

@clients.command()
async def same(ctx):
    await ctx.reply(":)")


clients.run(estoken.TOKEN)