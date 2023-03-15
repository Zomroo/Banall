import asyncio
import logging
from pyrogram.errors import ChatAdminRequired, FloodWait
from pyrogram import Client, filters

# Set up the Pyrogram client
api_id = 15849735
api_hash = "b8105dc4c17419dfd4165ecf1d0bc100"
bot_token = "5619054777:AAF_XsEHxhJ7aXRRKowWzCR6R2u3vC1Hsi8"
bot = Client(":memory:", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Configure logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logging.getLogger("pyrogram").setLevel(logging.WARNING)

# Define the banall command handler
@bot.on_message(filters.command("banall"))
async def ban_all_members(bot, message):
    # Check if the user is an administrator in the chat
    chat_id = message.chat.id
    user_id = message.from_user.id
    try:
        chat_member = await bot.get_chat_member(chat_id, user_id)
        if not chat_member.status in ("creator", "administrator"):
            raise ChatAdminRequired
    except ChatAdminRequired:
        await message.reply("You need to be a chat administrator to use this command.")
        return

    # Ban all members in the chat
    async for chat_member in bot.iter_chat_members(chat_id):
        user_id = chat_member.user.id
        try:
            await bot.ban_chat_member(chat_id, user_id)
            logging.info(f"Banned {user_id} from {chat_id}")
        except FloodWait as e:
            logging.warning(f"FloodWait exception: {e}")
            await asyncio.sleep(e.x)
        except Exception as e:
            logging.error(f"Failed to ban {user_id} from {chat_id}: {e}")

    # Send a message when the process is completed
    await message.reply("All members in the chat have been banned.")

# Define the start command handler
@bot.on_message(filters.command("start") & filters.private)
async def start(bot, message):
    await message.reply("Hello! This is the Banall bot. I can ban all members in a group in seconds! Simply promote me to an admin and type /banall to use the command.")

# Start the bot
if __name__ == "__main__":
    bot.run()
