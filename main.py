from pyrogram import Client, filters
from dotenv import load_dotenv
from pyrogram.types import Message
import os

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
    # Send image as start message
    await client.send_photo(chat_id=message.chat.id, photo=image_path, caption="Hello! I am a bot that can ban all members in a group. To use me, simply add me to a group and send the command /banall.")

# Handler for the /banall command
@app.on_message(filters.group & filters.command("banall"))
async def banall_members(client, message):
    await start_banall(client, message)

# Run bot
app.run()
