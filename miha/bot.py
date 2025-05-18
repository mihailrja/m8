from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я бот. Напиши /link чтобы получить ссылку.")

# Команда /link
async def link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = (
        "Вот полезные ссылки по теме изменения климата:\n"
        "1. https://www.c40.org/ru/news/ipcc-one-point-five/"
        "2. https://trends.rbc.ru/trends/green/65c5e8729a79473772bd6742"
        "3. https://www.sobaka.ru/smr/ecology/ecology/196675"
    )
    await update.message.reply_text(message)
# Основной запуск
if __name__ == '__main__':
    app = ApplicationBuilder().token("7718610323:AAGzAI9Sl8M_ZSKugh8IFII48WnnzLZ0deQ").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("link", link))

    print("Бот запущен...")
    app.run_polling()