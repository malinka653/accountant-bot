from os import environ
from telegram.ext import CommandHandler, ApplicationBuilder
from src.utils.configure import load_config
from src.utils.db_handler import init_db, shutdown_db
from src.handlers import start, helper, spend, transfer, status, reset, register


def main() -> None:
    load_config()

    api_token = environ['API_TOKEN']
    app = (
        ApplicationBuilder()
        .token(api_token)
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
    app.add_handler(CommandHandler("register", register.register))

    app.run_polling()


if __name__ == '__main__':
    main()
