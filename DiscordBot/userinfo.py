import discord
import asyncio

async def userinfo(client, message):
    global voteStrings
    text = ""
    if message.content.startswith('~whois'):
        if len(message.mentions) == 0:
            text = "You must @mention a user."
        elif len(message.mentions) > 1:
            text = "You may only @mention one user."
        else:
            user = message.mentions[0]
            text += user.mention + "\n"
            text += "avatar url: " + user.avatar_url + "\n"
            text += "username: " + user.name + "\n"
            text += "joined: " + str(user.joined_at) + "\n"
        await client.send_message(message.channel, text)

    elif message.content.startswith('~avatar'):
        if len(message.mentions) == 0:
            text = "You must @mention a user."
        elif len(message.mentions) > 1:
            text = "You may only @mention one user."
        else:
            text += message.mentions[0].mention + " " + message.mentions[0].avatar_url
        await client.send_message(message.channel, text)
