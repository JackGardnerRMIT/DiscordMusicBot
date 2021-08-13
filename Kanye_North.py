#ODU1NjkwNzQ3NzY3MTYwODMz.YM2KHA.UUm9dep2hjmBbQsGk17zZ9HJO_c

#https://discord.com/api/oauth2/authorize?client_id=855708495818129428&permissions=8&scope=bot

#ODU1NzA4NDk1ODE4MTI5NDI4.YM2aow.3ipoutbwiBeQcrQmVgaWfpXShPA

#https://replit.com/@JackGardnerRMIT/KanyeNorth#main.py

#Main.py

import discord
from discord.ext import commands
import music

cogs = [music]

client = commands.Bot(command_prefix='?', intents = discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)

client.run("ODU1NzA4NDk1ODE4MTI5NDI4.YM2aow.3ipoutbwiBeQcrQmVgaWfpXShPA")

#Music.py

import discord
from discord.ext import commands
import youtube_dl

class music(commands.Cog):
    def __init__(self, client):
        self.clent = client

    @commands.command()
    async def join(self,ctx):
        if ctx.author.voice is None:
            await ctx.send("You're not in a voice channel!")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
          await voice_channel.connect()
        else:
          await ctx.voice_client.move_to(voice_channel)

    @commands.command()
    async def disconnect(self,ctx):          
      await ctx.voice_client.disconnect()

    @commands.command()
    async def play(self,ctx,url):
      ctx.voice_client.stop()
      FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
      YDL_OPTIONS = {'format':"bestaudio"}
      vc = ctx.voice_client

      with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
        info = ydl.extract_info(url, download=False)
        url2 = info['formats'][0]['url']
        source = await discord.FFmpegOpusAudio.from_probe(url2,
        **FFMPEG_OPTIONS)
        vc.play(source)

    @commands.command()
    async def pause(self,ctx):          
      await ctx.voice_client.pause()
      await ctx.send("Paused")

    @commands.command()
    async def resume(self,ctx):          
      await ctx.voice_client.resume()
      await ctx.send("Resume")

def setup(client):
    client.add_cog(music(client))