import json
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters

# Load or initialize the list of user IDs
try:
    with open('users.json', 'r') as file:
        user_ids = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    user_ids = []

# Replace 'YOUR_TOKEN_HERE' with your bot's token
TOKEN = '7197297531:AAEpWy4DGrJkN28CtxO143gRtWRo9afOZH8'

def start(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    if user_id not in user_ids:
        user_ids.append(user_id)
        # Save the updated user_ids list
        with open('users.json', 'w') as file:
            json.dump(user_ids, file)
        context.bot.send_message(chat_id=user_id, text="Welcome! You're now subscribed to broadcasts.")

def broadcast(update: Update, context: CallbackContext):
    # Ensure the command is from the admin (for example, yourself)
    # You should replace 'YOUR_USER_ID' with your actual Telegram user ID
    if update.effective_user.id == YOUR_USER_ID:
        message = ' '.join(context.args)
        for user_id in user_ids:
            context.bot.send_message(chat_id=user_id, text=message)
    else:
        update.message.reply_text("You do not have permission to use this command.")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    
    # Handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("broadcast", broadcast))
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
