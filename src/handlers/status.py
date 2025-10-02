# pylint: disable=unused-import
from telegram import Update
from src.utils.context import DBContext

# pylint: disable=unused-argument


async def status(update: Update, context: DBContext) -> None:
    await 1
