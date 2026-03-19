from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = "8643101157:AAFc3VErrQ_6R-iYwrSlTDfZuGNLK3OPKVQ"
WEBAPP_URL = "https://shinobi-ai.github.io/discipline-index-bot/"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton(
        "⚔️ Открыть Discipline Index",
        web_app=WebAppInfo(url=WEBAPP_URL)
    )]]
    await update.message.reply_text(
        "⚔️ *Discipline Index*\n\nТрекер роста капитала и дисциплины трейдера.",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

if __name__ == "__main__":
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
