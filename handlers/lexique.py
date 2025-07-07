from telegram import Update
from telegram.ext import ContextTypes
from utils.loader import load_json

LEXIQUE = load_json("lexique.json")

async def lexique_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    if not args:
        await update.message.reply_text("❓ Tape un mot à chercher. Exemple : `/lexique vpn`")
        return
    
    mot = ' '.join(args).lower().strip("?.,! ")
    definition = LEXIQUE.get(mot)
    
    if definition:
        await update.message.reply_text(f"📘 *{mot.title()}* : {definition}", parse_mode='Markdown')
    else:
        await update.message.reply_text("❌ Mot non trouvé dans le lexique.")
