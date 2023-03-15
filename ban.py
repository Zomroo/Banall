import telegram
from telegram.ext import CommandHandler, Updater

# Define your bot token here
TOKEN = '5619054777:AAF_XsEHxhJ7aXRRKowWzCR6R2u3vC1Hsi8'

def ban_all(update, context):
    # Get the chat ID and bot object
    chat_id = update.message.chat_id
    bot = context.bot
    
    # Get the list of group members
    members = bot.get_chat_members(chat_id)
    
    # Ban each group member
    for member in members:
        user_id = member.user.id
        bot.kick_chat_member(chat_id, user_id)
    
    # Send a confirmation message
    bot.send_message(chat_id=chat_id, text='All group members have been banned.')

# Create the updater and dispatcher
updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Register the ban_all command handler
ban_all_handler = CommandHandler('banall', ban_all)
dispatcher.add_handler(ban_all_handler)

# Start the bot
updater.start_polling()
updater.idle()
