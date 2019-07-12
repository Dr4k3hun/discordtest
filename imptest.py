import discord

from discord import Member
from discord import guild
from discord import abc
from discord import channel

messages = 0
joined = 0

TOKEN = "NTc5MzQxNTM2ODQ4OTA0MjIw.XRiXpg.xGfzQ39oePhrGG-prEUm-SLIBPU"
client = discord.Client()


# id = 594845376033587212


@client.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name='Guest')
    await Member.add_roles(member, role)


async def update_stats():
    await client.wait_until_ready()
    global messages, joined
    messages += 0.5


@client.event

async def on_message(message):
    ID = client.get_guild(594845376033587212)
    print(message.content)
    global messages
    messages += 0.5

    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content == "!help":
        embed = discord.Embed(title="Útmutató a bothoz", description="Néhány hasznos parancs")
        embed.add_field(name="!hello", value="Üdvözli a felhasználót")
        embed.add_field(name="!felhasználók", value="Megmondja, hogy hány ember van a szerveren")
        embed.add_field(name="!üzenetek",
                        value="Megmondja, hogy hány üzenet lett elküldve a szerveren, mióta online van")
        await message.channel.send(content=None, embed=embed)

    if message.content == '!kurvaanyád' != -1:
        msg = 'Kedves {0.author.mention}! Az édesanyám nem kurva, csak jól keres.'.format(message)
        await message.channel.send(msg)


    if message.content == '!hello' != -1:

        msg = 'Hello {0.author.mention}'.format(message)
        await message.channel.send(msg)
    elif message.content == "!felhasználók":
        await message.channel.send(f"""Ennyi ember van a szerveren: {ID.member_count}.""")
    elif message.content == "!üzenetek":
        await message.channel.send(f"""Mióta online vagyok {int(messages)} üzenet lett elküldve a szerveren.""")


client.loop.create_task(update_stats())


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(TOKEN)
