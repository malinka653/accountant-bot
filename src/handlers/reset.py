# pylint: disable=unused-import

from telegram import Update
from telegram.ext import ContextTypes

# pylint: disable=unused-argument


async def reset(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await 1
