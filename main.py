import time
import config
from telethon import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest

client = TelegramClient("anon", config.API_ID, config.API_HASH)

async def main():
    last_time_string = ''

    while True:
        local_time = time.localtime()
        time_string = time.strftime("%H:%M", local_time)
        time.sleep(2)

        if time_string != last_time_string:
            await client(UpdateProfileRequest(first_name=config.NAME.replace('{T}', str(time_string))))
            last_time_string = time_string
			
with client:
    while True:
        try:
            client.loop.run_until_complete(main())
            time.sleep(15)
        except KeyboardInterrupt:
            exit()
