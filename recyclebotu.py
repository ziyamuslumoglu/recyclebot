
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def mem(ctx):
    with open('images/mem2.jpg','rb') as f:
        picture = discord.File(f)   
    await ctx.send(file=picture)

@bot.command()
async def merhaba(ctx):
       
    await ctx.send(f"Merhaba ben {bot.user}. Ben insanları geri dönüşüm hakkında bilgilendirim. ben \"mem\" ve \"merhaba\" komutlarına sahibim. bu komutları \"$\" işareti ile çağırabilirsin. haydi o zaman atmayalım dönüştürelim :)")

@bot.command()
async def recycleimg(ctx):
     with open('images/recycle.jpg','rb') as f:
         picture = discord.File(f)
     text="Recycle"  
     await ctx.send(file=picture,content=text)

bot.run("MTE2MDE0ODM4MDgyNDEwOTA3Ng.GoXJwF.qD_scjT4uKLWFtZ_B35VpMnWpJ7HprhDbM_NN0")
