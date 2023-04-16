from RiZoeLX.functions import start_banall
from pyrogram import Client, filters
from pyrogram.types import Message
import os


app = Client('my_bot', api_id=15849735, api_hash="b8105dc4c17419dfd4165ecf1d0bc100", bot_token="5984667167:AAFLwhlM5--e_3JbWN-MieYcJxH-77zPEYw")

@app.on_message(filters.group & filters.command("banall"))
async def banall_members(client, message):
   await start_banall(client, message)

app.run()
