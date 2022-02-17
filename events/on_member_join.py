from nextcord.ext import commands
import nextcord


class OnMemberJoin(commands.Cog):
    def __init__(self, client):
        super().__init__()
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await member.add_roles(nextcord.utils.get(member.guild.roles, name="osadnik"))


def setup(client):
    client.add_cog(OnMemberJoin(client))
