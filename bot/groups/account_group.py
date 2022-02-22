import discord
import commands.accounts.add as cadd
import commands.accounts.info as cinfo
import commands.accounts.list as clist
import commands.accounts.delete as cdelete
import commands.accounts.possible as cpossible
import commands.accounts.set_possible as cset_possible
from discord.commands import Option
accountGroup = discord.SlashCommandGroup(
    name="account", description="Account Managment", guild_ids=[940315647064277022])


@accountGroup.command(guild_ids=[940315647064277022])
async def add(ctx, name: Option(str, "What should we call this alt", required=True), token: Option(str, "Enter your alt's token", required=True)):
    await cadd.execute(ctx, name, token)


@accountGroup.command(guild_ids=[940315647064277022], description="Gives you info on an account")
async def info(ctx, name: Option(str, "Alt Name", required=True)):
    await cinfo.execute(ctx, name)


@accountGroup.command(guild_ids=[940315647064277022], description="Lists your accounts")
async def list(ctx):
    await clist.execute(ctx)


@accountGroup.command(guild_ids=[940315647064277022], description="Removes an account")
async def delete(ctx, name: Option(str, "Alt Name", required=True)):
    await cdelete.execute(ctx, name)


@accountGroup.command(guild_ids=[940315647064277022], description="Removes an account")
async def remove(ctx, name: Option(str, "Alt Name", required=True)):
    await cdelete.execute(ctx, name)


@accountGroup.command(guild_ids=[940315647064277022], description="Shows you the number of accounts have/can have")
async def possible(ctx):
    await cpossible.execute(ctx)


@accountGroup.command(guild_ids=[940315647064277022], description="Set the number of possible accounts for a user")
async def set_possible(ctx, user: Option(discord.Member, "User", required=True), amount: Option(int, "Amount of Accounts", required=True)):
    await cset_possible.execute(ctx, user, amount)


def setup(bot):
    bot.add_application_command(accountGroup)
