from discord.ext import commands
import os
import random
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.event
async def on_message(message):
    if message.content.startswith("/ping"):
        await message.channel.send("pong")
    if message.comtent.startswith("/dice "):
    	await message.channel.send(message.content)

bot.run(token)
