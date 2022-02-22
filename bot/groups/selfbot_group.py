import discord
import commands.selfbot.start as cstart
import commands.selfbot.stop as cstop
from discord.commands import Option
selfbotGroup = discord.SlashCommandGroup(
    name="selfbot", description="Selfbot Managment", guild_ids=[940315647064277022])


@selfbotGroup.command(guild_ids=[940315647064277022])
async def start(ctx, name: Option(str, "Alt Name", required=True)):
    await cstart.execute(ctx, name)

@selfbotGroup.command(guild_ids=[940315647064277022])
async def stop(ctx, name: Option(str, "Alt Name", required=True)):
    await cstop.execute(ctx, name)


def setup(bot):
    bot.add_application_command(selfbotGroup)
