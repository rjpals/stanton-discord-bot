import discord
import asyncio

async def moderation(client, message):
    if message.content.startswith('~kick'):
        if len(message.mentions) == 0:
            text = "You must @mention a user to kick."
        else:
            for i in range(0, len(message.mentions)):
                await client.kick(message.mentions[i])
        await client.send_message(message.channel, text)

    elif message.content.startswith('~ban'):
        if len(message.mentions) == 0:
            text = "You must @mention a user to kick."
            await client.send_message(message.channel, text)
        elif len(message.mentions) > 1:
            text = "You can only ban a single user at a time."
            await client.send_message(message.channel, text)
        else:
            await client.ban(message.mentions[0], 0)
    elif message.content.startswith('~botname'):
        if len(message.content) <= 9:
            text = "Please provide new bot username"
        else:
            try:
                await client.edit_profile(username = message.content[9:])
                text = "Bot name changed to: " + message.content[9:]
            except:
                text = "Name changes too frequent, wait a while."
            await client.send_message(message.channel, text)
    elif message.content.startswith('~botavatar'):
        if len(message.content) <= 11:
            text = "Please provide a png image path."
        else:
            f = open(message.content[11:], 'rb')
            await client.edit_profile(avatar = f.read())
            f.close()
