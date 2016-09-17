import discord
import asyncio


votes=[]
voteStrings=[]
voters = []

async def vote(client, message):
    global voteStrings
    text = ""
    if message.content.startswith('~vote'):
        text += "Voting has begun make you vote now.\n"
        inVote = True
        voteStrings = message.content[5:].split(';')
        for i, v in enumerate(voteStrings):
            votes.append(0)
            text+=("~v" + str(i+1) + ": " + v + "\n")
            i+=1
        await client.send_message(message.channel, text)

    elif message.content.startswith('~endvote'):
        text += "End Vote\n"
        for i, v in enumerate(voteStrings):
            text += str(votes[i]) + ": " + v + "\n"
        voteStrings.clear()
        votes.clear()
        await client.send_message(message.channel, text)
            
    elif not (message.author.id in voters) and message.content.startswith('~v'):
        try:
            votes[int(message.content[2:])-1] += 1
            voters.append(message.author.id)
        except ValueError:
            print("VALUE ERROR")


