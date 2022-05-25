# import stuff (obv)
import discord
import os
import aiocron
from dotenv import load_dotenv
import datetime
# load dotenv files from top directory
load_dotenv()

# get the token and instantiate the bot
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
bot = discord.Client()

# check for event (ready)
@bot.event
async def on_ready():
	guild_count = 0

	for guild in bot.guilds:
		print(f"- {guild.id} (name: {guild.name})")

		guild_count = guild_count + 1
    # print n of discord servers the bot is in (acts as a pseudo-"ready")
	print("Morb6 is in " + str(guild_count) + " guilds.")
# prints the amount of days morbius has been out just in case
today = datetime.date.today()
morbius = datetime.date(2022, 3, 31)
diff = today - morbius
print(diff.days)

# sets channel and format (yes this is custom to a server)
CHANNEL_ID=869743854964846634
date_format = "%m/%d/%Y"

# on cron time ready
@aiocron.crontab('0 17 * * fri')
async def cornjob1():
    # calculate difference in dates
    today = datetime.date.today()
    morbius = datetime.date(2022, 3, 31)
    diff = today - morbius
    # set the channel for the bot's context
    channel = bot.get_channel(CHANNEL_ID)
    # async function completion: send string in bot's contexted channel
    await channel.send('Its morbin time, it has been ' + str(diff.days) + ' days since Morbius released.')

# run the bot with the dotenv-provided token
bot.run(DISCORD_TOKEN)