#=========================================================
#					Biblio
#=========================================================

import discord # Импортируем библиотеку дискорд
from discord.ext import commands 
from discord.utils import get
from config import config # импортируем переменную конфиг
import json
import random

#=========================================================
#					Events
#=========================================================

client = commands.Bot(command_prefix = config['prefix'])
client.remove_command('help')

@client.event
async def on_ready():
	print('[LOG] Bot a online!') # Пишем в консоль о том что бот работает

	await client.change_presence( status = discord.Status.online, activity = discord.Game('Discord')) # статус


#=========================================================
#					Code
#=========================================================
#=========================================================
#					Команда "Kick"
#=========================================================
@client.command(pass_context = True)
@commands.has_permissions( administrator = True)
async def kick(ctx, member: discord.Member = None, *, reason):
	await ctx.channel.purge( limit = 1)
	await member.kick( reason = reason)
	await ctx.send(embed = discord.Embed(
		title = f"""Kick""",
		description = f"""
		Бот кикнул пользователя {member.mention}. Причина: {reason}
		Попросил: {ctx.author.mention}""",
		color = 15158332,
		inline = False
		))
#=========================================================
#					Команда "Ban"
#=========================================================
@client.command(pass_context = True)
@commands.has_permissions( administrator = True)
async def ban( ctx, member: discord.Member, *, reason):
	await ctx.channel.purge( limit = 1)
	await member.ban( reason = reason)
	await ctx.send(embed = discord.Embed(
		title = f"""Ban""",
		description = f"""
		Бот забанил игрока {member.mention}. Причина: {reason}
		Попросил: {ctx.author.mention}""",
		color = 15158332,
		inline = False
		))
#=========================================================
#					Команда "Mute"
#p.s. создайте роль "Mute" для начала
#=========================================================
@client.command(pass_context = True)
@commands.has_permissions( administrator = True)
async def mute( ctx, member: discord.Member, reason):
	await ctx.channel.purge( limit = 1)
	mute_role = discord.utils.get(ctx.message.guild.roles, name = 'Mute')

	await member.add_roles(mute_role)
	await ctx.send(embed = discord.Embed(
		title = f"""Mute""",
		description = f"""
		Бот дал мут игроку {member.mention}. Причина: {reason}
		Попросил: {ctx.author.mention}""",
		color = 15158332,
		inline = False
		))	

#=========================================================
#					Команда "Unmute"
#=========================================================
@client.command(pass_context = True)
@commands.has_permissions( administrator = True)
async def unmute( ctx, member: discord.Member, reason):
	await ctx.channel.purge( limit = 1)
	mute_role = discord.utils.get(ctx.message.guild.roles, name = 'Mute')

	await member.remove_roles(mute_role)
	await ctx.send(embed = discord.Embed(
		title = f"""Unmute""",
		description = f"""
		Бот убрал мут с игрока {member.mention}. Причина: {reason}
		Попросил: {ctx.author.mention}""",
		color = 15158332,
		inline = False
		))	
#=========================================================
#					Команда "Unban"
#=========================================================
@client.command(pass_context = True)
@commands.has_permissions( administrator = True)
async def unban(ctx, *, member, reason):
	await ctx.channel.purge( limit = 1)
	banned_users = await ctx.guild.bans()

	for banned_entry in banned_users:
		user = banned_entry.user

		await ctx.guild.unban(user)
		await ctx.send(embed = discord.Embed(
		title = f"""Unban""",
		description = f"""
		Бот разбанил игрока {member.mention}. Причина: {reason}
		Попросил: {ctx.author.mention}""",
		color = 15158332,
		inline = False
		))	

		return

#=========================================================
#					Команда "Clear"
#=========================================================
@client.command()
@commands.has_permissions( administrator = True)
async def clear(ctx, amount=5):
	await ctx.channel.purge(limit=amount)

#=========================================================
#					Команда "changestatus"
#=========================================================
@client.command()
@commands.has_permissions( administrator = True )
async def changestatus( ctx, statustype:str = None, *, arg:str = None):
    if statustype is None: # Type Check
        await ctx.send( 'Вы не указали тип Статуса' )
    elif arg is None: # Arg Check
        await ctx.send( 'Вы не указали нужный аргумент' )
    else:
        if statustype.lower() == 'game': # Game
            await Bot.change_presence (activity=discord.Game( name = arg) )
        elif statustype.lower() == 'listen': # Listen
            await Bot.change_presence( activity=discord.Activity( type=discord.ActivityType.listening, name = arg) )
        elif statustype.lower() == 'watch': # Watch
            await Bot.change_presence( activity=discord.Activity( type=discord.ActivityType.watching, name = arg) )
#=========================================================
#					Run a bot
#=========================================================
client.run(config['token'])
