from nextcord.ext import commands
import random
import nextcord


class ForFun(commands.Cog):
    def __init__(self, client):
        super().__init__()
        self.client = client

    @commands.command(aliases=["8ball"])
    async def eightball(self, ctx):
        responses = [
            "Oczywiście, że tak",
            "Na 100%!",
            "Zdecydowanie tak",
            "Na pewno!!!",
            "Tak",
            "Raczej tak",

            "Oczywiście, że nie",
            "Na 0%...",
            "Zdecydowanie nie",
            "Na pewno nie xD",
            "Nie",
            "Raczej nie"
        ]
        await self.reply(embed=nextcord.Embed(
            description=f":8ball: {random.choice(responses)}"
        ))

    @commands.command()
    async def iq(self, ctx, member: nextcord.Member = None):
        if member is None:
            member = ctx.author
        await ctx.reply(f"{member.mention} ma {random.randint(40, 300)} iq")


def setup(client):
    client.add_cog(ForFun(client))
