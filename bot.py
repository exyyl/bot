import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Токен из переменных окружения
TOKEN = os.environ.get('BOT_TOKEN')

if not TOKEN:
    print("ERROR: BOT_TOKEN not set!")
    exit(1)

# Простое логирование
logging.basicConfig(level=logging.INFO)

# Создаем бота
application = Application.builder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Привет! Я работаю!')

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Ты написал: {update.message.text}')

# Добавляем обработчики
application.add_handler(CommandHandler("start", start))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

if __name__ == '__main__':
    print("Бот запущен!")
    application.run_polling()
