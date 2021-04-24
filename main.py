import art # ascii text art
import datetime # date and time
import discord # discord.py library
from discord.ext import commands # discord.py commands extension
from keepAlive import keepAlive # uptime script
import os # retrieving bot token
import random # random library

"""
command_prefix: the prefix for the bot's commands
intents = the assigned intents the bot has
case_insensitive = a boolean feature to allow case insensitivity when calling commands (ex: !helP would function)
"""
bot = commands.Bot(command_prefix = "!", case_insensitive = True)

# bot initialization
@bot.event
async def on_ready():
	# prints the bot's username in ASCII text art
	art.tprint(bot.user.name)
	
	# changes the status of the bot
	await bot.change_presence(status = discord.Status.online, activity = discord.Activity(type = discord.ActivityType.watching, name = "this Server"))

# error handler
@bot.event
async def on_command_error(ctx, error):
	await ctx.trigger_typing()
	await ctx.send(f"```{error}```")

# hello command
@bot.command()
async def hello(ctx):
	await ctx.trigger_typing()
	await ctx.send(f"Hello there, {ctx.author.mention}!")
	print("[COMMAND] Hello")

# ping command
@bot.command()
async def ping(ctx):
	await ctx.trigger_typing()
	await ctx.send(f":satellite: The latency is `{round(bot.latency * 1000)}`ms")
	print("[COMMAND] Ping")

# predict command
@bot.command(aliases = ["8ball"])
async def predict(ctx, *, question):
	await ctx.trigger_typing()
	responses = ["Yes", "Maybe", "No"]
	response = random.choice(responses)
	await ctx.send(f":8ball: {response}")
	print("[COMMAND] Predict")

# color command
@bot.command()
async def color(ctx, hexCode: discord.Color):
	await ctx.trigger_typing()
	embed = discord.Embed(title = ":trackball: Color Search", description = str(hexCode).lower(), color = hexCode, timestamp = datetime.datetime.utcnow())
	embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
	embed.set_image(url = f"https://www.colorhexa.com/{str(hexCode).lower()[1:]}.png")
	await ctx.send(embed = embed)

# direct message command
@bot.command()
async def dm(ctx, member: discord.Member, *, message):
	await ctx.trigger_typing()
	await member.send(message)
	await ctx.send(":white_check_mark: Sent!")

keepAlive()
bot.run(os.environ["token"], bot = True, reconnect = True)
