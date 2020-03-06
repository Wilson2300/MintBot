import discord
import os


client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("테스트"))
    print("ready")
    print(client.user.name)
    print(client.user.id)

@client.event
async def on_message(message):
    if message.author.bot:
        return None

    if message.content == "!테스트":
        await message.channel.send("성공")
    if message.content.startswith == "근데 솔직히":
        await message.channel.send("인정합니다.")

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
