# import stuff (obv)
import discord
import os
import aiocron
from dotenv import load_dotenv
import datetime
from discord.ext import commands
# load dotenv files from top directory
load_dotenv()

# check for event (ready)
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='Morbius'))
    
    print('Connected to bot: {}'.format(bot.user.name))
    print('Bot ID: {}'.format(bot.user.id))
    
# sets channel and format (yes this is custom to a few servers)
ID1=869743854964846634
ID2=979421338387222648
ID3=898141938534981673
date_format = "%m/%d/%Y"

# on cron time ready
@aiocron.crontab('0 17 * * fri') # Every friday at 5pm UTC
async def cornjob1():
    # calculate difference in dates
    today = datetime.date.today()
    morbius = datetime.date(2022, 3, 31)
    diff = today - morbius
    # set the channel for the bot's context
    ch1 = bot.get_channel(ID1)
    ch2 = bot.get_channel(ID2)
    ch3 = bot.get_channel(ID3)
    chs = [ch1, ch2, ch3]
    for x in chs:
        # async function completion: send string in bot's contexted channel
        await x.send('Its morbin time, it has been ' + str(diff.days) + ' days since Morbius released.')

# run the bot with the dotenv-provided token
bot.run(DISCORD_TOKEN)
