import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# === ТВОЙ ТОКЕН ===
TOKEN = "7949352913:AAH1EX2wgWsIb5WBgdqq4RV7R8XoVnYT3PE"

# === ИМЯ PDF ===
PDF_FILE = "AI_Контент_Гайд.pdf"

# === ОБРАБОТЧИКИ ===

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📘 Привет! Вот твой PDF-гайд 👇")
    await context.bot.send_document(
        chat_id=update.effective_chat.id,
        document=open(PDF_FILE, "rb")
    )
    await update.message.reply_text(
        "💳 Для доступа к шаблонам:\n"
        "Переведи 490₽ на карту 4893 4704 9814 3038\n"
        "Остренко Юрий Борисович\n\n"
        "✅ После оплаты — напиши /paid\n"
        "🤝 Хочешь стать партнёром? Жми /partner"
    )

async def paid(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✅ Оплата получена!\n"
        "Вот твои шаблоны: [сюда вставь ссылку или файлы]"
    )

async def partner(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤝 Партнёрка:\n"
        "Рассказывай друзьям о боте и получай 50%!\n"
        "Твоя ссылка: https://t.me/aiwriterkit_bot"
    )

# === ПРИЛОЖЕНИЕ ===

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("paid", paid))
app.add_handler(CommandHandler("partner", partner))

# === ЗАПУСК ЧЕРЕЗ WEBHOOK ===

print("Бот запущен через Webhook! 🚀")

app.run_webhook(
    listen="0.0.0.0",
    port=int(os.environ.get("PORT", 5000)),
    webhook_url="https://aiwriterkit-bot.onrender.com"
)
