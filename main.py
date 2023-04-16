from RiZoeLX.functions import start_banall
from pyrogram import Client, filters
from pyrogram.types import Message
from dotenv import load_dotenv
import os


app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.group & filters.command("banall"))
async def banall_members(client, message):
   await start_banall(client, message)

app.run()
