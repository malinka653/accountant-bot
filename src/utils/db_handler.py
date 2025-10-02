from telegram.ext import ContextTypes
from tinydb import TinyDB
from src.utils.paths import DB_DIR


async def init_db(context: ContextTypes.DEFAULT_TYPE):
    if 'db' not in context.bot_data.keys():
        context.bot_data['db'] = TinyDB(f'{DB_DIR}/db.json')


async def shutdown_db(context: ContextTypes.DEFAULT_TYPE):
    if 'db' in context.bot_data.keys():
        context.bot_data['db'].close()
