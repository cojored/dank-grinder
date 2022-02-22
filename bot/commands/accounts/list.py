import discord
from modules.bot.db import accounts, possibleAccounts


def getName(item):
    return f"Name: `{item['name']}`"


async def execute(ctx):
    if (possibleAccounts.find_one({"uid": str(ctx.user.id)})):
        posaccounts = possibleAccounts.find_one(
            {"uid": str(ctx.user.id)})["amount"]
    else:
        posaccounts = 1
    collection = accounts[str(ctx.user.id)]
    embed = discord.Embed(title="Accounts", color=0x0000FF)
    for document in collection.find():
        embed.add_field(
            name="Name", value=f"`{document['name']}`", inline=True)
        embed.add_field(
            name="Token", value=f"`{document['token'][:10]}...`", inline=True)
    embed.set_footer(
        text=f"You are using {collection.count_documents({})}/{posaccounts} account(s)")
    await ctx.respond(embed=embed, ephemeral=True)
