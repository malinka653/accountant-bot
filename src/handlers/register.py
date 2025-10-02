from telegram import Update
from telegram.ext import ContextTypes
from tinydb import Query


async def register(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    db = context.bot_data['db']
    chat_id = update.message.chat_id
    entry = Query()
    if len(context.args) > 0:
        for username in context.args:
            username = username[1:]
            if not db.contains((entry.username == username) & (entry.chat_id == chat_id)):
                db.insert(
                    {'username': username, 'chat_id': chat_id, 'spent': 0})
    else:
        username = update.message.from_user.username
        if not db.contains((entry.username == username) & (entry.chat_id == chat_id)):
            db.insert(
                {'username': username, 'chat_id': chat_id, 'spent': 0})
    await context.bot.send_message(chat_id, text='Registered in goyim database.')
