import discord
import random
import os
import aiocron
from dotenv import load_dotenv
import datetime
from discord.ext import commands
# load dotenv files for token (optional)
load_dotenv()


# load the token and instantiate the bot
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
bot = commands.Bot(command_prefix='m!',intents=discord.Intents.all())



# on bot load ready send some messages in terminal
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='Morbius in 4k'))
    print('Connected to bot: {}'.format(bot.user.name))
    print('Bot ID: {}'.format(bot.user.id))

# ------------------------------------- #
#               COMMANDS                #


# ------------------
# Channel ID Library

#grab current chID for library
@bot.command()
async def ch(ctx):
    chID = ctx.channel.id
    await WTTF(chID, ctx)

#check for duplicates and append chID into library
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


# -------------
# Timed message

# DRY implementation
def dateTime():
    today = datetime.date.today()
    morbius = datetime.date(2022, 3, 31)
    diff = today - morbius
    return diff

#on cron time ready
@aiocron.crontab('0 17 * * fri') # Every friday at 5pm UTC
async def cornjob1():
    # calculate difference in dates
    diff = dateTime()

    # set the channel for the bot's context
    with open('chnl.txt', 'r') as f:
      chs = f.readlines()
    for x in chs: #send message in every channel id in library
        await bot.get_channel(int(x)).send('Its morbin time, it has been ' + str(diff.days) + ' days since Morbius released.')

#test command
@bot.command()
async def date(ctx):
    diff = dateTime()
    with open('chnl.txt', 'r') as f:
        chs = f.readlines()
    for x in chs:
        await bot.get_channel(int(x)).send('Its morbin time, it has been ' + str(diff.days) + ' days since Morbius released.')

# --------------
# Misc. commands

# |gif command start|

#funny gif command reference
def get_nostalgia():
    with open('nosgifs.txt', 'r') as f:
        nostalgia = random.choice(f.readlines())
    return nostalgia

#hacky error fix
prev_nostalgia = ''

#random func
@bot.event
async def on_message(message):
    if bot.user.id != message.author.id:
        if ('old') in message.content.lower():
            global prev_nostalgia
            nostalgia = get_nostalgia()
            while nostalgia == prev_nostalgia:
                nostalgia = get_nostalgia()
            prev_nostalgia = nostalgia
            await message.channel.send(nostalgia)
    await bot.process_commands(message)

# |gif command end|

# run the bot with the dotenv-provided token
bot.run(DISCORD_TOKEN)