import discord
import subprocess
from discord.commands import Option
intents = discord.Intents.default()
intents.members = True
bot = discord.Bot(intents=intents)
bot.load_extension('groups.account_group')
bot.load_extension('groups.selfbot_group')


# Start API
subprocess.Popen("/usr/bin/node /config/workspace/api/index.js", shell=True)

# Log when ready


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


# Login as Bot
bot.run("OTM0MDgwNTY0Njg2OTEzNTQ2.Yeq4UA.mvRzCPI_PMITKzIhEcEDciwJ0b8")
