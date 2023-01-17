# Morb6

[hummusaki](https://github.com/Apoc101) and [Phil](https://github.com/Phil-Swift-Furry)

Configurable Discord Bot that sends "it's morbin time" and the amount of days that have passed since Morbius released every Friday at 5pm UTC, to get started use `m!help`

Why'd we make this? Because I've always wanted to learn about scheduling and I finally had a reason to do it, discovering a nearly 50 year old scheduling method called [cron](https://en.wikipedia.org/wiki/Cron), and Phil came up with the idea in the first place so props to him 👍👍<br>

If, for whatever reason, you want to host your instance of the bot just input the token into the `.env` file, install the required [dependencies](https://github.com/Apoc101/Morb6/blob/main/requirements.txt) and then run `bot.py`

## Possible improvements

- Use a noSQL DB like Mongo instead of a .txt file to make scaling easier in case people *really* like the bot
- Voice channel commands (pro)
- Format the messages in a nicer way
- Add the ability to make custom timers (DB required)
