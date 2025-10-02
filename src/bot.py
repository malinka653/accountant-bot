from os import environ
from telegram.ext import CommandHandler, ApplicationBuilder, ContextTypes
from utils.configure import load_config
from utils.context import DBContext, init_db, shutdown_db
from handlers import start, helper, spend, transfer, status, reset


def main() -> None:
    load_config()

    api_key = environ['API_KEY']
    app = (
        ApplicationBuilder()
        .token(api_key)
        .context_types(ContextTypes(context=DBContext))
        .post_init(init_db)
        .post_shutdown(shutdown_db)
        .build()
    )

    # Handlers
    app.add_handler(CommandHandler("start", start.start))
    app.add_handler(CommandHandler("help", helper.helper))
    app.add_handler(CommandHandler("spend", spend.spend))
    app.add_handler(CommandHandler("transfer", transfer.transfer))
    app.add_handler(CommandHandler("status", status.status))
    app.add_handler(CommandHandler("reset", reset.reset))

    app.run_polling()


if __name__ == '__main__':
    main()
