import discord
import asyncio
from trash import trash
from help import help, prune
from voiceClient import summon, playTest

Token = input("Enter your token: ")
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    if message.content.startswith('~test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=1000):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, message.author.name + ', you have {} messages.'.format(counter))

    elif message.content.startswith('~praise'):
        await client.send_message(message.channel, 'https://media.giphy.com/media/fr42tarocsK6Q/giphy.gif')

    elif message.content.startswith('~help'):
        await help(client, message)

    elif message.content.startswith('~permission'):
        if client.user.permissions_in(message.channel).read_messages:
            await client.send_message(message.channel, "I have permission")
        else:
            await client.send_message(message.channel, "I do not have permission")

    elif message.content.startswith('~summon'):
        await summon(client, message)

    elif message.content.startswith('~prune'):
        await prune(client, message)

    elif message.content.startswith('~play'):
        await playTest(client, message)

    else:
        await trash(client, message)


@client.event
async def on_member_join(member):
    await client.send_message(member.server, member.mention + ' has joined the server.')


@client.event
async def on_member_remove(member):
    await client.send_message(member.server, member.mention + ' has been forcefully removed from the channel.')

@client.event
async def on_voice_state_update(before, after):
    if client.is_voice_connected(after.server):
        vClient = client.voice_client_in(before.server)
        if len(vClient.channel.voice_members) == 1:
            await client.voice_client_in(before.server).disconnect()



client.run(Token)