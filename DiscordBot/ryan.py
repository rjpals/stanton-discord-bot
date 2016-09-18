import discord
import asyncio
from random import randrange
from reddittest import random_hot_post
from memes import meme_request

ASCIIKITTEN = """                      __     __,
                      \,`~"~` /
      .-=-.           /    . .\
     / .-. \          {  =    Y}=
    (_/   \ \          \      /
           \ \        _/`'`'`b
            \ `.__.-'`        \-._
             |            '.__ `'-;_
             |            _.' `'-.__)
              \    ;_..-`'/     //  \
              |   /  /   |     //    |
              \  \ \__)   \   //    /
               \__)        './/   .'
                             `'-'`
"""

   

    async def ryan(client, message):
        if message.content.startswith('!memeasdfasdf'):
            await client.send_message(message.channel, "http://i.imgur.com/2UsbZdM.jpg")

        elif message.content.startswith('!kitten'):
            if message.content.startswith('!kittenrussianroulette'):
                barrel = randrange(1, 6)
                print(barrel)
                if (barrel < 2):
                    await client.send_message(message.channel, ASCIIKITTEN)
                    await client.send_message(message.channel, "Oh noes!! The kiten is kill!!1!1!")

                else:
                    await client.send_message(message.channel, random_kitten())
                    await client.send_message(message.channel, "The kiten lives 2day!!")
            else:
                await client.send_message(message.channel, random_kitten())

        elif message.content.startswith('!eyebleach'):
            for i in range(1,5):
                await client.send_message(message.channel, random_kitten())

        elif message.content.startswith('!clear'):
            msg = ''
            for i in range(1, 25):
                msg += ".\n"
            for i in range(1, 3):
                await client.send_message(message.channel, msg)

        elif message.content.startswith('!shit'):
            await client.send_message(message.channel, random_hot_post('shitpost'))

        elif message.content.startswith('!meme'):
            things = message.content.split(":")
            if len(things) < 2:
                await client.send_message(message.channel, random_hot_post('adviceanimals'))

            else:
                meme = meme_request(things[1], things[2])
                await client.send_message(message.channel, meme)

