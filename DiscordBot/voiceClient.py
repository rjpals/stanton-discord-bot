import discord
import asyncio


async def voiceInit():
    if not discord.opus.is_loaded():
        discord.opus.load_opus('opus')


async def summon(client, message):
    """Summons the bot to join your voice channel."""
    summoned_channel = message.author.voice_channel
    if summoned_channel is None:
        await client.send_message(message.channel, 'You are not in a voice channel.')
        return False

    if client.is_voice_connected(message.server):
        await client.voice_client_in(message.server).move_to(summoned_channel)
    else:
        await client.join_voice_channel(summoned_channel)

    return True

async def playTest(client, message):
    """Play test audio"""
    audio_channel = message.author.voice_channel
    if audio_channel is None:
        await client.send_message(message.channel, 'You are not in a voice channel.')
        return False

    elif not client.voice_client_in(message.server):
        await client.send_message(message.channel, 'I am not in a voice channel please "~summon" me')

    elif client.voice_client_in(message.server).channel == message.author.voice_channel:
        await voiceInit()
        vClient = client.voice_client_in(message.server)
        player = await vClient.create_ytdl_player('https://www.youtube.com/watch?v=fKCejWupowA')
        player.start()

    else:
        await client.send_message(message.channel, 'You are not in my voice channel. Please join or "~summon" me')


    return True
