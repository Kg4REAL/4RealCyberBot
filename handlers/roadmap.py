from telegram import Update
from telegram.ext import ContextTypes
from utils.loader import load_text

async def roadmap_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = load_text("roadmap.txt")
    await update.message.reply_text(f"🛣️ Feuille de route :\n{text}")
