prefix = "~"
import random
import asyncio
import urllib.request
from bs4 import BeautifulSoup    
import os
import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord import Game
import logging
import json
import aiohttp
bot = commands.Bot(command_prefix=prefix, self_bot=False)
bot.remove_command("help")
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online,activity=Game(name='Type '+bot.command_prefix+'help for help'))
    global amounts
    try:
        with open('amounts.json') as f:
            amounts = json.load(f)
    except FileNotFoundError:
        amounts = {}
    print("Ready to troll")

@bot.command()
async def help(ctx,comm=""):
    if comm.lower()== "kall":
        embed=discord.Embed(
            description="Kicks all users the bot has permission to kick.",
            color=discord.Color.blue()
            )
        embed.set_author(name="kall")
        await ctx.send(embed=embed) 
    elif comm.lower()== "ball":
        embed=discord.Embed(
            description="Bans all users the bot has permission to ban.",
            color=discord.Color.blue()
            )
        embed.set_author(name="ball")
        await ctx.send(embed=embed)
    elif comm.lower()== "ban":
        embed=discord.Embed(
            description="Bans the specified user from the server.",
            color=discord.Color.blue()
            )
        embed.set_author(name="ban")
        embed.add_field(name="Usage",value="`ban <member> [reason]`",inline=False)
        await ctx.send(embed=embed) 
    elif comm.lower()== "kick":
        embed=discord.Embed(
            description="Kicks the specified user from the server.",
            color=discord.Color.blue()
            )
        embed.set_author(name="kick")
        embed.add_field(name="Usage",value="`kick <member>`",inline=False)
        await ctx.send(embed=embed) 
    elif comm.lower()== "unban":
        embed=discord.Embed(
            description="Unbans the specified user ID from the server.",
            color=discord.Color.blue()
            )
        embed.set_author(name="unban")
        embed.add_field(name="Usage",value="`unban <userID>`",inline=False)
        await ctx.send(embed=embed) 
    elif comm.lower()== "rall":
        embed=discord.Embed(
            description="Renames every user the bot has permission to rename in the server.",
            color=discord.Color.blue()
            )
        embed.set_author(name="rall")
        embed.add_field(name="Usage",value="`rall [nickname]`",inline=False)
        await ctx.send(embed=embed)
    elif comm.lower()== "dall":
        embed=discord.Embed(
            description="Deletes everything in the stated condition the bot has permission to delete in the server.",
            color=discord.Color.blue()
            )
        embed.set_author(name="dall")
        embed.add_field(name="Usage",value="`dall <condition>`",inline=True)
        embed.add_field(name="Conditons",value="`channels,roles,emojis,all`",inline=True)
        await ctx.send(embed=embed)
    elif comm.lower()== "destroy":
        embed=discord.Embed(
            description="Deletes everything in the server the bot has permission to and bans every user the bot can ban.",
            color=discord.Color.blue()
            )
        embed.set_author(name="destroy")
        await ctx.send(embed=embed)
    elif comm.lower()== "purge":
        embed=discord.Embed(
            description="Deletes the specified amount of messages.",
            color=discord.Color.blue()
            )
        embed.set_author(name="purge")
        embed.add_field(name="Usage",value="`purge <limit>`")
        await ctx.send(embed=embed)
    elif comm.lower()== "prefix":
        embed=discord.Embed(
            description="Changes the bot's prefix. If left with no condition it changes it back to the default prefix '~'.",
            color=discord.Color.blue()
            )
        embed.set_author(name="prefix")
        embed.add_field(name="Usage",value="`prefix [new prefix]`")
        await ctx.send(embed=embed)
    elif comm.lower()== "8ball":
        embed=discord.Embed(
            description="Reaches into the future to find the answer to your question.",
            color=discord.Color.blue()
            )
        embed.set_author(name="8ball")
        embed.add_field(name="Usage",value="`8ball [question]`")
        await ctx.send(embed=embed)
    elif comm.lower()== "say":
        embed=discord.Embed(
            description="Make the bot say whatever you want.",
            color=discord.Color.blue()
            )
        embed.set_author(name="say")
        embed.add_field(name="Usage",value="`say [message]`")
        await ctx.send(embed=embed)
    elif comm.lower()== "image":
        embed=discord.Embed(
            description="Sends an image with the given tags, if no tag is given sends a random image.(May not work if there are porblems with files being sent in discord)",
            color=discord.Color.blue()
            )
        embed.add_field(name="Usage",value="`image [tags]`")
        embed.set_author(name="image")
        await ctx.send(embed=embed)
    elif comm.lower()== "gif":
        embed=discord.Embed(
            description="Sends a gif with the given tags, if no tag is given sends a random gif.(May not work if there are porblems with files being sent in discord)",
            color=discord.Color.blue()
            )
        embed.add_field(name="Usage",value="`gif [tags]`")
        embed.set_author(name="gif")
        await ctx.send(embed=embed)
    elif comm.lower()== "insult":
        embed=discord.Embed(
            description="Sends a random insult.",
            color=discord.Color.blue()
            )
        embed.set_author(name="insult")
        embed.add_field(name="Usage",value="`insult [target]`")
        await ctx.send(embed=embed)
    elif comm.lower()== "balance":
        embed=discord.Embed(
            description="Says how many slaves the mentioned member has. If left empty it will say how many slaves you have.",
            color=discord.Color.blue()
            )
        embed.set_author(name="balance")
        embed.add_field(name="Usage",value="`balance <member>`")
        await ctx.send(embed=embed)
    elif comm.lower()== "transfer":
        embed=discord.Embed(
            description="Transfers the given amount to the mentioned member, if you have enough slaves to do that.",
            color=discord.Color.blue()
            )
        embed.set_author(name="transfer")
        embed.add_field(name="Usage",value="`transfer <member> [amount]`")
        await ctx.send(embed=embed)
    elif comm.lower()== "roulette":
        embed=discord.Embed(
            description="Spins the roullete. Minimum bet is 1 slave.",
            color=discord.Color.blue()
            )
        embed.set_author(name="roulette")
        embed.add_field(name="Usage",value="`roulette <color> [bet]`")
        embed.add_field(name="Colors",value="`red`,`black`,`green`")
        await ctx.send(embed=embed)
    elif comm.lower()== "coinflip" or comm.lower()== "cf":
        embed=discord.Embed(
            description="Flips a coin. You can bet slaves on the outcome.",
            color=discord.Color.blue()
            )
        embed.set_author(name="coinflip")
        embed.add_field(name="Usage",value="`coinflip`\n`coinflip <heads/tails> [bet]`")
        embed.add_field(name="Aliases",value="`cf`")
        await ctx.send(embed=embed)
    elif comm.lower()== "messagelog":
        embed=discord.Embed(
            description="Enables/disables the message log in a given channel.",
            color=discord.Color.blue()
            )
        embed.set_author(name="messagelog")
        embed.add_field(name="Usage",value="`messagelog <enable/disable> [channel]`")
        await ctx.send(embed=embed)
    elif comm.lower()== "modlog":
        embed=discord.Embed(
            description="Enables/disables the mod log in a given channel.",
            color=discord.Color.blue()
            )
        embed.set_author(name="modlog")
        embed.add_field(name="Usage",value="`modlog <enable/disable> [channel]`")
        await ctx.send(embed=embed)
    elif comm.lower()== "loginlog":
        embed=discord.Embed(
            description="Enables/disables the mod log in a given channel.",
            color=discord.Color.blue()
            )
        embed.set_author(name="loginlog")
        embed.add_field(name="Usage",value="`loginlog <enable/disable> [channel]`")
        await ctx.send(embed=embed)
    elif comm.lower()== "help":
        embed=discord.Embed(
            description="Provides you with the commands list.\nDo help <command> for extended command info.",
            color=discord.Color.blue()
            )
        embed.set_author(name="help")
        embed.add_field(name="Usage",value="`help [command]`")
        await ctx.send(embed=embed)
    elif comm=="":
        embed=discord.Embed(
            color=discord.Color.blue()
            )
        embed.set_author(name="Help")
        embed.add_field(name="Moderator suff", value="`kick`,`ban`,`unban`,`purge`,`prefix`",inline=False)
        embed.add_field(name="Destructive stuff", value="`kall`,`ball`,`rall`,`dall`,`destroy`",inline=False)
        embed.add_field(name="Fun stuff", value="`8ball`,`say`,`image`,`gif`,`insult`",inline=False)
        embed.add_field(name="Currency stuff", value="`balance`,`transfer`,`roulette`,`coinflip`",inline=False)
        embed.add_field(name="Utility stuff", value="`messagelog`,`modlog`,`loginlog`",inline=False)
        embed.set_footer(text="To get more info on a command, do "+bot.command_prefix+"help command name")

        msg=await ctx.send("React with 📫, to get the list of commands in your DMs or with 🏠 to get it here.")
        await discord.Message.add_reaction(msg,"📫")
        await discord.Message.add_reaction(msg,"🏠")

        def check(reaction,user):
            if user == ctx.message.author :
                if str(reaction.emoji) == '📫':
                    return user == ctx.author and str(reaction.emoji) == '📫'
                elif str(reaction.emoji) == '🏠':
                    return user == ctx.author and str(reaction.emoji) == '🏠'
        try:
            reaction, user = await bot.wait_for('reaction_add',timeout=60.0,check=check)
        except asyncio.TimeoutError:
            await ctx.send('Canceling the command.')
        else:
            if(str(reaction)=="📫"):
                await ctx.send("The command list will be sent to your DMs.")
                await ctx.author.send(embed=embed)
            elif(str(reaction)=="🏠"):
                await ctx.send("The command list will be sent here")
                await ctx.send(embed=embed)    
    else:
        await ctx.send("No such command found!")

@bot.command()
async def prefix(ctx,*,nprefix="~"):
    nprefix = nprefix.strip()
    bot.command_prefix=nprefix
    return await ctx.send(ctx.author.mention+" has changed the prefix to "+nprefix)

@bot.command()
async def say(ctx,*,msg):
    await ctx.send(msg)
    await ctx.message.delete()

@bot.command(aliases = ['bean'])
async def ban(ctx, member:discord.User = None, *, reason = None):
    if member == None:
        await ctx.channel.send("You need to pick a user to ban!")
    elif member == ctx.message.author:
        await ctx.channel.send("You cannot ban yourself!")
    if reason == None:
        reason = "Various reasons"
    message = "You have been banned from "+ctx.guild.name+" for "+reason+"!"
    try:
        await member.send(message)
    except:
        pass
    await ctx.guild.ban(member)
    await ctx.channel.send(member.name+" has been banned!")
    print (member.name+" has been banned from "+ctx.guild.name+"!")

@bot.command()
async def unban(ctx,id:int):
    user = await bot.fetch_user(id)
    await ctx.guild.unban(user)
    await ctx.send(user.name+" has been unbanned!")
    print (user.name+" has been unbanned from "+ctx.guild.name+"!")

@bot.command()
async def kick(ctx, member:discord.User = None):
    if member == None:
        await ctx.channel.send("You need to pick a user to kick!")
    elif member == ctx.message.author:
        await ctx.channel.send("You cannot kikc yourself!")
    await ctx.guild.kick(member)
    await ctx.send(member.name+" has been kicked!")
    print(member.name+" has been kicked from "+ctx.guild.name+"!")

@bot.command()
async def kall(ctx):
    if ctx.author.guild_permissions.kick_members:
        for member in ctx.guild.members:
            try:
                await member.kick()
                print (member.name+" has been kicked from "+ctx.guild.name)
            except:
                pass    
        return await ctx.send(ctx.author.mention+" has kicked everyone.")
    else:
        return await ctx.send("You don't have permission to do that!")

@bot.command()
async def ball(ctx):
    if ctx.author.guild_permissions.ban_members:
        for member in ctx.guild.members:
            try:
               await member.bad()
               print (member.name+" has been banned from "+ctx.guild.name)
            except:
                pass    
        return await ctx.send(ctx.author.mention+" has banned everyone.")
    else:
        return await ctx.send("You don't have permission to do that!")

@bot.command()
async def rall(ctx,*,rename_to=""):
    if ctx.author.guild_permissions.manage_nicknames:
        for member in ctx.guild.members:
            try:
                await member.edit(nick=rename_to)
                print (member.name+" has been renamed to " + str(rename_to) + " in " +ctx.guild.name)
            except:
                pass
    else:
        return await ctx.send(ctx.author.mention+" you don't have permission to do that!")

@bot.command()
async def dall(ctx, condition=""):
    if condition.lower() == "channels":
        if ctx.author.guild_permissions.manage_channels:
            for channel in ctx.guild.channels:
                try:
                    await channel.delete()
                    print (channel.name + " has been deleted in " + ctx.guild.name)
                except:
                    pass
        else:
            return await ctx.send(ctx.author.mention+", you don't have permission to do that!")

    elif condition.lower() == "roles":
        if ctx.author.guild_permissions.manage_roles:
            for role in ctx.guild.roles:
                try:
                    await role.delete()
                    print (role.name + " has been deleted in " + ctx.guild.name)
                except:
                    pass
            return await ctx.send(ctx.author.mention+" has deleted all roles.")
        else:
            return await ctx.send(ctx.author.mention+", you don't have permission to do that!")

    elif condition.lower() == "emojis":
        if ctx.author.guild_permissions.manage_emojis:
            for emoji in ctx.guild.emojis:
                try:
                    await emoji.delete()
                    print (emoji.name + " has been deleted in " + ctx.guild.name)
                except:
                    pass
                return await ctx.send(ctx.author.mention+" has deleted all emojis.")
        else:
            return await ctx.send(ctx.author.mention+", you don't have permission to do that!")
            
    elif condition.lower() == "all":
        if ctx.author.guild_permissions.manage_emojis&ctx.author.guild_permissions.manage_roles&ctx.author.guild_permissions.manage_channels:
            for emoji in ctx.guild.emojis:
                try:
                    await emoji.delete()
                    print (emoji.name + " has been deleted in " + ctx.guild.name)
                except:
                    pass

            for channel in ctx.guild.channels:
                try:
                    await channel.delete()
                    print (channel.name + " has been deleted in " + ctx.guild.name)
                except:
                    pass

            for role in ctx.guild.roles:
                try:
                    await role.delete()
                    print (role.name + " has been deleted in " + ctx.guild.name)
                except:
                    pass
        else:
            return await ctx.send(ctx.author.mention+", you don't have permission to do that!")
    else:
        return await ctx.send(ctx.author.mention+", you have to choose one of the following condition- channels, roles, emojis or all!")

@bot.command()
async def destroy(ctx):
    if ctx.author.guild_permissions.administrator:

        for emoji in ctx.guild.emojis:
            try:
                await emoji.delete()
                print (emoji.name + " has been deleted in " + ctx.guild.name)
            except:
                pass

        for channel in ctx.guild.channels:
            try:
                await channel.delete()
                print (channel.name + " has been deleted in " + ctx.guild.name)
            except:
                pass

        for role in ctx.guild.roles:
            try:
                await role.delete()
                print (role.name + " has been deleted in " + ctx.guild.name)
            except:
                pass

        for member in ctx.guild.members:
            try:
               await member.ban()
               print (member.name + " has been banned from " + ctx.guild.name)
            except:
               pass
    else:
        return await ctx.send("You don't have permission to do that!")

@bot.command()
async def insult(ctx,*,args=''):
    html = urllib.request.urlopen("https://insult.mattbas.org/api/insult.html").read()
    soup = BeautifulSoup(html,"html.parser")
    insult_text = soup.find('h1')
    return await ctx.send(args+" "+insult_text.text)

@bot.command()
async def image(ctx, *, search=""):
    embed = discord.Embed()
    if search == '':
        response="https://loremflickr.com/320/240?random="+str(random.randint(1,10000))
        embed.set_image(url=response)
    else:
        try:
            session = aiohttp.ClientSession()
            search.replace(' ', ',')
            response=await session.get("https://loremflickr.com/json/320/240/"+search+"/all")
            data = json.loads(await response.text())
            embed.set_image(url=data["file"])
            await session.close()
        except:
            return await ctx.send("Couldn't find image with the given tag or something went wrong.")
    await ctx.send(embed=embed)

@bot.command()
async def gif(ctx, *, search=""):
    embed = discord.Embed()
    session = aiohttp.ClientSession()
    flag=1
    if search == '':
        response = await session.get('https://api.giphy.com/v1/gifs/random?api_key=qcC6nU945riNO4xoV4ZYU63rYBadeaeQ')
        data = json.loads(await response.text())
        embed.set_image(url=data['data']['images']['original']['url'])
    else:
        try:
            search.replace(' ', '+')
            response = await session.get('http://api.giphy.com/v1/gifs/search?q=' + search + '&api_key=qcC6nU945riNO4xoV4ZYU63rYBadeaeQ&limit=10')
            data = json.loads(await response.text())
            gif_choice = random.randint(0, 9)
            embed.set_image(url=data['data'][gif_choice]['images']['original']['url'])
        except:
            await ctx.send("Couldn't find gifs with the given tag or something went wrong.")
            flag=0
    await session.close()
    if(flag):
        await ctx.send(embed=embed)

@bot.command(aliases=["8ball"])
async def _8ball(ctx,*,question):
    responses=['It is certain.',
               'It is decidedly so.',
               'Without a doubt.',
               'Yes – definitely.',
               'You may rely on it.',
               'As I see it, yes.',
               'Most likely.',
               'Outlook good.',
               'Yes.',
               'Signs point to yes.',
               'Reply hazy, try again',
               'Ask again later.',
               'Better not tell you now.',
               'Cannot predict now.',
               'Concentrate and ask again.',
               'Don\'t count on it.',
               'My reply is no.',
               'My sources say no.',
               'Outlook not so good.',
               'Very doubtful.',]
    embed=discord.Embed(
        color=discord.Color.red()
        )
    embed.set_author(name="8ball")
    embed.add_field(name=question, value=random.choice(responses),inline=True)
    await ctx.send(embed=embed)
@bot.command()
async def purge(ctx,amount=1):
    amount=int(amount)
    await ctx.message.delete()
    await ctx.channel.purge(limit=amount)
    await ctx.send("Cleared by "+ctx.author.mention)

@bot.command(aliases = ['cf'])
async def coinflip(ctx,side="",bet=0):
    sides=['heads','tails']
    landed=random.choice(sides)
    id=str(ctx.message.author.id)
    if amounts[id] < bet:
        await ctx.send("You need "+str(bet-amounts[id])+" more slaves to do that!")
    elif bet==0:
        await ctx.send("It landed on "+landed)
    elif bet<10 and bet!=0:
        await ctx.send("The minimum bet is 10 slaves!")
    else:
        amounts[id]-=bet
        await ctx.send("It landed on "+landed)
        if (side.lower()=="heads" and landed=="heads") or (side.lower()=="tails" and landed=="tails"):
            amounts[id]+=2*bet
            await ctx.send("Congrats "+ctx.author.mention+", you won: "+str(2*bet))
        else:
            await ctx.send("Oof "+ctx.author.mention+", you lost "+str(bet)+" slaves. Good luck next time!")
        _save()
@bot.command()
async def messagelog(ctx,status="",channel=""):
    try:
        channel=channel.replace("<","")
        channel=channel.replace(">","")
        channel=channel.replace("#","")
        channel=int(channel)
        channel=bot.get_channel(channel)
    except:
        await ctx.send("Not a valid channel.")
    if status.lower()=='enable':
        await ctx.send("Starting message log in "+channel.mention)
        @bot.event
        async def on_message_delete(message):
            embed = discord.Embed(description="**Message from **"+message.author.mention+"** deleted in**"+message.channel.mention+"\n"+message.content,colour = discord.Color.blue())
            embed.set_author(name ='Message Deleted', icon_url = message.author.avatar_url)
            await channel.send(embed = embed)
        @bot.event
        async def on_message_edit(before,after):
            if before.content != after.content:
                embed = discord.Embed(description="**Message from **"+ctx.author.mention+"** edited in**"+ctx.channel.mention,colour = discord.Color.red())
                embed.set_author(name ='Message Edited', icon_url = before.author.avatar_url)
                embed.add_field(name="Before:",value=before.content,inline=False)
                embed.add_field(name="After:",value=after.content,inline=False)
                await channel.send(embed = embed)
    elif status.lower()=='disable':
        await ctx.send("Disabling message log.")
    else:
        return await ctx.send("Choose to enable or disable the message log.")

@bot.command()
async def modlog(ctx,status="",channel=""):
    try:
        channel=channel.replace("<","")
        channel=channel.replace(">","")
        channel=channel.replace("#","")
        channel=int(channel)
        channel=bot.get_channel(channel)
    except:
        await ctx.send("Not a valid channel.")
    if status.lower()=='enable':
        await ctx.send("Starting mod log in "+channel.mention)
        global count
        count=0
        @bot.event
        async def on_member_ban(guild, user):
            global count
            count+=1
            await channel.send("**BAN** | Case "+str(count))
            await channel.send("**Target: **  "+str(user)+" ("+str(user.id)+")")
            
            
        @bot.event
        async def on_member_unban(guild, user):
            global count
            count+=1
            await channel.send("**UNBAN** | Case "+str(count))
            await channel.send("**Target: **  "+str(user)+" ("+str(user.id)+")")
            
            
    elif status.lower()=='disable':
        await ctx.send("Disabling mod log.")
    else:
        return await ctx.send("Choose to enable or disable the mod log.")

@bot.command()
async def loginlog(ctx,status="",channel=""):
    try:
        channel=channel.replace("<","")
        channel=channel.replace(">","")
        channel=channel.replace("#","")
        channel=int(channel)
        channel=bot.get_channel(channel)
    except:
        await ctx.send("Not a valid channel.")
    if status.lower()=='enable':
        await ctx.send("Starting login log in "+channel.mention)
        @bot.event
        async def on_member_join(member):
            await channel.send(member.mention+" has joined "+ctx.guild.name+"!")
            
        @bot.event
        async def on_member_remove(member):
            await channel.send(member.name+" has left "+ctx.guild.name+"!")
            
            
    elif status.lower()=='disable':
        await ctx.send("Disabling login log.")
    else:
        return await ctx.send("Choose to enable or disable the login log.")
@bot.event
async def on_message(message):
    if message.author.bot: return
    id = str(message.author.id)
    if id not in amounts:
        amounts[id] = 100
        await message.channel.send("You are now a registered slave owner and have been given 100 slaves")
        _save()
    else:
        amounts[id]+=random.randint(0,5)
        _save()
    await bot.process_commands(message)
@bot.command()
async def balance(ctx,member:discord.User=None):
    try:
        id = str(member.id)
    except:
        id=str(ctx.message.author.id)
    if id ==str(ctx.message.author.id):
        await ctx.send("You have "+str(amounts[id])+" slaves.")
    else:
        await ctx.send(member.mention+" has "+str(amounts[id])+" slaves.")
@bot.command()
async def transfer(ctx,member: discord.Member,amount=0):
    primary_id = str(ctx.message.author.id)
    other_id = str(member.id)
    if other_id not in amounts:
        await ctx.send(member.mention+" is not a fan of slavery and does not own slaves")
    elif amounts[primary_id] < amount:
        await ctx.send("You need "+str(amount-amounts[primary_id])+" more slaves to do that")
    else:
        amounts[primary_id] -= amount
        amounts[other_id] += amount
        await ctx.send("You have successfully given "+member.mention+" "+str(amount)+" slaves!")
    _save()

def _save():
    with open('amounts.json', 'w+') as f:
        json.dump(amounts, f)

@bot.command()
async def roulette(ctx,color,bet=10):
    id=str(ctx.message.author.id)
    if amounts[id] < bet:
        await ctx.send("You need "+str(bet-amounts[id])+" more slaves to do that!")
    elif bet<10:
       await ctx.send("The minimum bet is 10 slaves!")
    else:
        amounts[id]-=bet
        msg=["🟩","🟥","⬛","🟥","⬛","🟥","⬛","🟥","⬛","🟥","⬛","🟥","⬛","🟥","⬛","🟥","⬛","🟥","⬛","🟥","⬛","🟥","⬛","🟥","⬛","🟥","⬛","🟥","⬛","🟥","⬛","🟥","⬛","🟥","⬛","🟥","⬛"]
        b=random.randint(0,36)
        message=await ctx.send("━━━━━━▼━━━━━━\n "+msg[b-8]+msg[b-7]+msg[b-6]+msg[b-5]+msg[b-4]+msg[b-3]+msg[b-2]+msg[b-1]+msg[b]+"\n━━━━━━▲━━━━━━")
        while b<len(msg):
            await message.edit(content="━━━━━━▼━━━━━━\n "+msg[b-8]+msg[b-7]+msg[b-6]+msg[b-5]+msg[b-4]+msg[b-3]+msg[b-2]+msg[b-1]+msg[b]+"\n━━━━━━▲━━━━━━")
            await asyncio.sleep(0.7)
            b+=1
        b=0
        while b<random.randint(0,36):
            await message.edit(content="━━━━━━▼━━━━━━\n "+msg[b-8]+msg[b-7]+msg[b-6]+msg[b-5]+msg[b-4]+msg[b-3]+msg[b-2]+msg[b-1]+msg[b]+"\n━━━━━━▲━━━━━━")
            await asyncio.sleep(0.7)
            b+=1
        winner=msg[b-5]
        await asyncio.sleep(1)
        if color.lower()=="black" and winner=="⬛":
            amounts[id]+=2*bet
            await ctx.send("Congrats "+ctx.author.mention+", you won: "+str(2*bet))
        elif color.lower()=="red" and winner=="🟥":
            amounts[id]+=2*bet
            await ctx.send("Congrats "+ctx.author.mention+", you won: "+str(2*bet))
        elif color.lower()=="green" and winner=="🟩":
            amounts[id]+=2*bet
            await ctx.send("Congrats "+ctx.author.mention+", you hit green and won: "+str(14*bet))
        else:
            await ctx.send("Oof "+ctx.author.mention+", you lost "+str(bet)+" slaves. Good luck next time!")
        _save()

bot.run('TOKEN')
