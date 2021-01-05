import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('help cog loaded!')

    @commands.command()
    async def help(self,ctx):
        embed = discord.Embed(title ='help',description = 'this shows commands available',color = discord.Color.dark_red())
        embed.add_field(name = 'join',value = 'makes the bot join voice channel',inline = True)
        embed.add_field(name = 'play',value = 'starts playing music',inline = True)
        embed.add_field(name = 'queue',value = 'queues set of songs to play next',inline = True)
        embed.add_field(name = 'skip',value='skips to the next song from queue',inline = True)
        embed.add_field(name = 'pause',value = 'pauses the song',inline = True)
        embed.add_field(name = 'resume',value='resumes the song',inline = True)
        embed.add_field(name = 'stop',value ='stops the song',inline = True)
        embed.add_field(name = 'leave',value = 'leaves the voice channel',inline = True)
        embed.add_field(name = 'ping',value = 'shows the latency of the bot',inline = True)
        embed.add_field(name = 'volume',value = 'adjust the volume',inline = True)
        embed.add_field(name = 'whois',value = 'gives the avatar and id of the mentioned user',inline = True)
        embed.add_field(name = 'clear',value = 'clears certain amount of texts in a channel',inline=True)
        await ctx.send(embed = embed)


def setup(bot):
    bot.add_cog(Help(bot))