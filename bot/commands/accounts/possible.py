import discord
from modules.bot.db import possibleAccounts, accounts


async def execute(ctx, userObject):
    if userObject:
        user = userObject
    else:
        user = userObject
    if (possibleAccounts.find_one({"uid": str(user.id)})):
        posaccounts = possibleAccounts.find_one(
            {"uid": str(user.id)})["amount"]
    else:
        posaccounts = 1
    collection = accounts[str(user.id)]
    embed = discord.Embed(title="Possible Accounts",
                          description=f"You have used `{collection.count_documents({})}/{posaccounts}` account(s)", color=0x0000FF)
    await ctx.respond(embed=embed, ephemeral=True)
