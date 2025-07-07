from telegram import Update
from telegram.ext import ContextTypes

async def help_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = (
        "👋 *Bienvenue sur 4RealCyberBot !*\n\n"
        "Voici les commandes disponibles :\n"
        "🔹 /quiz – Démarrer un quiz interactif\n"
        "🔹 /lexique [mot] – Rechercher un terme cybersécurité\n"
        "🔹 /roadmap – Voir la feuille de route\n"
        "🔹 /mission – Voir ta mission du jour\n"
        "🔹 /admin – (Admin) Modifier quiz/lexique\n"
    )
    await update.message.reply_text(msg, parse_mode="Markdown")
