from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import os

TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["گزینه ۱"],
        ["گزینه ۲"],
        ["گزینه ۳"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "یکی از گزینه‌ها رو انتخاب کن:",
        reply_markup=reply_markup
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "گزینه ۱":
        await update.message.reply_text("پیام مربوط به گزینه ۱")
    elif text == "گزینه ۲":
        await update.message.reply_text("پیام مربوط به گزینه ۲")
    elif text == "گزینه ۳":
        await update.message.reply_text("پیام مربوط به گزینه ۳")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()
