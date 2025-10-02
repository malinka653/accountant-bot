# pylint: disable=unused-import
from telegram import Update
from telegram.ext import ContextTypes
from src.utils.context import DBContext

# pylint: disable=unused-argument


async def transfer(update: Update, context: DBContext) -> None:
    await 1
