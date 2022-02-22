import discord
import subprocess
from modules.bot.db import accounts


async def execute(ctx, name):
    collection = accounts[str(ctx.user.id)]
    account = collection.find_one({"name": name})
    if account == None:
        await ctx.respond("BROOOOO ONLY VALID ACCOUNTSSSS", ephemeral=True)
        return
    subprocess.Popen(
        f"/usr/bin/node /config/workspace/selfbot/bot.js {account['token']} {ctx.user.id} {account['guild']} {account['channel']}", shell=True)
    embed = discord.Embed(title="Selfbot Started",
                          description=f"Started selfbot `{account['name']}`", color=0x0000FF)
    await ctx.respond(embed=embed, ephemeral=True)
