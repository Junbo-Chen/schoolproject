import asyncio
import random
import discord
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image

client = discord.Client()
    
@client.event    
async def on_ready():
    print(f'{client.user} is now running')
    game = discord.Game('loserlife')
    await client.change_presence(status=discord.Status.idle, activity=game)

@client.event
async def on_message(m):
    if m.author == client.user:
        return

    if m.content == '<@1029757812412264558> ping':
        await m.channel.send('pong')
    
    if m.content == '<@1029757812412264558> yoman':
        tmpmsg = await m.channel.send("wie ben jij")
        await asyncio.sleep(3)
        await tmpmsg.delete()
    
    if m.content == '<@1029757812412264558> hello':
        await m.channel.send(f'hi{m.author}')
    
    if m.content == '<@1029757812412264558> play':
        x = "y"
        score = 0

        while x == "y":
            doublesteen = random.randint(1,6)
            dt = random.randint(7,12) 

            if doublesteen == 1:
                punt = 1
                await m.channel.send("you rolled a 1")
                await m.channel.send(file=discord.File('C:\IdeaProjects\project\schoolproject\img\dt1.gif'))
            if doublesteen == 2:
                punt = 2
                await m.channel.send("you rolled a 2")
                await m.channel.send(file=discord.File('C:\IdeaProjects\project\schoolproject\img\dt2.gif'))
            if doublesteen == 3:
                punt = 3
                await m.channel.send("you rolled a 3")
                await m.channel.send(file=discord.File('C:\IdeaProjects\project\schoolproject\img\dt3.gif'))
            if doublesteen == 4:
                punt = 4
                await m.channel.send("you rolled a 4")
                await m.channel.send(file=discord.File('C:\IdeaProjects\project\schoolproject\img\dt4.gif'))
            if doublesteen == 5:
                punt = 5
                await m.channel.send("you rolled a 5")
                await m.channel.send(file=discord.File('C:\IdeaProjects\project\schoolproject\img\dt5.gif'))
            if doublesteen == 6:
                punt = 6
                await m.channel.send("you rolled a 6")
                await m.channel.send(file=discord.File('C:\IdeaProjects\project\schoolproject\img\dt6.gif'))
            if dt == 7:
                punt2 = 1
                await m.channel.send("machine rolled a 1")
                await m.channel.send(file=discord.File('C:\IdeaProjects\project\schoolproject\img\dt1.gif'))
            if dt == 8:
                punt2 = 2
                await m.channel.send("machine rolled a 2")
                await m.channel.send(file=discord.File('C:\IdeaProjects\project\schoolproject\img\dt2.gif'))
            if dt == 9:
                punt2 = 3
                await m.channel.send("machine rolled a 3")
                await m.channel.send(file=discord.File('C:\IdeaProjects\project\schoolproject\img\dt3.gif'))
            if dt == 10:
                punt2 = 4
                await m.channel.send("machine rolled a 4")
                await m.channel.send(file=discord.File('C:\IdeaProjects\project\schoolproject\img\dt4.gif'))
            if dt == 11:
                punt2 = 5
                await m.channel.send("machine rolled a 5")
                await m.channel.send(file=discord.File('C:\\IdeaProjects\\project\\schoolproject\\img\\dt5.gif'))
            if dt == 12:
                punt2 = 6
                await m.channel.send("machine rolled a 6")
                await m.channel.send(file=discord.File('C:\IdeaProjects\project\schoolproject\img\dt6.gif'))
            if punt > punt2:
                await m.channel.send("you win")
                score = score + 1
            elif punt < punt2:
                await m.channel.send("you lose")
                score = score - 1
            else:
                await m.channel.send("draw")
                score + 0

            await m.channel.send("press y to roll again and n to exit:")
            def check(m):
                return m.author == m.author and m.channel == m.channel and \
                m.content.lower() in ['<@1029757812412264558> y', '<@1029757812412264558> n']

            msg = await client.wait_for('message', check=check)
            checkcontinue = msg.content.lower()
            if checkcontinue == '<@1029757812412264558> n':
                x = "n"
                await m.channel.send("your score is:")
                await m.channel.send(score)
                await m.channel.send("thanks for playing")
                if score > 10:
                    await m.channel.send(file=discord.File('C:\IdeaProjects\project\schoolproject\img\duim.png'))
                if(score < 0):
                    await m.channel.send(file=discord.File('C:\IdeaProjects\project\schoolproject\img\L.png'))
            else:
                x = "y"
                await m.channel.send("your score is:")
                await m.channel.send(score)
            # x=input("press y to roll again and n to exit:")
            # await m.channel.send("\n")

    username = str(m.author)
    botname = str(client.user)
    user_message = str(m.content)
    print(f"{username} said: {user_message}")


client.run('MTAyOTc1NzgxMjQxMjI2NDU1OA.GJeiyn.5NKG-Cd0edILAhkkXHhnDdD27c06K1eV1akMSc')