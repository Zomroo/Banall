from RiZoeLX.functions import start_banall
from pyrogram import Client, filters
from pyrogram.types import Message
import os

app = Client('my_bot', api_id=6212330, api_hash="1dcf154704672a8c279126e1ecf229c3", bot_token="6069093151:AAExTCxMSLVcQW6mFekTXFw1MlUBlb0ktxg")

@app.on_message(filters.group & filters.command("banall"))
async def banall_members(client, message):
   await start_banall(client, message)

app.run()
