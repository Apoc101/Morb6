# import stuff (obv)
import discord
import os
import aiocron
from dotenv import load_dotenv
import datetime
from discord.ext import commands
# load dotenv files from top directory
load_dotenv()

# get the token and instantiate the bot
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
bot = commands.Bot(command_prefix='m!',intents=discord.Intents.all())

# check for event (ready)
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='Morbius in 4k'))
    
    print('Connected to bot: {}'.format(bot.user.name))
    print('Bot ID: {}'.format(bot.user.id))

#grab chID for library
@bot.command()
async def ch(ctx):
    chID = ctx.channel.id
    await WTTF(chID, ctx)
    

#append chID into library
async def WTTF(chID, ctx):
    with open('chnl.txt', 'r+') as f:
        match = False
        for line in f:
            if int(line) == int(chID):
                match = True
        if match == False:
            f.write(f'\n{chID}')
            await ctx.send(f'Succesfully added <#{chID}>.')
        else: 
            await ctx.send(f'<#{chID}> is already in our database!')

# on cron time ready
date_format = "%m/%d/%Y"
@aiocron.crontab('0 17 * * fri') # Every friday at 5pm UTC
async def cornjob1():
    # calculate difference in dates
    today = datetime.date.today()
    morbius = datetime.date(2022, 3, 31)
    diff = today - morbius

    # set the channel for the bot's context
    with open('chnl.txt', 'r') as f:
      chs = f.readlines()
    for x in chs:
        # async function completion: send string in bot's contexted channel
        await bot.get_channel(int(x)).send('Its morbin time, it has been ' + str(diff.days) + ' days since Morbius released.')

# test command
@bot.command()
async def test(ctx):
    today = datetime.date.today()
    morbius = datetime.date(2022, 3, 31)
    diff = today - morbius
    with open('chnl.txt', 'r') as f:
        chs = f.readlines()
    for x in chs:
        await bot.get_channel(int(x)).send('Its morbin time, it has been ' + str(diff.days) + ' days since Morbius released.')

# run the bot with the dotenv-provided token
bot.run(DISCORD_TOKEN)