import discord
import asyncio
import re

user_toDelete = ''

async def help(client, message):
    user = message.author
    await client.send_message(user, 'fuk u read a book')

async def prune(client, message):
    input = message.content
    if len(message.mentions) == 0:
        number = list(map(int, re.findall('\d+', input)))
        await client.purge_from(message.channel, limit=number[0])
        await client.send_message(message.channel, "Pruning the last " + str(number[0]) + " messages.")

    else:
        number = list(map(int, re.findall('\d+', input)))
        for user in message.mentions:
            userDelCount = 0
            async for log in client.logs_from(message.channel, limit=number[0]):
                if user == log.author:
                    client.delete_message(log)
                    userDelCount+=1

            await client.send_message(message.channel, "Pruned " + str(userDelCount) + " messages from" + user.mention +".")


