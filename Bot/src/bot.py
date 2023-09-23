import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'logged in as {client.user}')


async def evalute(message):
    userID=message.author
    msg_channel= message.channel
    await msg_channel.send('type in the first number, ' + str(userID))

    while True:
        msg = await client.wait_for('message')
        if  msg.author == userID:
            break
    number1= msg.content

    await msg_channel.send('type in the second number, ' + str(userID))

    while True:
        msg = await client.wait_for('message')
        if  msg.author == userID:
            break
    number2=msg.content

    await msg_channel.send(int(number1) + int(number2))     #should make sure that the numbers are ints but can't be bothered rn
    await msg_channel.send("the first number is " + number1 + " and the second is "+ number2)
    await msg_channel.send(msg_channel)



@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$eval'):
        await evalute(message)




