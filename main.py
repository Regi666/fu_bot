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


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

    # CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
    guild_count = 0

    # LOOPS THROUGH ALL THE GUILD / SERVERS THAT THE BOT IS ASSOCIATED WITH.
    for guild in client.guilds:
        # PRINT THE SERVER'S ID AND NAME.
        print(f"- {guild.id} (name: {guild.name}) ")

        # INCREMENTS THE GUILD COUNTER.
        guild_count = guild_count + 1

        text_channel_list = []
        for channel in guild.text_channels:
            text_channel_list.append(channel)
            if channel.name == "fuehrerhq":
                await channel.send(f"fu_bot is back!")


    # PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
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
        # SENDS BACK A MESSAGE TO THE CHANNEL.
        await message.channel.send("hey dirtbag")

    if message.content.startswith('$hello'):
        await message.channel.send('Fuck you ' + message.author.name + '!')

    if message.content.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)


client.run(TOKEN)
