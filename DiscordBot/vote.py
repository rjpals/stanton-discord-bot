import discord
import asyncio
import urllib
import json
import urllib.request

inVote = False
voteStrings=[]
votes=[]
async def trash(client, message):
    
    if message.content.startswith('~v'):
        if message.content.startswith('~vote'):
            inVote = True
            voteStrings = message.content[5:].split(';')
            print(voteStrings)

        tmp = await client.send_message(message.channel, "")
        
    elif message.content.startswith('~kappa'):
        await client.send_message(message.channer, "")
