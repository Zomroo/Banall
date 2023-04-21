from RiZoeLX.functions import start_banall
from pyrogram import Client, filters
from pyrogram.types import Message
from dotenv import load_dotenv
import os

load_dotenv(".env")
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Handler for the /start command
@app.on_message(filters.private & filters.command("start"))
async def start_command_handler(client, message):
    await message.reply_text("Hello! I am a bot that can ban all members in a group. To use me, simply add me to a group and send the command /banall.")

# Handler for the /banall command
@app.on_message(filters.group & filters.command("banall"))
async def banall_members(client, message):
    await start_banall(client, message)

app.run()
