import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'logged in as {client.user}')

@client.event
async def evalute(message):
    await message.channel.send('type in the first number')
    if message.content.startswith('$'):
        number1=message.content
        await message.channel.send('type in the second number')
        if message.content.startswith('$'):
            number2=message.content
    message.channel.send("the first number is " + number1 + "and the second is "+ number2)
    



@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$eval'):
        await evalute(message)




