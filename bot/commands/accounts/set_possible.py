import discord
from modules.bot.db import possibleAccounts, accounts


async def execute(ctx, user, amount):
    if str(ctx.user.id) != "694644198531661844":
        await ctx.respond("Nope", ephemeral=True)
        return
    if (possibleAccounts.find_one({"uid": str(user.id)})):
        possibleAccounts.update_one({"uid": str(user.id)}, {
                                    "$set": {"amount": amount}})
    else:
        possibleAccounts.insert_one({"uid": str(user.id), "amount": amount})
    posaccounts = possibleAccounts.find_one({"uid": str(user.id)})["amount"]
    collection = accounts[str(user.id)]
    embed = discord.Embed(title="Added Accounts",
                          description=f"{user.name} has used `{collection.count_documents({})}/{posaccounts}` account(s)", color=0x0000FF)
    await ctx.respond(embed=embed, ephemeral=True)
