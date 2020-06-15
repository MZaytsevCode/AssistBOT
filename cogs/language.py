# language.py
# Recycled 06/15/20
from discord.ext import commands


def get_lang():
    """Get language"""
    with open('cogs/lang.json', 'r') as lang:
        return lang.readline()[2:-2]


def set_lang(language):
    """Set language"""
    with open('cogs/lang.json', 'w') as lang:
        return lang.write('["' + language + '"]')


class Language(commands.Cog):

    def __init__(self, client):
        """Initialisation client and LANG"""
        self.client = client
        self.LANG = get_lang()

    @commands.has_role(670599227335770143)
    @commands.command(aliases=['lang'])
    async def set_language(self, ctx, lang):
        """Set language"""
        if lang == "EN":
            await ctx.send("Language set.")
            self.LANG = set_lang(lang)
        elif lang == "RU":
            await ctx.send("Язык установлен")
            self.LANG = set_lang(lang)
        else:
            await ctx.send("Set Error.")


def setup(client):
    client.add_cog(Language(client))
