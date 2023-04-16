from RiZoeLX.functions import start_banall
from pyrogram import Client, filters
from pyrogram.types import Message
from dotenv import load_dotenv
import os

load_dotenv(".env")
api_id = int(os.getenv("16844842"))
api_hash = os.getenv("f6b0ceec5535804be7a56ac71d08a5d4")
bot_token = os.getenv("5931504207:AAF-jzKC8USclrFYrtcaeAZifQcmEcwFNe4")

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.group & filters.command("banall"))
async def banall_members(client, message):
   await start_banall(client, message)

app.run()
