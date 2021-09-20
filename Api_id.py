# Bu fayl ishga tushishi bilan api_id va api_hash berilgan qiymatga teng bo'lgan userlarda chats da ko'rsatilgan userlardan
# xabar kelsa yoki yuborilsa xabar haqidagi to'liq malumot ekranga chiqadi matn o'zgaradi

import os
try:
    from telethon.sync import TelegramClient
    from telethon import TelegramClient,events,sync
    from telethon import functions,types
except:
    os.system('pip install telethon')
    from telethon.sync import TelegramClient
    from telethon import TelegramClient,events,sync
    from telethon import functions,types

api_id = 0000000 # my.telegram.org dan olinadi
api_hash = ""   # my.telegram.org dan olinadi

def funksiya():
    client = TelegramClient('session_name', api_id, api_hash)
    client.start()
    @client.on(events.NewMessage(chats=('@XabarnomalarBot','https://t.me/kunuz')))
    async def normal_handler(event):
        print(event.message)
        print(event.message.to_dict()['message'])

    client.run_until_disconnected()
funksiya()