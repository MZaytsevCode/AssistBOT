import discord
from discord.ext import commands

from cogs.language import get_lang


class Events(commands.Cog):

    def __init__(self, client):
        """Initialisation client"""
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        """Function check the operation of the bot."""
        print('{0} is online.'.format(self.client.user))
        await self.client.change_presence(status=discord.Status.dnd)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        """Sending a personal message about the bot and issuing a role in the chat."""
        if get_lang() == "EN":
            await member.send(
                f'Welcome {member}! White $help to find out my command.')
        else:
            await member.send(
                f'Добро пожаловать, {member}! Напиши !help чтобы узнать мои команды.')
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
                    if get_lang() == "EN":
                        await after.send(f'You have been given a role {i}!')
                    else:
                        await after.send(f'Вам выдали роль {i}!')
        elif len(before.roles) > len(after.roles):
            for i in before.roles:
                if i not in after.roles:
                    if get_lang() == "EN":
                        await after.send(f'You were deprived of the role {i}')
                    else:
                        await after.send(f'Вас лишили роли {i}')


def setup(client):
    """Setup function"""
    client.add_cog(Events(client))
