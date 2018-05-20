import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
from datetime import datetime




time = datetime.now()
#print(time.hour, ":" ,time.minute, ":" ,time.second)
hora = str(22-int(time.hour)) + ":" + str(60-int(time.minute)) + ":" + str(60-int(time.second))
#print ("<@%s> Restam",hora,"horas pra acessar https://www.kabum.com.br/ antes de você ter que ir dormir")

Client = discord.Client()
client = commands.Bot(command_prefix = "!")


@client.event
async def on_ready():
    print("Bot is online and connected to Discord")


@client.event
async def on_message(message):
    if message.content.upper().startswith('!CESAR'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Restam "  % (userID) + hora + " horas para Cesar acessar https://www.kabum.com.br/ antes dele ter que ir dormir")

# @client.event
# async def on_member_update(before,after): 
#   await client.send_message(message.channel, "<@%s> Restam "  % (userID) + hora + " horas para Cesar acessar https://www.kabum.com.br/ antes dele ter que ir dormir")
   
#    ''' 
#     counter = 0
# async for message in channel.history(limit=200):
#     if message.author == client.user:
#         counter += 1
# '''

@client.event
async def on_member_update(before,after):
    print("mudou o status")
    # Message(message)
    # message.author = after
    # message.content = 'HAUWISEHIASeiushiuhi'
    # message.channel = 
    
    if(str(after)== "Spellcaster#3310"):
        print('mudando o status')
        await client.send_message(after,mensagem)
        #await client.send_message(message.channel, "César vá dormirPara seus pais não brigarem")
    #await client.send_message(message.channel, "<@%s> Restam "  % (userID) + hora + " horas para Cesar acessar https://www.kabum.com.br/ antes dele ter que ir dormir")
client.run("NDQ3NjU0NzgxNzEyOTkwMjA4.DeK8UA.QFm3LRchFz5wk2LxBRKdsaoG5QY") #Replace token with your bots token

