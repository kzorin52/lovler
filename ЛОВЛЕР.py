from telethon import TelegramClient, events, sync
import re

api_id = '2014171'
api_hash = 'f188cfdc16e910da8098d88761443b79'
regex = r"BTC_CHANGE_BOT\?start="

client = TelegramClient('session', api_id, api_hash)

print('Authorized')

@client.on(events.NewMessage())
async def normal_handler(event):
    user_mess = event.message.to_dict()['message']
    
    print(user_mess)
    if re.search(r'BTC_CHANGE_BOT\?start=', user_mess):
        m = re.search(r'c_[0-9a-fA-F]+', user_mess)
        await client.send_message('BTC_CHANGE_BOT', '/start ' + m.group(0))
        print(m.group(0))

print('/BTC Lovler by Temnij/ started!')

client.start()
client.run_until_disconnected()