import logging
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("🌐 Google", url="https://google.com"),
            InlineKeyboardButton("နှိပ်ကြည့်ပါ ✨", callback_data="click_event")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("မင်္ဂလာပါ။ Server ပေါ်မှ အလုပ်လုပ်နေပါပြီ:", reply_markup=reply_markup)

async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text="ခလုတ်ကို အောင်မြင်စွာ နှိပ်လိုက်ပါပြီ! 🎉")

if __name__ == '__main__':
    # Token ကို Environment Variable ကနေ ဆွဲယူသုံးပါမည် (လုံခြုံရေးအတွက်)
    TOKEN = os.environ.get("8210097954:AAGpcNyX20W2vXcNj3PxTjf5xHYjn49M26k")

    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_click))

    print("Bot စတင် အလုပ်လုပ်နေပါပြီ...")
    app.run_polling(stop_signals=None)

