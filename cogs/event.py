# event.py
# Recycled 05/16/20
import discord
from discord.ext import commands


class Event(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        """Function check the operation of the bot."""
        print('{0} is online.'.format(self.client.user))

    @commands.Cog.listener()
    async def on_member_join(self, member):
        """Sending a personal message about the bot and issuing a role in the chat."""
        await member.send(
            f'Welcome {member}! White !com to find out my command.')
        role = discord.utils.get(member.guild.roles, id=691321624108073021)
        await member.add_roles(role)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        """Output information about user exit."""
        print(f'{member} leave from server.')

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        """Notifies about the issuance and withdrawal of a role from a user"""
        if len(before.roles) < len(after.roles):
            for i in after.roles:
                if i not in before.roles:
                    await after.send(f'You have been given a role {i}!')
        elif len(before.roles) > len(after.roles):
            for i in before.roles:
                if i not in after.roles:
                    await after.send(f'You were deprived of the role {i}')


def setup(client):
    client.add_cog(Event(client))
