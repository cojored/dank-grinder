import discord
import requests
import json
import random
from modules.bot.db import possibleAccounts, accounts

guilds = [944306638117036132, 944306568399302736, 944306502578085928]


async def execute(ctx, name, token):
    # Set amount of possible accounts
    if (possibleAccounts.find_one({"uid": str(ctx.user.id)})):
        posaccounts = possibleAccounts.find_one(
            {"uid": str(ctx.user.id)})["amount"]
    else:
        posaccounts = 1
    # Can they create a new account?
    collection = accounts[str(ctx.user.id)]
    if (int(collection.count_documents({})) >= int(posaccounts)):
        await ctx.respond("Max Accounts Created", ephemeral=True)
        return
    # Does an account with that name exist already
    if (collection.find_one({"name": name})):
        await ctx.respond("An account with that name exists already.", ephemeral=True)
        return
    await ctx.respond("Creating Account...... (No this is not just here to waste your time there are actual things happening)", ephemeral=True)
    # Validate Token
    vt = requests.post("http://localhost:6000/validateToken", data=json.dumps(
        {"token": token}), headers={'content-type': 'application/json'})
    if vt.status_code == 500:
        await ctx.interaction.edit_original_message("Enter a valid token :/")
        return
    elif vt.status_code == 200:
        pass
    else:
        await ctx.interaction.edit_original_message("An unexpected error occured please contact a mod/admin")
        return
    # Pick the guild id
    gid = random.choice(guilds)
    # Put the user into the guild needed for the further commands
    jg = requests.post("http://localhost:6000/joinGuild",
                       data=json.dumps({"guild": gid, "token": token}), headers={"content-type": "application/json"})
    if jg.status_code == 500:
        await ctx.interaction.edit_original_message("An error occured check your token and report this to a mod/admin")
        return
    elif jg.status_code == 200:
        pass
    else:
        await ctx.interaction.edit_original_message("An unexpected error occured please report this to a mod/admin")
        return
    # Make api call to get the user ID
    uid = requests.post("http://localhost:6000/getUid",
                        data=json.dumps({"token": token}), headers={'content-type': 'application/json'})
    # Variable Setting
    guild = ctx.bot.get_guild(gid)
    channel = await guild.create_text_channel(f"{ctx.user.id}-{name}", overwrites={guild.default_role: discord.PermissionOverwrite(read_messages=False), guild.get_member(int(uid.text)): discord.PermissionOverwrite(read_messages=True)})
    # Create account
    collection.insert_one({"name": name, "token": token, "aid": int(
        uid.text), "guild": int(guild.id), "channel": int(channel.id)})
    # Reply
    embed = discord.Embed(
        title="Account Added", description=f"You now have `{collection.count_documents({})}/{posaccounts}` account(s)", color=0x0000FF)
    await ctx.interaction.edit_original_message("Created", embed=embed)
