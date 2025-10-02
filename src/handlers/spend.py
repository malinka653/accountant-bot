from telegram import Update
from telegram.ext import ContextTypes
from tinydb import Query
from tinydb.operations import add


async def spend(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    db = context.bot_data['db']
    username = update.effective_user.username
    chat_id = update.message.chat_id

    # pylint: disable=unused-variable
    # pylint: disable=broad-exception-caught
    try:
        just_spent = int(context.args[0])
    except Exception as e:
        # log the error TODO
        await context.bot.send_message(chat_id, text='dumbass how did you manage to not get this right??')
        return None

    entry = Query()
    if db.contains((entry.username == username) & (entry.chat_id == chat_id)):
        db.update(add('spent', just_spent),
                  (entry.username == username) & (entry.chat_id == chat_id))
    else:
        db.insert({'username': username, 'chat_id': chat_id, 'spent': just_spent})

    await context.bot.send_message(chat_id, f'Recorded a donation of {just_spent} billion dollars to Israel.\nAm Yisrael Chai. אני אוהב כסף ')
