import discord
import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()

client = discord.Client(intents=intents)


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)


async def arp(message):
    command = os.popen('sudo arp-scan --interface=wlan0 --localnet -x')
    await message.channel.send(command.read())
    print(command.close())


def notify():
    json_data = json.loads(response.text)
    r = requests.post('https://maker.ifttt.com/trigger/new_kid_in_town/with/key/nL24KQ-9jMFlEyz9XLbgEPfJCeuYhBKa1YhmdOhr1LN', json={
        "value1": "fritz",
        "value2": "jetzt"
    })
    print(f"Status Code: {r.status_code}, Response: {r.json()}")


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

    guild_count = 0

    for guild in client.guilds:

        print(f"- {guild.id} (name: {guild.name}) ")

        guild_count = guild_count + 1

        text_channel_list = []
        for channel in guild.text_channels:
            text_channel_list.append(channel)
            if channel.name == "fuehrerhq":
                await channel.send(f"fu_bot is back!")

    print("FUBOT is in " + str(guild_count) + " guilds.")


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content == "hello":
        await message.channel.send("hey dirtbag")

    if message.content.startswith('$hello'):
        await message.channel.send('Fuck you ' + message.author.name + '!')

    if message.content.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    if message.content.startswith('$arp'):
        await arp(message)

@client.event
async def on_member_update(before, after):
    print(f"{after.name} has gone {after.status}.")
    if str(after.status) == 'online':
        await client.get_channel(id='fuehrerhq').send('Hello')

client.run(TOKEN)
