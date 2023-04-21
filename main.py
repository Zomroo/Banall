from RiZoeLX.functions import start_banall
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv
import os
import urllib.request


# Get environment variables
load_dotenv(".env")
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")

# Download image
image_url = "https://graph.org/file/6ca6f6b49add32b557681.jpg"
image_path = "image.jpg"
urllib.request.urlretrieve(image_url, image_path)

# Create client
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Handler for the /start command
@app.on_message(filters.private & filters.command("start"))
async def start_command_handler(client, message):
    # Create inline keyboard with two buttons
    inline_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Button 1", url="https://www.example.com"),
                InlineKeyboardButton(text="Button 2", url="https://www.google.com"),
            ],
            [
                InlineKeyboardButton(text="Close", callback_data="close"),
            ],
        ]
    )
    
    # Send image with inline keyboard as start message
    await client.send_photo(
        chat_id=message.chat.id,
        photo=image_path,
        caption="Hello! I am a bot that can ban all members in a group. To use me, simply add me to a group and send the command /banall.",
        reply_markup=inline_keyboard,
    )

# Handler for the /banall command
@app.on_message(filters.group & filters.command("banall"))
async def banall_members(client, message):
    await start_banall(client, message)

# Run bot
app.run()
