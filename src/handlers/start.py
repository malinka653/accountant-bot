from telegram import Update
from telegram.ext import ContextTypes


# pylint: disable=unused-argument
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hello. /help for help.")
