#!/usr/bin/env python
import discord, request, time, os
from discord.flags import Intents
from discord.ext import commands

#! ==
#! Bot frontend
#// install "Better Comments" extension to have color coded commments
#// for clearer code understanding.
#! ==

#?    _       _ _   _       _ _
#?   (_)_ __ (_) |_(_) __ _| (_)_______
#?   | | '_ \| | __| |/ _` | | |_  / _ \
#?   | | | | | | |_| | (_| | | |/ /  __/
#?   |_|_| |_|_|\__|_|\__,_|_|_/___\___|
#?
#* functions to set up the bot

#! Initial configs
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = r')', intents = intents)
client.remove_command("help")


#! PRINT MESSAGE ON ACTIVATION
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="over the server"))
    print("ciao")


#! ==

#?    ____ _                            _   ___ ____      
#?   / ___| |__   __ _ _ __  _ __   ___| | |_ _|  _ \ ___ 
#?  | |   | '_ \ / _` | '_ \| '_ \ / _ \ |  | || | | / __|
#?  | |___| | | | (_| | | | | | | |  __/ |  | || |_| \__ \
#?   \____|_| |_|\__,_|_| |_|_| |_|\___|_| |___|____/|___/
#?                                                        
#* This bot isn't meant to be a commercial bot, therefore I've not added "set-up commands" (to avoid bloat).
#* Edit this part of the source code to configure Zella-bot for your server. [Suckless Ideology]

server_name = None                      #? replace with your server's name
main_channel_id = None                  #? replace with your general channel's ID
member_count_id = None                  #? replace with member count (voice) channel's ID 
confession_channel_id = None            #? replace with your confession channel's ID


#! ==

#?                _                        _   _
#?     __ _ _   _| |_ ___  _ __ ___   __ _| |_(_) ___  _ __
#?    / _` | | | | __/ _ \| '_ ` _ \ / _` | __| |/ _ \| '_ \
#?   | (_| | |_| | || (_) | | | | | | (_| | |_| | (_) | | | |
#?    \__,_|\__,_|\__\___/|_| |_| |_|\__,_|\__|_|\___/|_| |_|
#?
#* functions that will trigger automatically

#! update member count channel
def member_count(member):
    member_count_channel = member.guild.get_channel(member_count_id)
    return member_count_channel.edit(name=f'Members: {member.guild.member_count}')


#! User Join
@client.event
async def on_member_join(member):
    #! update member count
    await member_count(member)

    #! in server
    chit_chat = member.guild.get_channel(main_channel_id)
    embed=discord.Embed(title=f"Welcome to the {server_name}!", color=request.random_color())
    embed.set_author(name="Zella-bot")
    embed.add_field(name = f"🎋{member.name}🍡" , value=messages.welcome_server(member.mention))
    embed.set_thumbnail(url = member.avatar_url)
    embed.set_image(url = request.welcome_banner())
    await chit_chat.send(embed=embed)
    await chit_chat.send(member.mention, delete_after=1)


#! ==

#?                                                  _
#?     ___ ___  _ __ ___  _ __ ___   __ _ _ __   __| |___
#?    / __/ _ \| '_ ` _ \| '_ ` _ \ / _` | '_ \ / _` / __|
#?   | (_| (_) | | | | | | | | | | | (_| | | | | (_| \__ \
#?    \___\___/|_| |_| |_|_| |_| |_|\__,_|_| |_|\__,_|___/
#?
#* Commands which will be triggered by the user


#! YOUTUBE COMMAND
@commands.guild_only()
@client.command(aliases=['youtube', 'YOUTUBE'])
async def yt(ctx, *, query):
    await ctx.send(f"https://youtube.com/watch?v={request.youtube(query)}")


#! PING
@commands.guild_only()
@client.command()
async def ping(ctx):
    await ctx.send(f"📡 {int(client.latency * 1000)}m/s")


#! HELP
@client.command(aliases=['info', 'about', 'HELP'])
async def help(ctx):
    embed=discord.Embed(title="°✧ :noote_right: **HЄLPÐЄSK** :noote_left: ✧°", description=r"︶︶︶︶︶︶︶︶︶︶︶︶˚", color=request.random_color())
    embed.set_author(name="Zella-bot")
    embed.add_field(name="𝔸𝕓𝕠𝕦𝕥", value=request.about, inline=False)
    embed.add_field(name="ℂ𝕠𝕟𝕗𝕖𝕤𝕤𝕚𝕠𝕟", value=request.confessions, inline=False)
    embed.add_field(name="ℂ𝕠𝕞𝕞𝕒𝕟𝕕𝕤", value=request.commands)
    embed.set_footer(text='GitHub.com/ut-kr/Zella-Bot')
    await ctx.send(embed=embed)


#! CONFESSION COMMAND
@client.command(aliases=['listen', 'confession'])
async def confess(ctx, *, confession):
    channel = client.get_channel(confession_channel_id)
    user = channel.guild.get_member(ctx.message.author.id)

    if isinstance(ctx.channel, discord.channel.DMChannel):
        if (len(confession) > 15):
            
            unique_id = request.random_id()
            embed = discord.Embed(title=r"CONFESSION :leaves: ", description = confession, color=request.random_color())
            embed.set_author(name="Zella-bot")
            embed.set_footer(text=f"id: {unique_id}")
            await channel.send(embed=embed)
            await ctx.send(f":partying_face: Successfully posted your anonymous confession with the **id: {unique_id}** at <#{confession_channel_id}>")
        else:
            await ctx.send("your confession is quite too small :/")
    else:
        await ctx.send("make confessions in our DMS :wink: ")


#! pfp command
@client.command(aliases=['avatar', 'av'])
async def pfp(ctx, member=None):
    if not member:
        member = ctx.author
    else:
        if member[0] == "<":
            member = member[3:-1]
        member = int(member)
        member = client.get_user(member)

    if member == None:
        await ctx.send("user not found in the server :/")
    else:
        embed=discord.Embed(title=member.name, color=request.random_color())
        embed.set_author(name="Zella-bot")
        embed.set_image(url = member.avatar_url)
        await ctx.send(embed=embed)


#! ==

#?    ___ _ __ _ __ ___  _ __ ___
#?   / _ \ '__| '__/ _ \| '__/ __|
#?  |  __/ |  | | | (_) | |  \__ \
#?   \___|_|  |_|  \___/|_|  |___/
#?
#* instead of giving error messages on invalid syntax, bot will show commmand info


#! YT CMD INFO
@yt.error
async def youtube_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed=discord.Embed(title="YouTube", url="https://www.youtube.com", color=0xff0000)
        embed.set_author(name="Zella-bot")
        embed.set_thumbnail(url="https://img.talkandroid.com/uploads/2014/06/YouTube_App_Large_Icon-450x450.png")
        embed.add_field(name="About", value="Search youtube videos right here from discord!", inline=False)
        embed.add_field(name="Commands", value="`)yt {query}` | `)youtube {query}` | `)vid {query}`", inline=False)
        embed.set_footer(text="type )help for more info")
        await ctx.send(embed=embed)


#! CONFESSION INFO
@confess.error
async def confess_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed=discord.Embed(title="Confession", color=request.random_color())
        embed.set_author(name="Zella-bot")
        embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2013/07/13/12/47/girl-160326__340.png")
        embed.add_field(name="About", value="DM me your confession and I will post it in the confession channel anonymously ;)", inline=False)
        embed.add_field(name="DM Syntax", value="`)listen {message}` | `)confess {message}` | `)confession {message}`", inline=False)
        embed.set_footer(text="type )help for more info")
        await ctx.send(embed=embed)


#! INVALID COMMAND- SHOW MESSAGE HOW TO GET INVOLVED IN DEVELOPMENT AKA SHARE SUGGESTIONS
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed=discord.Embed(title="Command Not Found", description="The command you're trying does not exists....yet.\nAdd issues/PR on my GitHub if you have more suggestions", color=request.random_color())
        embed.set_author(name="Zella-bot")
        embed.set_thumbnail(url="https://i.pinimg.com/originals/6c/da/e5/6cdae5ec608d8df875c5766a5c24bf3e.png")
        embed.set_footer(text="type )help for all bot-commands")
        await ctx.send(embed=embed)


#! ==

client.run(os.environ['token'])