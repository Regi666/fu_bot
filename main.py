import discord
import os
import requests
import json

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
        print(f"- {guild.id} (name: {guild.name})")

        # INCREMENTS THE GUILD COUNTER.
        guild_count = guild_count + 1

    # PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
    print("FUBOT is in " + str(guild_count) + " guilds.")


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


client.run(os.getenv('TOKEN'))
