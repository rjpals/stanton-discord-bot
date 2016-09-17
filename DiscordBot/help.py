import discord
import asyncio


async def help(client, message):
    user = message.author
    await client.send_message(user, 'fuk u read a book')