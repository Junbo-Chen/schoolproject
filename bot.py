# async def send_message(message, user_message, is_private):
#     try:
#         response = project.handle_message(user_message)
import discord
import project

async def play_dice(mesage, user_message):
    try:
        dice = project.roll_dice(user_message)
        await message.author.send(dice)
    except Exception as e:
        print(e)
        
def run_discord_bot():
    token = 'MTAyOTc1NzgxMjQxMjI2NDU1OA.GUnxM4.RB0TDBgdlzjKKJaWwM_z0cy4ZT-h2K7OMLom08'
    client = discord.client()

    @client.event
    async def on_ready():
        print(f'{client.user} is now running')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        username = str(message.author)
        user_message = str(message.content)
        print(f"{username}said: {user_message}")


    client.run(token)