def strt():
    import telepot
    from time import sleep

    TOKEN = '5469986479:AAHQ9JJSovHBW4WDbEgOSPbycOZw4l_i11w' 
    receiver = 643179948

    bot = telepot.Bot(TOKEN)

    for i in range(1200):
        bot.sendMessage(receiver, str(i))
        sleep(5)
# # #strt()
print('hello')
# from time import sleep
# def loop():
#     for i in range(5):
#         print(i)
#         sleep(5)
# def stop():
#     quit()