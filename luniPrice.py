import discord
import os
from bs4 import BeautifulSoup as BS
import requests
from keepAlive import keep_alive
import asyncio

tokenPrice = os.getenv('tokenPrice')

luniPrice = discord.Client()

@luniPrice.event
async def on_ready():
  print ("Starting up")
      
  
  print('Logged in as {0.user}'.format(luniPrice))
  luniPrice.loop.create_task(presence())        

async def presence():
  while True:

    try:
    
      url = "https://coinmarketcap.com/currencies/luni/"
      # getting the request from url 
      data = requests.get(url)
  
      # converting the text 
      soup = BS(data.text, 'html.parser')
  
      # finding meta info for the current price
      price = soup.find("div", class_ ="priceValue").text

      await luniPrice.change_presence(activity = discord.Activity(type = 3, name = 'LUNI : ' + price))
    
      print('Price retrieved @' + price)
      print('Retrieving price...')
      await asyncio.sleep(1)

    except:

      return
    

keep_alive()

luniPrice.run(tokenPrice)