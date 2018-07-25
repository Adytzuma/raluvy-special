import discord
from discord.ext import commands
import asyncio
import logging
import math
import random
import traceback
import os
from discord import opus
from asyncio import sleep

bot = commands.Bot(command_prefix='d!')
logging.basicConfig(level='INFO')
bot.remove_command('help')
bot.load_extension('admin')
colors = [discord.Colour.purple(), discord.Colour.blue(), discord.Colour.red(), discord.Colour.green(), discord.Colour.orange()]
admin1 = [404708655578218511]
admin2 = [390540063609454593]
gid = [464783042310045707]



@bot.listen()
async def on_message(message):
    if message.content.lower() == '<@390540063609454593>' and message.author != bot.user:
        em = discord.Embed(color=random.choice(colors))
        em.add_field(name=message.guild.owner.name + ' is away', value='Stop pinging me')
        await message.channel.send(embed=em)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(name='8ball')
async def l8ball(ctx, question=None):
    if question is None:
        return await ctx.send('Hey, te rog foloseste `d!8ball <intrebare>`')
    if question is not None:
        await ctx.send(random.choice(['● It is certain.', '● It is decidedly so.', '● Without a doubt.', '● Yes - definitely.', '● You may rely on it', '● As I see it, yes.', '● Most likely.', '● Outlook good.', '● Yes.', '● Signs point to yes.', '● Reply hazy, try again', '● Ask again later.', '● Better not tell you now.', '● Cannot predict now.', '● Concentrate and ask again.', '● Don`t count on it.', '● My reply is no.', '● My sources say no', '● Outlook not so good.', '● Very doubtful.' ]))

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command()
async def kill(ctx, member: discord.Member=None):
    if member is None:
        await ctx.send('Ai murit, acum da-i mention alt cuiva!')
    if member is ctx.me:
        return await ctx.send('Nah-nah, eu am protectie ;)')
    if member is ctx.author:
        return await ctx.send('Nu te poti omori singur')
    if member is not None:
        await ctx.send(random.choice([f'{ctx.author.mention} a vrut sa-l omoare pe {member.mention} doar ca sa impiedicat si s-a lovit cu capul de o piatra', f'{member.mention} a dat prea mult rage la Clash Royale pana a lesinat si a murit', f'{member.mention} a fost impins de {ctx.author.mention} de la etajul 5 si a murit', f'{member.mention} Pregatea masa doar ca a adormit si a luat foc', f'{member.mention} a fost impuscat :gun: de {ctx.author.mention}', f'Dupa o incercare grea de al omori pe {member.mention} , {ctx.author.mention} a fost arestat']))

    
@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases =['BAN', 'Ban'])
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member=None):
    """da ban la prosti"""
    if member is ctx.author:
        return await ctx.send('Nu iti poti da ban singur!')
    if member is ctx.message.guild.owner:
        await ctx.send('nu pot sa-i dau ban la owner')
    if member is ctx.me:
        await ctx.send(':x: | Nu pot sa-mi dau ban singur!')
    if member is None:
        await ctx.send(':bust_in_silhouette: | Te rog, foloseste `d!ban @<membru>`')
    if member is not None and member != ctx.author:
        await member.ban()
        await ctx.send(f':white_check_mark: | {member} a luat ban!')
    
@bot.listen()
async def on_ready():
    print(f'Logging in as {bot.user.name}')
    await bot.change_presence(activity=discord.Game(name="cu Raluca | d!help"))

@commands.cooldown(1, 60, commands.BucketType.user)
@bot.command()
async def report(ctx, *, problema=None):
    if problema is None:
        return await ctx.send('Care este problema ta? (Foloseste `d!report <problema`)')
    if problema is not None:
        await bot.get_guild(464783042310045707).get_channel(470960523194793984).send(f'{ctx.author} a raportat: {problema}')
  
    
@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases =['Kick', 'KICK'])
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member=None):
    """da kick la prosti"""
    if member is ctx.author:
        return await ctx.send('Nu iti poti da kick singur!')
    if member is ctx.message.guild.owner:
        await ctx.send('nu pot sa-i dau kick la owner')
    if member is ctx.me:
        await ctx.send(':x: | Nu pot sa-mi dau kick singur!')
    if member is None:
        await ctx.send(':bust_in_silhouette: | Te rog, foloseste `d!kick @<membru>`')
    if member is not None and member != ctx.author:
        await member.kick()
        await ctx.send(f':white_check_mark: | {member} a luat kick!')
        
@bot.command()
async def invite(ctx):
    await ctx.send('Bot-ul e privat, nu poti sa-l inviti!')

@bot.command()
async def choose(ctx, option1, option2):
    a = [option1, option2]
    if option1 == option2:
        return await ctx.send(':x: | Nu pot alege aceleasi lucruri!')
    await ctx.send(f':thinking: | {ctx.author.mention}, aleg **' + random.choice(a) + '** !')




    

@bot.listen()
async def on_member_remove(member):
    if member.guild.id == 464783042310045707:
        em = discord.Embed(color=random.choice(colors))
        em.add_field(name=':cry: Goodbye!:', value=member.mention, inline=False)
        em.add_field(name=':tools: Info:', value='Ne-a parasit... Speram sa revii, esti mereu bine venit :sob:', inline=False)
        em.set_thumbnail(url=member.avatar_url)
        await bot.get_guild(464783042310045707).get_channel(464783042310045709).send(embed=em)
    if member.guild.id != 464783042310045707:
        return


@bot.check
async def botcheck(ctx):
    return not ctx.message.author.bot

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases= ["Avatar", "AVATAR"])
async def avatar(ctx, member: discord.Member=None):
    """Get your info"""
    if member is None:
        member = ctx.author
    em = discord.Embed(title="", color=discord.Colour.blue())
    em.set_author(name=f"{member}'s avatar")
    em.set_image(url=member.avatar_url)
    msg = await ctx.send(embed=em)


@bot.listen()
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        return await ctx.send(f':raised_back_of_hand: | Stop! Nu mai scrie asa de repede! Asteapta in ** {int(error.retry_after)} ** secunde!  ', delete_after=5)
    if isinstance(error, commands.MissingPermissions):
        return await ctx.send('Nu ai permisiunea sa executi aceasta comanda!')
    if isinstance(error, commands.NotOwner):
        return await ctx.send('Nu detii acest bot!')



@bot.command(aliases= ["Say", "SAY"])
async def say(ctx, *, message):
    """Make the BOT say what you want"""
    if ctx.author.id is admin1 or admin2:
        return await ctx.send(message)


@commands.cooldown(1, 5, commands.BucketType.user)    
@bot.command()
async def welcome(ctx):
    em = discord.Embed(color=random.choice(colors))
    em.add_field(name=':tada: Welcome:', value=ctx.author.mention, inline=False)
    em.add_field(name=':tools: Info:', value='Nu uita sa citesti <#464789280368230400>, citeste <#466924639797641216> pentru mai multe informatii. Daca aveti o problema la server-ul nostru, contacti un membru staff! ENJOY', inline=False)
    em.set_thumbnail(url=ctx.author.avatar_url)  
    await ctx.send(embed=em)

'★★★★✰'

@commands.cooldown(1, 5, commands.BucketType.user)   
@bot.command()
async def goodbye(ctx):
    em = discord.Embed(color=random.choice(colors))
    em.add_field(name=':cry: Goodbye!:', value=ctx.author.mention, inline=False)
    em.add_field(name=':tools: Info:', value='Ne-a parasit... Speram sa revii, esti mereu bine venit :sob:', inline=False)
    em.set_thumbnail(url=ctx.author.avatar_url)
    await ctx.send(embed=em)


@bot.listen()
async def on_member_join(member):
    if member.guild.id == 464783042310045707:        
        em = discord.Embed(color=random.choice(colors))
        em.add_field(name=':tada: Welcome:', value=member.mention, inline=False)
        em.add_field(name=':tools: Info:', value='Nu uita sa citesti <#464789280368230400>, citeste <#466924639797641216> pentru mai multe informatii. Daca aveti o problema la server-ul nostru, contacti un membru staff! ENJOY', inline=False)
        em.set_thumbnail(url=member.avatar_url)
        await bot.get_channel(464783042310045709).send(embed=em)
    if member.guild.id != 464783042310045707:
        return
   
        

    
    
@bot.command()
async def about(ctx):
    em = discord.Embed(color=random.choice(colors))
    em.add_field(name=':crown: Owner', value='<@390540063609454593>', inline=True)
    em.add_field(name=':family_mwgb: Servers', value=f'{len(bot.guilds)}', inline=True)
    em.add_field(name=':bust_in_silhouette: Members', value=f'{len(bot.users)}', inline=True)
    em.add_field(name=':page_facing_up: Library', value='discord.py')
    em.add_field(name=':newspaper: Latency', value=f'{ctx.bot.latency * 1500:.0f} MS')
    em.set_thumbnail(url=ctx.me.avatar_url)
    await ctx.send(embed=em)


@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases= ["Playerinfo", "PLAYERINFO", "USERINFO", "Userinfo", "userinfo"])
async def playerinfo(ctx, member: discord.Member=None):
    """Get your info"""
    if member is None:
        member = ctx.author
    em = discord.Embed(color=random.choice(colors))
    em.set_author(name="Informatii")
    em.add_field(name="Nume", value=member.name, inline=False)
    em.add_field(name="ID", value=member.id, inline=False)
    em.add_field(name="Cel mai mare rol", value=member.top_role, inline=False)
    em.add_field(name="A intrat pe", value=member.joined_at, inline=False)
    em.add_field(name=f'Roluri [{len(member.roles)}]', value=', '.join(g.name for g in member.roles))
    em.set_thumbnail(url=member.avatar_url)
    msg = await ctx.send(embed=em)
    
@bot.command(aliases= ["doggy", "dog"])
async def doge(ctx):
    fp = "doge/{}".format(random.choice(os.listdir("doge")))
    await ctx.send(file=discord.File(fp)) 

@bot.listen()
async def on_message(message):
    if bot.user.mentioned_in(message):
        await message.author.edit(nick='mention alert')



"""
@bot.listen()
async def on_member_join(member):
    if member.guild.id == 461953532019605504:      
        e = discord.Embed(color=discord.Colour.blue())
        e.add_field(name=':tada: Welcome!', value=member.mention, inline=False)
        e.add_field(name=':tools: Info:', value=f'Bine ai venit pe {member.guild.name}! Nu uita sa citesti <#461959981936148511>. Speram sa te distrezi alaturi de noi! Acum suntem {member.guild.member_count}', inline=False)
        e.set_thumbnail(url=member.avatar_url)
        await bot.get_guild(461953532019605504).get_channel(470916620332695562).send(embed=e)
    if member.guild.id != 461953532019605504:
        return

    



@bot.listen()
async def on_member_remove(member):
    if member.guild.id == 461953532019605504:      
        e = discord.Embed(color=discord.Colour.blue())
        e.add_field(name=':sob: Goodbye!', value=member.mention, inline=False)
        e.add_field(name=':tools: Info:', value=f'Speram sa te mai intorci pe la noi ... Esti mereu bine venit ! Acum Suntem {member.guild.member_count} :sob: :pensive:', inline=False)
        e.set_thumbnail(url=member.avatar_url)
        await bot.get_guild(461953532019605504).get_channel(470916620332695562).send(embed=e)
    if member.guild.id != 461953532019605504:
        return
"""
  
@bot.command()
async def lenny(ctx):
    await ctx.send('( ͡° ͜ʖ ͡°)')

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command()
async def help(ctx):
    em = discord.Embed(color=random.choice(colors))
    em.set_author(name='Comenzi!')
    em.add_field(name='★Moderation★', value='`kick, ban, purge`', inline=False)
    em.add_field(name='★Info★', value='`about, avatar, report, userinfo`', inline=False)
    em.add_field(name='★Fun★', value='`kill, 8ball, choose`', inline=False)
    em.add_field(name='★Suplimentare★', value='`welcome, goodbye`', inline=False)
    em.add_field(name='★Musica★', value='`play, stop, resume, pause, stop, playing` (coming soon)', inline=False)
    em.set_footer(text='✰Foloseste `d!` inainte de comanda✰')
    em.set_thumbnail(url=ctx.me.avatar_url)
    await ctx.send(embed=em)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases= ["clear", "prune", "delete", "PURGE", "Purge"])
@commands.has_permissions(manage_channels=True)
async def purge(ctx, number : int):
    if number>100 or num<0:
        return await ctx.send('Te rog specializeaza un numar mai mic de 101')
    await ctx.message.delete()
    await ctx.channel.purge(limit=number)
    await ctx.message.channel.send(f':white_check_mark: | Am sters {int(number)} mesaje', delete_after=5)  

























bot.run('NDcwNTY1ODAwNDk2MDcwNjU2.Djcl5w.zJPGdGJoVlMH389DGCnSoQi_tto')
