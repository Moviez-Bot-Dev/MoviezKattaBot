
import logging
import logging.config

# Get logging configurations
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("imdbpy").setLevel(logging.ERROR)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("aiohttp").setLevel(logging.ERROR)
logging.getLogger("aiohttp.web").setLevel(logging.ERROR)


from pyrogram import Client, __version__
from pyrogram.raw.all import layer
from database.ia_filterdb import Media
from database.users_chats_db import db
from info import *
from utils import temp
from typing import Union, Optional, AsyncGenerator
from pyrogram import types
from Script import script 
from datetime import date, datetime 
import pytz
from aiohttp import web
from plugins import web_server

import asyncio
from pyrogram import idle
from maniabot import MoviezKattaBot
from util.keepalive import ping_server
from maniabot.clients import initialize_clients


PORT = "8080"
MoviezKattaBot.start()
loop = asyncio.get_event_loop()

# async def iter_messages(
#     client,
#     chat_id: Union[int, str],
#     limit: int,
#     offset: int = 0,
# ) -> Optional[AsyncGenerator["types.Message", None]]:
#     """Iterate through a chat sequentially.
#     This convenience method does the same as repeatedly calling :meth:`~pyrogram.Client.get_messages` in a loop, thus saving
#     you from the hassle of setting up boilerplate code. It is useful for getting the whole chat messages with a
#     single call.
#     Parameters:
#         client (:obj:`pyrogram.Client`):
#             The Pyrogram client instance.
            
#         chat_id (``int`` | ``str``):
#             Unique identifier (int) or username (str) of the target chat.
#             For your personal cloud (Saved Messages) you can simply use "me" or "self".
#             For a contact that exists in your Telegram address book you can use his phone number (str).
            
#         limit (``int``):
#             Identifier of the last message to be returned.
            
#         offset (``int``, *optional*):
#             Identifier of the first message to be returned.
#             Defaults to 0.
#     Returns:
#         ``Generator``: A generator yielding :obj:`~pyrogram.types.Message` objects.
#     Example:
#         .. code-block:: python
#             for message in iter_messages(client, "pyrogram", 1, 15000):
#                 print(message.text)
#     """
#     current = offset
#     while True:
#         new_diff = min(200, limit - current)
#         if new_diff <= 0:
#             return
#         messages = await client.get_messages(chat_id, list(range(current, current + new_diff + 1)))
#         for message in messages:
#             yield message
#             current += 1

async def Mania_start():
    print('\n')
    print('Initalizing Telegram Bot ')
    bot_info = await MoviezKattaBot.get_me()
    MoviezKattaBot.username = bot_info.username
    await initialize_clients()
    if ON_HEROKU:
        asyncio.create_task(ping_server())
    b_users, b_chats = await db.get_banned()
    temp.BANNED_USERS = b_users
    temp.BANNED_CHATS = b_chats
    await Media.ensure_indexes()
    me = await MoviezKattaBot.get_me()
    temp.ME = me.id
    temp.U_NAME = me.username
    temp.B_NAME = me.first_name
    MoviezKattaBot.username = '@' + me.username
    app = web.AppRunner(await web_server())
    await app.setup()
    bind_address = "0.0.0.0"
    logging.info(f"{me.first_name} with for Pyrogram v{__version__} (Layer {layer}) started on {me.username}.")
    logging.info(LOG_STR)
    tz = pytz.timezone('Asia/Kolkata')
    today = date.today()
    now = datetime.now(tz)
    time = now.strftime("%H:%M:%S %p")
    await MoviezKattaBot.send_message(chat_id=LOG_CHANNEL, text=script.RESTART_TXT.format(today, time))
    app = web.AppRunner(await web_server())
    await app.setup()
    bind_address = "0.0.0.0"
    await web.TCPSite(app, bind_address, PORT).start()
    await idle()


if __name__ == '__main__':
    try:
        loop.run_until_complete(Mania_start())
    except KeyboardInterrupt:
        logging.info('----------------------- Service Stopped -----------------------')
