from nextcord.ext import commands
import nextcord


class OnReady(commands.Cog):
    def __init__(self, client):
        super().__init__()
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(activity=nextcord.Game(name='Co za pieron z tego bota'))
        print('that Pieron has connected  ---> {0.user}'.format(self.client))


def setup(client):
    client.add_cog(OnReady(client))
