import discord
from modules.bot.db import possibleAccounts, accounts


async def execute(ctx, name):
    if (possibleAccounts.find_one({"uid": str(ctx.user.id)})):
        posaccounts = possibleAccounts.find_one(
            {"uid": str(ctx.user.id)})["amount"]
    else:
        posaccounts = 1
    collection = accounts[str(ctx.user.id)]
    account = collection.find_one({"name": name})
    await ctx.bot.get_guild(int(account['guild'])).get_channel(int(account['channel'])).delete()
    collection.delete_one({"name": name})
    embed = discord.Embed(title="Account Removed",
                          description=f"You now have `{collection.count_documents({})}/{posaccounts}` account(s)", color=0x0000FF)
    await ctx.respond(embed=embed, ephemeral=True)
