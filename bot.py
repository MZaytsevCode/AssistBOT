# bot.py
# Recycled 04/26/20
import os
import random

import discord
from discord.ext import commands

# Leave this prefix
client = commands.Bot(command_prefix='!')

# Constant language
LANG = 'EN'


@client.event
async def on_ready():
    """Function check the operation of the bot."""
    print('{0} подключен.'.format(client.user))


@client.event
async def on_member_join(member):
    """Sending a personal message about the bot and issuing a role in the chat."""
    await member.send(
        f'Welcome {member}! White !com to find out my command.'
        f'(Добро пожаловать {member}! Напиши !com чтобы узнать мои команды.)')
    role = discord.utils.get(member.guild.roles, id=691321624108073021)
    await member.add_roles(role)


@client.event
async def on_member_remove(member):
    """Output information about user exit."""
    print(f'{member} вышел c сервера.')


@client.event
async def on_member_update(before, after):
    if before.roles != after.roles:
        if len(before.roles) < len(after.roles):
            if get_lang() == 'RU':
                await after.send(f'Вам выдана новая роль!')
            elif get_lang() == 'EN':
                await after.send(f'You were given a new role!')
        if len(before.roles) > len(after.roles):
            if get_lang() == 'RU':
                await after.send(f'Вас лишили роли(')
            elif get_lang() == 'EN':
                await after.send(f'You were deprived of the role(')
    else:
        if before.status != after.status:
            await after.send(f'Статус был изменен на {after.status}.')


@client.command()
async def ping(ctx):
    """Return you latency"""
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    """8-ball game"""
    responses = ["It is certain (Бесспорно)",
                 "It is decidedly so (Предрешено)",
                 "Without a doubt (Никаких сомнений)",
                 "Yes — definitely (Определённо да)",
                 "You may rely on it (Можешь быть уверен в этом)",
                 "As I see it, yes (Мне кажется — «да»)",
                 "Most likely (Вероятнее всего)",
                 "Outlook good (Хорошие перспективы)",
                 "Signs point to yes (Знаки говорят — «да»)",
                 "Yes (Да)",
                 "Reply hazy, try again (Пока не ясно, попробуй снова)",
                 "Ask again later (Спроси позже)",
                 "Better not tell you now (Лучше не рассказывать)",
                 "Cannot predict now (Сейчас нельзя предсказать)",
                 "Concentrate and ask again (Сконцентрируйся и спроси опять)",
                 "Don’t count on it (Даже не думай)",
                 "My reply is no (Мой ответ — «нет»)",
                 "My sources say no (По моим данным — «нет»)",
                 "Outlook not so good (Перспективы не очень хорошие)",
                 "Very doubtful (Весьма сомнительно)"]
    if get_lang() == "EN":
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')
    elif get_lang() == "RU":
        await ctx.send(f'Вопрос: {question}\nОтвет: {random.choice(responses)}')


@client.command()
async def clear(ctx, amount=6):
    """Clear chat"""
    await ctx.channel.purge(limit=amount)


@client.command()
async def spam(ctx, mes="Why?", time=1):
    """Spam command"""
    for _ in range(time):
        await ctx.send(str(mes))


@client.command()
async def users(ctx):
    """Return bot users"""
    user = ""
    for i in range(1, len(client.users)):
        user += str(client.users[i]) + "\n\t"
    if get_lang() == "EN":
        await ctx.send(f'Bot users:\n\t' + str(user))
    elif get_lang() == "RU":
        await ctx.send(f'Пользователи бота:\n\t' + str(user))


@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    """Ban user."""
    await member.ban(reason=reason)
    if get_lang() == "EN":
        await ctx.send(f'Banned {member.mention}')
    elif get_lang() == "RU":
        await ctx.send(f'Заблокирован {member.mention}')


@client.command()
async def unban(ctx, *, member):
    """Unban user."""
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            if get_lang() == "EN":
                await ctx.send(f'Unbanned {member.mention}')
            elif get_lang() == "RU":
                await ctx.send(f'Разблокирован {member.mention}')


@client.command(aliases=["lang"])
async def language(ctx, lang):
    """Set language"""
    if lang in ['RU', "EN"]:
        set_lang(lang)
        if get_lang() == "RU":
            await ctx.send("Русский язык установлен.")
        elif get_lang() == "EN":
            await ctx.send("English set.")
        else:
            await ctx.send("Set error.")
    else:
        await ctx.send("Set error.")


def set_lang(lang):
    """Set constant LANG"""
    global LANG
    LANG = lang


def get_lang():
    """Return constant LANG"""
    global LANG
    return LANG


@client.command()
async def wb(ctx, *, question):
    """Game White or Black"""
    rc = get_random_color()
    if question == rc:
        if get_lang() == "EN":
            await ctx.send("Yes, it's " + question)
        elif get_lang() == "RU":
            await ctx.send("Да, это " + question)
    else:
        if get_lang() == "EN":
            await ctx.send("No, it's " + question)
        elif get_lang() == "RU":
            await ctx.send("Нет, это " + question)


def get_random_color():
    """Random generate color"""
    colors = ['white', 'black']
    return random.choice(colors)


@client.command(aliases=['wbg'])
async def WhatByGame(ctx):
    """Function for choice game"""
    responses = ["Fortnite", "CS:GO", "Valorant", "GTA:SA",
                 "PUBG", "SAR", "Rust", "RDR2", "Assassin's creed",
                 "Call of duty:Warzone"]
    if get_lang() == "EN":
        await ctx.send(f'Play to {random.choice(responses)}')
    elif get_lang() == "RU":
        await ctx.send(f'Поиграй в {random.choice(responses)}')


@client.command(aliases=['rg'])
async def RandomGame(ctx, *, games):
    """Random choice game"""
    if get_lang() == "EN":
        await ctx.send(f'Play to {random.choice(games.split())}')
    elif get_lang() == "RU":
        await ctx.send(f'Поиграй {random.choice(games.split())}')


@client.command()
async def com(ctx):
    """Bot commands"""
    if get_lang() == "EN":
        await ctx.send(f'Bot commands:'
                       f'\n\n\t * !ping - You ping,'
                       f'\n\n\t * !8ball question - Ball of predictions,'
                       f'\n\n\t * !clear Qty - Clear chat,'
                       f'\n\n\t * !ban @nickname - Ban user,'
                       f'\n\n\t * !unban nickname#user tag - Unban user'
                       f'\n\n\t * !wb white/black - Game white or black,'
                       f'\n\n\t * !com - Bot command,'
                       f'\n\n\t * !users - Bot users,'
                       f'\n\n\t * !spam message qty - spam function,'
                       f'\n\n\t * !wbg - Advice on what to play'
                       f'\n\n\t * !rg game1 game2 game3 ... gameN - Randomly chooses a game'
                       f'\n\n\t * !lang lang(EN/RU) - Set language'
                       )
    elif get_lang() == "RU":
        await ctx.send(f'Команды бота:'
                       f'\n\n\t * !ping - Ваш пинг,'
                       f'\n\n\t * !8ball вопрос - Шар предсказаний,'
                       f'\n\n\t * !clear Кол-во - Очистка чата,'
                       f'\n\n\t * !ban @ник - Блокировка пользователя,'
                       f'\n\n\t * !unban ник#персональный тег - Разблокировать пользователя'
                       f'\n\n\t * !wb цвет(white/black) - Игра белое/черное,'
                       f'\n\n\t * !com - Команды Бота,'
                       f'\n\n\t * !users - Пользователи бота,'
                       f'\n\n\t * !spam сообщение кол-во - Спам функция,'
                       f'\n\n\t * !wbg - Совет во что поиграть'
                       f'\n\n\t * !rg game1 game2 game3 ... gameN - Рандомно выбирает игру'
                       f'\n\n\t * !lang язык(EN/RU) - Установаить язык'
                       )


# Token in *******.
token = os.environ.get('BOT_TOKEN')
client.run(str(token))
