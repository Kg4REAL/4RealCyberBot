from telegram import Update
from telegram.ext import ContextTypes
import random

MISSIONS = [
    "Trouver toutes les failles sur le réseau local en 30 minutes !",
    "Analyser le trafic réseau avec Wireshark.",
    "Scanner un serveur cible avec Nmap et rapporter les ports ouverts.",
    "Créer une wordlist personnalisée pour bruteforce.",
    "Identifier les failles XSS dans une page web.",
]

async def mission_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mission = random.choice(MISSIONS)
    await update.message.reply_text(f"🎯 Ta mission : {mission}")
