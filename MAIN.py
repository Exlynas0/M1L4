import discord
from Homework import *

# Variabel intents menyimpan hak istimewa bot
intents = discord.Intents.default()
# Mengaktifkan hak istimewa message-reading
intents.message_content = True
# Membuat bot di variabel klien dan mentransfernya hak istimewa
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Kita telah masuk sebagai {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('halo'):
        await message.channel.send("Hi!")
    elif message.content.startswith('Are you really the death?'):
        await message.channel.send("Yes! I am, but i'm also a member here!")
    elif message.content.startswith('$pass'):
        await message.channel.send(gen_pass(10))
    elif message.content.startswith('what type of weapon you like to use?'):
        await message.channel.send("It's Axe, Knife, scythe, and a Bow!")
    elif message.content.startswith('bye'):
        await message.channel.send("Thank you for the talk!")
    else:
        await message.channel.send(message.content)

client.run("MTIxMzQ3MDYyMjkzNjYwNDc2Mg.GInWLn.4tD_UTH2LSKjXHkc8OjZN9DalfakJLLBY025eM")