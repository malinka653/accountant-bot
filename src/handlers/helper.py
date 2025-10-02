from telegram import Update
from telegram.ext import ContextTypes


async def helper(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(update.message.chat_id, text='''
Hello goyims, Gaza children and other non-Israelites.
                                   
/spend adds money that you have spent. Example: /spend 200
If you wish to include details, add them after a linebreak or space.

/transfer is used to register a transfer of mone
Usage: /transfer 200 @jew_accountant_bot
                                   
/status prints out a message with information about how much everyone owes to everyone.
Alternatively, /status @someone prints how much @someone owes everyone.
                                   
/reset transfers all of your money to me and makes your loans 0. 
Am Yisrael Chai. אני אוהב כסף '''
                                   )
