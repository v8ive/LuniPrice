import discord, os, asyncio, requests
from bs4 import BeautifulSoup as BS
from datetime import datetime as dt

token = os.getenv('token')

bot = discord.Client()

@bot.event
async def on_ready():
  print ("Starting up")
      
  
  print('Logged in as {0.user}'.format(bot))
  bot.loop.create_task(presence())        

async def presence():
  while True:

    try:
    
      currentTime = dt.now()
      time = currentTime.strftime('%H:%M:%S')

      url = "https://coinmarketcap.com/currencies/luni/"
      # getting the request from url 
      data = requests.get(url)
  
      # converting the text 
      soup = BS(data.text, 'html.parser')
  
      # finding meta info for the current price
      price = soup.find("div", class_ ="priceValue").text

      await bot.change_presence(activity = discord.Activity(type = 3, name = 'LUNI : ' + price))
    
      print(time + ' - Price retrieved @ ' + price)
      print('.........................................')
      
      await asyncio.sleep(5)

    except:

      return

bot.run(token)