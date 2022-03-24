import discord, asyncio, terra
from decouple import config
from datetime import datetime as dt

token = config('token')

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
      amount = 1
      price = float(terra.swap(amount, 'luni'))
      price = str(price/1000000)

      await bot.change_presence(activity = discord.Activity(type = 3, name = 'LUNI : $' + price))
    
      print(time + ' - Price retrieved @ ' + price)
      print('.........................................')
      
      await asyncio.sleep(10)

    except:

      return

bot.run(token)