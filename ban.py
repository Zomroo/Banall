from pyrogram import Client, filters
from pyrogram.types import ChatPermissions

# Define your bot token here
API_ID = 15849735
API_HASH = 'b8105dc4c17419dfd4165ecf1d0bc100'
BOT_TOKEN = '5619054777:AAF_XsEHxhJ7aXRRKowWzCR6R2u3vC1Hsi8'

# Create the Pyrogram client
app = Client('my_bot', api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Define the ban_all command handler
@app.on_message(filters.command('banall'))
def ban_all_command_handler(client, message):
    # Get the chat ID and the user ID of the person who triggered the command
    chat_id = message.chat.id
    user_id = message.from_user.id
    
    # Check if the user is an administrator in the chat
    chat_member = client.get_chat_member(chat_id, user_id)
    if chat_member.status not in ['creator', 'administrator']:
        message.reply('You must be an admin to use this command.')
        return
    
    # Get the list of group members
    members = client.get_chat_members(chat_id)
    
    # Ban each group member
    for member in members:
        user_id = member.user.id
        client.restrict_chat_member(chat_id, user_id, ChatPermissions())
    
    # Send a confirmation message
    message.reply('All group members have been banned.')

# Start the bot
app.run()
