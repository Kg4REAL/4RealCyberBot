from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
)
from handlers.quiz import quiz_handler, answer_handlers
from handlers.lexique import lexique_handler
from handlers.roadmap import roadmap_handler
from handlers.mission import mission_handler
from handlers.admin import admin_handler
from handlers.help import help_handler

import os
from dotenv import load_dotenv

# Charger les variables d'environnement (.env)
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

def main():
    # Créer l'application Telegram avec le token
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    # 🔹 Commandes du bot
    app.add_handler(CommandHandler("start", help_handler))
    app.add_handler(CommandHandler("help", help_handler))
    app.add_handler(CommandHandler("quiz", quiz_handler))
    app.add_handler(CommandHandler("lexique", lexique_handler))
    app.add_handler(CommandHandler("roadmap", roadmap_handler))
    app.add_handler(CommandHandler("mission", mission_handler))
    app.add_handler(CommandHandler("admin", admin_handler))

    # 🔹 Gérer les réponses du quiz (1, 2, 3, 4)
    for handler in answer_handlers:
        app.add_handler(handler)

    # Démarrer le bot
    print("✅ Bot lancé avec succès. Attente des commandes...")
    app.run_polling()

if __name__ == "__main__":
    main()
