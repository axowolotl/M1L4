import discord
from logic import gen_pass, gen_emodji, flip_coin

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
    if message.content.startswith('$hello'):
        await message.channel.send("haii qwq")
    elif message.content.startswith('$bye'):
        await message.channel.send("goodbye!")
    elif message.content.startswith('$bikinpassword'):
        await message.channel.send(gen_pass(10))
    elif message.content.startswith('$emote'):
        await message.channel.send(gen_emodji())
    elif message.content.startswith('$coin'):
        await message.channel.send(flip_coin())
    else:
        await message.channel.send(message.content)

client.run("")