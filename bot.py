from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# 🔑 ТВОЙ ТОКЕН БОТА
TOKEN = "7949352913:AAH1EX2wgWsIb5WBgdqq4RV7R8XoVnYT3PE"

# 📄 ПУТЬ К PDF-ГАЙДУ
PDF_FILE = "AI_Контент_Гайд.pdf"  # Файл должен лежать в той же папке!

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📘 Привет! Вот твой PDF-гайд по AI-контенту 👇"
    )
    await context.bot.send_document(
        chat_id=update.effective_chat.id,
        document=open(PDF_FILE, "rb")
    )
    await update.message.reply_text(
        "💳 Для доступа к шаблонам:\n"
        "Переведи 490₽ на карту 4893 4704 9814 3038\n"
        "Получатель: Остренко Юрий Борисович\n\n"
        "✅ После оплаты — напиши /paid\n"
        "🤝 Хочешь стать партнёром? Жми /partner"
    )

async def paid(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✅ Оплата получена!\n"
        "Вот твои шаблоны и бонус: [тут можешь вставить ссылку или текст]"
    )

async def partner(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤝 Партнёрка:\n"
        "Рассказывай друзьям о боте и получай 50% с каждой продажи!\n"
        "Твоя реферальная ссылка: https://t.me/aiwriterkit_bot\n\n"
        "Для учёта напиши мне в ЛС с чек-листом!"
    )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("paid", paid))
app.add_handler(CommandHandler("partner", partner))

print("Бот запущен! Жми Ctrl+C для остановки.")
app.run_polling()
