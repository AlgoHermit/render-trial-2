import telepot 
from time import sleep

TOKEN = '5469986479:AAHQ9JJSovHBW4WDbEgOSPbycOZw4l_i11w' 
receiver = 643179948

bot = telepot.Bot(TOKEN)

for i in range(1200):
    bot.sendMessage(receiver, f"render-2, {str(i)}")
    print(f"render-2, {str(i)}")
    sleep(5)