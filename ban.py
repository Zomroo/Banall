from pyrogram import Client, filters
from pyrogram.types import ChatPermissions

# Define your bot token here
API_ID = 15849735
API_HASH = 'b8105dc4c17419dfd4165ecf1d0bc100'
BOT_TOKEN = '5619054777:AAF_XsEHxhJ7aXRRKowWzCR6R2u3vC1Hsi8'

# Create the Pyrogram client
app = Client('my_bot', api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Define the /banall command handler
@app.on_message(filters.command("banall") & filters.group)
def ban_all_command_handler(client, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    chat_member = client.get_chat_member(chat_id, user_id)
    
    if chat_member.status in ["administrator", "creator"]:
        # Get all members in the chat
        members = client.get_chat_members(chat_id)
        
        # Ban all members except for the bot and admins
        for member in members:
            member_id = member.user.id
            member_chat_member = client.get_chat_member(chat_id, member_id)
            if not member_bot and member_chat_member.status not in ["administrator", "creator"]:
                client.kick_chat_member(chat_id, member_id)
        
        # Send a message to confirm the ban
        message.reply_text("All members except for admins and the bot have been banned.")
        
    else:
        # If the user is not an admin, send an error message
        message.reply_text("You must be an admin to use this command.")


# Start the bot
app.run()
