import discord
from modules.bot.db import accounts


async def execute(ctx, name):
    collection = accounts[str(ctx.user.id)]
    embed = discord.Embed(title="Account Info", color=0x0000FF)
    if (collection.find_one({"name": name}) == None):
        await ctx.respond("An account with that name does not exist", ephemeral=True)
        return
    embed.add_field(
        name="Name", value=f"`{collection.find_one({'name': name})['name']}`", inline=True)
    embed.add_field(
        name="Token", value=f"`{collection.find_one({'name': name})['token']}`", inline=True)
    await ctx.respond(embed=embed, ephemeral=True)
