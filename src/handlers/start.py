from telegram import Update
from telegram.ext import ContextTypes


# pylint: disable=unused-argument
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(update.message.chat_id, text="Shalom. /help for help.")
