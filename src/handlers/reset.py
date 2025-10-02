from telegram import Update
from telegram.ext import ContextTypes
from tinydb import Query
from tinydb.operations import set as change_to


async def reset(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    db = context.bot_data['db']
    chat_id = update.message.chat_id

    entry = Query()
    db.update(change_to('spent', 0), entry.chat_id == chat_id)

    await context.bot.send_message(chat_id, 'All loans are now 0.')
