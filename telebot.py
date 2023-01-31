from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello  {update.effective_user.first_name}')


app = ApplicationBuilder().token("6172418592:AAG6SXMIKVpDLon0WDViA2Q-qiiQM_Gsb-Y").build()

app.add_handler(CommandHandler("hello", hello))


print('Hello')
app.run_polling()