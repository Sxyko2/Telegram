import telegram
from telegram.ext import Updater, MessageHandler

bot_token = '6360692980:AAHP1KuZcZoo1JCoWURZ5Uc8pEkY088055I'
bot = telegram.Bot(token=bot_token)

# Replace 'YOUR_GROUP_CHAT_ID' with the chat ID of your group.
group_chat_id = 1758692034 # Example chat ID, replace with your group's ID.

def forward_media(update, context):
    media = update.message.photo[-1] if update.message.photo else None
    if media:
        bot.send_photo(chat_id=group_chat_id, photo=media.file_id)
    else:
        update.message.reply_text("I can only forward photos for now.")

def main():
    updater = Updater(token=bot_token, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(forward_media))

    updater.start_polling()
    updater.idle()

    main()
