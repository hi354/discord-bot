from email.message import Message
from pydoc import describe
from turtle import title
import discord
from discord.ext import commands
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions
import asyncio
 
intents = discord.Intents.default()
intents.members = True
 
client = commands.Bot(command_prefix = '-', intents = intents)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game('Visual Studio Code'))
    print("Bot is online")
    print("___________________")

@client.event
async def on_member_join(member):
    await member.send(f'Hi {member.mention}! Welcome to our server, in 20 seconds you will get "Member" role, which will give you access to the rest of the server, please read the rules in that time.')
    await asyncio.sleep(20)
    verifiedRole = discord.utils.get(member.guild.roles, id = 943770929689931846)
    await member.add_roles(verifiedRole)

@client.command()
async def hello(ctx):
    await ctx.channel.send(f"Hello! {ctx.author.mention}")


@client.command()
@has_permissions(kick_members = True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.channel.send(f"{member} has succesfully been kicked!")

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.channel.send("Sorry you don't have the required permissions to run this command!")

@client.command()
@has_permissions(ban_members = True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.channel.send(f"{member} has succesfully been banned!")

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.channel.send("Sorry you don't have the required permissions to run this command!")

@client.command()
@has_permissions(ban_members = True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminater = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminater):
            await ctx.guild.unban(user)
            await ctx.send(f"Unbanned {user.mention}!")

@unban.error
async def unban_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.channel.send("Sorry, You do not have the required permissions to run this command!")

@client.command()
async def showerthoughts(ctx):
    await ctx.channel.send("Falling over and getting hit by a planet are the same thing!!")

@client.command()
async def testing_embed(ctx, user: discord.Member, *, message=None):
    message = "Welcome to our server!"
    embed = discord.Embed(title=message, description="This server is for gamers of all types to come and make new friends!")
    await user.send(embed=embed)
    await ctx.channel.send(f"Sent DM to {user}.")





client.run('OTQ1NzU5MTUwOTA0ODQ4NDQ0.YhU02A.lkdA7emZkWlNPPuYLNLl8Kony7s')