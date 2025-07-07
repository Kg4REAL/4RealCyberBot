from flask import Flask, render_template, jsonify, request
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "data"))

app = Flask(__name__)

# Charger les questions en mémoire (pour simplifier)
with open(os.path.join(DATA_DIR, "questions.json"), encoding="utf-8") as f:
    QUESTIONS = json.load(f)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/lexique")
def lexique():
    with open(os.path.join(DATA_DIR, "lexique.json"), encoding="utf-8") as f:
        lexique = json.load(f)
    return render_template("lexique.html", lexique=lexique)

@app.route("/quiz")
def quiz():
    return render_template("quiz_interactif.html")

@app.route("/api/questions")
def api_questions():
    # renvoyer la liste des questions en JSON
    return jsonify(QUESTIONS)

if __name__ == "__main__":
    app.run(debug=True)
