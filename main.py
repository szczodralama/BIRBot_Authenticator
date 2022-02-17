import nextcord as discord
from discord.ext import commands
from discord.ext.commands import bot
import os
import discord


client = commands.Bot(command_prefix="!")
client = discord.Client()


# def get_quote():
#     response = requests.get(url="https://discord.com/api/guilds/941796543877480468/widget.json")
#     json_data = json.loads(response.text)
#     quote: object = json_data
#     return (quote)


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='Co za pieron z tego bota'))
    print('that Pieron has connected  ---> {0.user}'.format(client))


# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
#
#     if message.content.startswith('!pieron'):
#         await message.channel.send('https://tenor.com/view/patron-luis-gif-10533495')
#     channel = client.get_channel('okrągły-stół')
#     await channel.send('Pieron!')


# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
#
#     if message.content.startswith('!id'):
#         quote = get_quote()
#         await message.channel.send(quote)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!verif'):
        embedVar = discord.Embed(title='Weryfikacja zakończona pomyślnie!', description='Xamel#8225',color=0x00ff00)
        embedVar.set_footer(text='Od teraz możesz wysyłać wiadomości na kanałach tekstowych oraz rozmawiać na vc!')
        embedVar.set_image(
            url='https://cdn1.iconfinder.com/data/icons/basic-ui-icon-rounded-colored/512/icon-41-512.png')
        # embedVar.set_thumbnail('https://cdn1.iconfinder.com/data/icons/basic-ui-icon-rounded-colored/512/icon-41-512.png')
        embedVar.set_author(
            name='Xamel#8225',
            icon_url='https://cdn.discordapp.com/widget-avatars/JQN_Lr2zL7R5o4oQ-_qd-x7RvdAVPzfIrDFVqgL1lWA/Oksz5EQUGIoETA-txZMplTvaMrwFgHgKconXoARVpSwJSTl8Qw44XLMjvGyivzw9AxgC-R-3bMaAiPTuOSQQHdILRo8iR6X_p0RTpT6bZn2JiVwpMeL6w_uWvr-w-H_r6Zr8bFZulUkQKw')
        embedVar.add_field(name='Data utworzenia konta: ', value='29.03.2018, 12:35:16', inline=False)
        # embedVar.add_field(name='...', value='...', inline=True)
        # embedVar.add_field(name='...', value='...', inline=True)
        await message.channel.send(embed=embedVar)
    else:
        await message.channel.send("ERROR: invalid command. Twoja komenda jest jebanym inwalidą! --> run'beka_z_typa.exe'")
        return

############################################################################################################

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
#
#     if message.content.startswith('!pieron'):
#         await message.channel.send('https://tenor.com/view/patron-luis-gif-10533495')




client.run("")


