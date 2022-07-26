import discord
from discord.ext import tasks
import os
import requests
import json
import googlio
from datetime import datetime
import time
import asyncio

loop = asyncio.get_event_loop()

client = discord.Client()

now = datetime.now()

current_time = datetime.now().strftime("%H:%M:%S")

def get_quote():
  resp=requests.get("https://zenquotes.io/api/quotes/")
  jd=json.loads(resp.text)
  quote=jd[0]['q']
  return quote


@client.event
async def on_ready():
    print("We have logged as in {0.user}".format(client))
    
    
#names used later on in dis/respect
disrespec=['agni','asmit','diksha','abhranil','priyanka','aryan','ankana','agnideepto','ogni']
respec=['aritro','satyabrata','satya']
dad=['dad!','son!']

@client.event
async def on_message(mssg):
        
    if mssg.author == client.user:
      return
    else:
      await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=datetime.now().strftime("%H:%M:%S")))
    #QUOTES
    if mssg.content.startswith('quotes<'):
      q=get_quote()
      await mssg.channel.send(q)
      
    #GOOGLE
    if mssg.content.startswith('google<'):
      q=googlio.srch(mssg.content[7:])
      await mssg.channel.send(q)
    
    #displaying dis/respect when name is found 
    for word in respec:
      if word in mssg.content.lower():
        await mssg.channel.send('HEY! Respect Lord '+ word[0].upper()+word[1:].lower())
    
    for word in disrespec:
      if word in mssg.content.lower():
        await mssg.channel.send('No need to pay attention to '+ word[0].upper()+word[1:].lower())

    #DAD BOT
    for word in dad:
      if word in mssg.content.lower():
        await mssg.channel.send('SHUT THE F UP DAD BOT')


@client.event
async def on_group_join():
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=datetime.now().strftime("%H:%M:%S")))
@client.event  
async def on_group_remove():
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=datetime.now().strftime("%H:%M:%S")))
@client.event
async def on_message_delete(mssg):
  if 'hi' in mssg:
    await mssg.channel.send('GOD SAW WHAT U DELETED')
  
client.run(('OTI3NDc1MDg0MDY5ODUxMTk4.YdKwew.5ghGl5CYu8lNIzxgz246j4tqWuE'))

my_background_task()












