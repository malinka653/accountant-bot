from telegram.ext import ContextTypes
from tinydb import TinyDB
from paths import DB_DIR


class DBContext(ContextTypes.DEFAULT_TYPE):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.db: TinyDB = None


def init_db(context: DBContext):
    if not hasattr(context.bot, 'db'):
        context.bot.db = TinyDB(f'{DB_DIR}/db.json')


def shutdown_db(context: DBContext):
    if hasattr(context.bot, 'db'):
        context.bot.db.close()
