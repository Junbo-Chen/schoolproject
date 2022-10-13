import asyncio
import discord

client = discord.Client()
    
@client.event    
async def on_ready():
    print(f'{client.user} is now running')
    game = discord.Game('loserlife')
    await client.change_presence(status=discord.Status.idle, activity=game)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)
    print(f"{username} said: {user_message} in {channel}")


    if message.content == "yoman":
        tmpmsg = await message.channel.send("wie ben jij")
        await asyncio.sleep(3)
        await tmpmsg.delete()

    if message.content == 'ping':
        return 'pong'
    
client.run('MTAyOTc1NzgxMjQxMjI2NDU1OA.GUnxM4.RB0TDBgdlzjKKJaWwM_z0cy4ZT-h2K7OMLom08')