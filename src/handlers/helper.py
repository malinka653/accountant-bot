from telegram import Update
from telegram.ext import ContextTypes


# pylint: disable=unused-argument
async def helper(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('''Hello goyims, Gaza children and other non-Israelites.
                                    /spend adds money that you have spent. Example: /spend 200
                                    If you wish to include details, add them after a linebreak or space. 
                                    /transfer is used to register a transfer of money. Usage: /transfer 200 @jew_accountant_bot
                                    /status prints out a message with information about how much everyone owes to everyone. 
                                    Am Yisrael Chai. אני אוהב כסף ''')
