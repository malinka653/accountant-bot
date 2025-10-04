from telegram import Update
from telegram.ext import ContextTypes
from tinydb import Query
from tinydb.operations import subtract


async def status(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    db = context.bot_data['db']
    chat_id = update.message.chat_id

    if len(context.args) > 1:
        await context.bot.send_message(chat_id, text='Too many arguments. They aren\'t shekels - you can never have too many of those.')
        return None

    entry = Query()
    dicts = list(db.search(entry.chat_id == chat_id))
    dicts.sort(key=lambda x: x['spent'])
    to_decrease = dicts[0]['spent']
    n = len(dicts)
    total_spent = sum(item['spent'] for item in dicts)
    average = total_spent / n
    owes = [average - item['spent'] for item in dicts]
    transfers = {}
    l = 0
    r = n - 1
    while l < r:
        if abs(owes[l]) == abs(owes[r]):
            transfers[(l, r)] = owes[l]
            l += 1
            r -= 1
        elif abs(owes[l]) > abs(owes[r]):
            transfers[(l, r)] = abs(owes[r])
            owes[l] += owes[r]
            r -= 1
        else:
            transfers[(l, r)] = abs(owes[l])
            owes[r] += owes[l]
            l += 1

    if len(context.args) == 1:
        transactions = 0
        index = next((i for i, item in enumerate(dicts)
                      if item['username'] == context.args[0]), None)
        message_text = 'Goy, you owe:\n'
        for (from_index, to_index), amount in transfers.items():
            if from_index == index:
                message_text += f'@{dicts[from_index]['username']} -> @{dicts[to_index]['username']}: {amount} shekels\n'
                transactions += 1

        if transactions == 0:
            message_text = 'Dirty goy, how did you manage to clear your debts?'
    else:
        transactions = 0
        message_text = 'Goyims, you owe:\n'
        for (from_index, to_index), amount in transfers.items():
            message_text += f'@{dicts[from_index]['username']} -> @{dicts[to_index]['username']}: {amount} shekels\n'
            transactions += 1

        if transactions == 0:
            message_text = 'Goyims, you only owe your love to Israel. And 150 billion shekels, too.'

    await context.bot.send_message(chat_id, text=message_text)

    db.update(subtract('spent', to_decrease),
              entry.chat_id == chat_id)  # to prevent overflow
