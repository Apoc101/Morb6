import discord
import os
import aiocron
from dotenv import load_dotenv
import datetime
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
bot = discord.Client()


@bot.event
async def on_ready():
	guild_count = 0

	for guild in bot.guilds:
		print(f"- {guild.id} (name: {guild.name})")

		guild_count = guild_count + 1
	print("SampleDiscordBot is in " + str(guild_count) + " guilds.")
today = datetime.date.today()
morbius = datetime.date(2022, 3, 31)
diff = today - morbius
print(diff.days)

CHANNEL_ID=869743854964846634
date_format = "%m/%d/%Y"

@aiocron.crontab('*/5 * * * *')
async def cornjob1():
    today = datetime.date.today()
    morbius = datetime.date(2022, 3, 31)
    diff = today - morbius
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send('Its morbin time, it has been ' + str(diff.days) + ' days since Morbius released.')

bot.run(DISCORD_TOKEN)