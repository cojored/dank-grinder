import discord
from modules.bot.db import accounts


async def execute(ctx, name):
    collection = accounts[str(ctx.user.id)]
    account = collection.find_one({"name": name})
    if account == None:
        await ctx.respond("BROOOOO ONLY VALID ACCOUNTSSSS", ephemeral=True)
        return
    channel = ctx.bot.get_guild(int(account['guild'])).get_channel(
        int(account['channel']))
    await channel.send(".stop")
    embed = discord.Embed(title="Selfbot Stopped",
                          description=f"Stopped selfbot `{account['name']}`", color=0x0000FF)
    await ctx.respond(embed=embed, ephemeral=True)
