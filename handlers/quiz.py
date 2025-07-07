import json
import random
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler, MessageHandler, filters

with open("data/questions.json", encoding="utf-8") as f:
    QUESTIONS = json.load(f)

NB_QUESTIONS = 5  # Nombre de questions par partie

async def quiz_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    selected = random.sample(QUESTIONS, min(NB_QUESTIONS, len(QUESTIONS)))
    context.user_data["quiz"] = {
        "questions": selected,
        "current": 0,
        "score": 0
    }
    await send_next_question(update, context)

async def send_next_question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    quiz = context.user_data.get("quiz")

    if quiz["current"] >= len(quiz["questions"]):
        score = quiz["score"]
        total = len(quiz["questions"])
        del context.user_data["quiz"]
        await update.message.reply_text(
            f"🏁 Quiz terminé !\nTu as obtenu {score}/{total} bonnes réponses. 🎯"
        )
        return

    q = quiz["questions"][quiz["current"]]
    msg = f"🧠 Question {quiz['current'] + 1} :\n\n{q['question']}\n"
    for i, choice in enumerate(q['choices'], 1):
        msg += f"{i}. {choice}\n"
    await update.message.reply_text(msg + "\nRéponds avec 1, 2, 3 ou 4.")

async def handle_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    quiz = context.user_data.get("quiz")
    if not quiz:
        return

    try:
        idx = int(update.message.text.strip()) - 1
    except:
        await update.message.reply_text("❌ Réponse invalide. Tape 1, 2, 3 ou 4.")
        return

    q = quiz["questions"][quiz["current"]]
    if idx < 0 or idx >= len(q["choices"]):
        await update.message.reply_text("❌ Réponse invalide. Tape 1, 2, 3 ou 4.")
        return

    selected = q["choices"][idx]
    correct = q["answer"]

    if selected == correct:
        await update.message.reply_text("✅ Bonne réponse !")
        quiz["score"] += 1
    else:
        await update.message.reply_text(f"❌ Mauvaise réponse. La bonne réponse était : *{correct}*", parse_mode="Markdown")

    quiz["current"] += 1
    await send_next_question(update, context)

quiz_handler = CommandHandler("quiz", quiz_handler)
answer_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, handle_answer)
answer_handlers = [answer_handler]
