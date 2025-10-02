from telegram import Update
from telegram.ext import ContextTypes
from tinydb import Query
from tinydb.operations import add, subtract


async def transfer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    db = context.bot_data['db']
    transferred_from = update.message.from_user.username
    chat_id = update.message.chat_id

    # pylint: disable=unused-variable
    # pylint: disable=broad-exception-caught
    try:
        transferred = int(context.args[0])
    except Exception as e:
        # log the error TODO
        await context.bot.send_message(update.message.chat_id, text='dumbass how did you manage to not get this right??')
        return None

    try:
        transferred_to = context.args[1][1:]
    except Exception as e:
        # log the error TODO
        await context.bot.send_message(update.message.chat_id, text='dumbass how did you manage to not get this right??')
        return None

    entry = Query()
    if not db.contains((entry.username == transferred_from) & (entry.chat_id == chat_id)):
        db.insert({'username': transferred_from,
                  'chat_id': chat_id, 'spent': 0})

    if not db.contains((entry.username == transferred_to) & (entry.chat_id == chat_id)):
        db.insert({'username': transferred_to, 'chat_id': chat_id, 'spent': 0})

    db.update(add('spent', transferred), (entry.username ==
              transferred_from) & (entry.chat_id == chat_id))
    db.update(subtract('spent', transferred), (entry.username ==
              transferred_to) & (entry.chat_id == chat_id))

    await context.bot.send_message(update.message.chat_id, text='Registered shekel transfer.')
