import discord
from discord.abc import T
from discord.embeds import E
from discord.ext import commands
# from discord.forms import Form
import datetime
import os
from asyncio import sleep
from discord_components.client import DiscordComponents
# from discord_components import DiscordComponents,Button, ButtonStyle, InteractionType
from dotenv import load_dotenv
import requests
import asyncio

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
client=commands.Bot(command_prefix= 'heh ')

@client.event
async def on_ready():
    DiscordComponents(client)
    time = datetime.datetime.now()
    print("Riana is ready!")
    channel = client.get_channel(channelchannel)
    embed = discord.Embed(
        title = "rianaa is Ready!",
        description = f"Online at {time}",
    )
    await channel.send(embed = embed)

@client.command()
async def ping(ctx):
    await ctx.send('pong')

@client.command()
async def clear(ctx , amount=100000):
  await ctx.channel.purge(limit=amount + 1)

#========== kode pemanasan ===============
@client.command()
async def comfort(ctx, user: discord.Member = None):
    if user == None:
        await ctx.message.reply('Who should I comfort?') #idk what is this
    elif user != None and user == str('me'):
        user == ctx.author
    await ctx.send('Hey')
    await sleep(5)
    await ctx.send("If you have a bad day")
    await sleep(1)
    await ctx.send('plz watch this')
    embed = discord.Embed(
        title = 'hi!',
        description = f'Please have a greaet day! {user.mention} ;)'
    )
    embed.set_image(url='https://cdn.discordapp.com/attachments/891375274212618262/891375336586113094/2Q.png')
    await ctx.send(embed=embed)

#================= kode ala ala ================
@client.command()
async def embed(ctx):
    try:
        t = await ctx.send('Please include your title text :')
        msg = await client.wait_for(
            "message",
            timeout=10,
            check=lambda message: message.author == ctx.author and message.channel == ctx.channel
        )
        if msg:
            await t.delete()
            title = msg
        d = await ctx.send('Please include your description text :')
        msg = await client.wait_for(
            "message",
            timeout=10,
            check=lambda message: message.author == ctx.author and message.channel == ctx.channel
        )
        if msg:
            await d.delete()
            description = msg
    except asyncio.TimeoutError:
        await sent.delete()
        await ctx.send('<a:loading:892056760985198672> Cancelling.....', delete_after=6)
        await sleep(2)
        await ctx.send(">>> *Cancelling due to timeout.*", delete_after=4)
    # Embed = discord.Embed(
    #     title=title,
    #     description=description
    # )
    # await ctx.send(embed=Embed)
    await ctx.send(f'{title}\n{description}')

@client.command()
async def omong(ctx, *,message=None):
    if message == None:
        await ctx.reply("Aku suruh omong apa?")
        return
    await ctx.message.delete()
    await ctx.send(str(message))

@client.command()
async def tes(ctx):
    await ctx.send('<a:loading:892056760985198672>')

### =================== component code ==========================



### =================== User input code =========================
### error 
@client.command()
async def echo(ctx):
    await ctx.message.delete()
    embed = discord.Embed(
        title="kamu mau omong apa?",
        description="kamu omong aku ulang. timeoout 1 menit"
    )
    sent = await ctx.send(embed=embed)

    try:
        msg = await client.wait_for(
            "message",
            timeout=3,
            check=lambda message: message.author == ctx.author and message.channel == ctx.channel
        )
        if msg:
            await sent.delete()
            await msg.delete()
            await ctx.send(msg.content)
    except asyncio.TimeoutError:
        await sent.delete()
        await ctx.send('<a:loading:892056760985198672> Cancelling.....', delete_after=6)
        await sleep(2)
        await ctx.send(">>> *Cancelling due to timeout.*", delete_after=4)

## this code is by myself

# @client.command()
# async def test(ctx):
#     await ctx.send(
#         "hellooooooooooooooooooooooooooo please click the button",
#         components = [clientButton(label="Click here", custom_id = "button1")
#         ],
#     )


client.run(TOKEN)
