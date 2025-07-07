from telegram import Update
from telegram.ext import ContextTypes
from utils.loader import load_json
import json, os

LEXIQUE_PATH = os.path.join(os.path.dirname(__file__), "../data/lexique.json")

ADMIN_ID = 5064295982  # Ton ID

async def admin_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id != ADMIN_ID:
        await update.message.reply_text("🚫 Accès refusé.")
        return

    args = context.args
    if not args or args[0] not in ("add", "del"):
        await update.message.reply_text("⚙️ Utilisation : /admin add mot:definition  |  /admin del mot")
        return

    mode = args[0]
    content = ' '.join(args[1:])

    lexique = load_json("lexique.json")

    if mode == "add":
        if ":" not in content:
            await update.message.reply_text("❌ Format attendu : mot:definition")
            return
        mot, definition = map(str.strip, content.split(":", 1))
        lexique[mot.lower()] = definition
        with open(LEXIQUE_PATH, "w", encoding="utf-8") as f:
            json.dump(lexique, f, ensure_ascii=False, indent=2)
        await update.message.reply_text(f"✅ Mot '{mot}' ajouté.")

    elif mode == "del":
        mot = content.strip().lower()
        if mot in lexique:
            del lexique[mot]
            with open(LEXIQUE_PATH, "w", encoding="utf-8") as f:
                json.dump(lexique, f, ensure_ascii=False, indent=2)
            await update.message.reply_text(f"🗑️ Mot '{mot}' supprimé.")
        else:
            await update.message.reply_text("❌ Mot introuvable.")
