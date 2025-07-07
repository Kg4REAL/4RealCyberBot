# 🤖 4RealCyberBot

Un bot Telegram + interface web pour apprendre la cybersécurité de manière interactive.  
Développé par **@Kg4reall** – powered by Python 💻

---

## 📚 Fonctionnalités

### 🔸 Côté Bot Telegram :
- `/start` ou `/help` → Bienvenue + aide
- `/quiz` → Lance un quiz interactif (score à la fin)
- `/lexique vpn` → Cherche un mot dans le lexique cybersécurité
- `/roadmap` → Feuille de route d’apprentissage
- `/mission` → Mini défi à réaliser
- `/admin add mot:definition` → Ajouter un mot (admin only)
- `/admin del mot` → Supprimer un mot (admin only)

### 🔸 Côté Web (Flask) :
- **Lexique** accessible dans un design propre
- **Quiz interactif** : joue, réponds et obtiens ton score final
- Page d’accueil simple et moderne

---

## 🛠️ Installation rapide

### 1. Cloner le projet
```bash
git clone https://github.com/kg4real/4RealCyberBot.git
cd 4RealCyberBot/telegram_bot
2. Créer l'environnement Python

python3 -m venv env
source env/bin/activate
3. Installer les dépendances

pip install -r requirements.txt
4. Configurer le fichier .env
Crée un fichier .env à la racine :


TELEGRAM_TOKEN=your_telegram_bot_token
▶️ Lancer le Bot Telegram

python bot.py
🌐 Lancer l’interface Web (Flask)

cd webapp
python app.py
Ensuite va sur http://localhost:5000

📁 Structure du projet

telegram_bot/
├── bot.py                  # Fichier principal du bot Telegram
├── data/                   # Données du projet
│   ├── lexique.json        # Définitions de cybersécurité
│   ├── questions.json      # Questions du quiz
│   ├── roadmap.txt         # Feuille de route
│   └── scores.json         # Pour le classement futur
├── env/                    # Environnement virtuel Python
├── handlers/               # Tous les handlers du bot
│   ├── quiz.py             # Logique du quiz
│   ├── lexique.py          # Commande /lexique
│   ├── mission.py          # Commande /mission
│   ├── roadmap.py          # Commande /roadmap
│   ├── admin.py            # Ajout/Suppression lexique
│   └── help.py             # Message d’aide
├── utils/
│   └── loader.py           # Fonctions de chargement JSON
├── webapp/
│   ├── app.py              # Serveur Flask
│   └── templates/
│       ├── home.html
│       ├── lexique.html
│       └── quiz_interactif.html
├── README.md               # Ce fichier
└── requirements.txt        # Liste des dépendances

##💡Améliorations possibles
🎯 Ajouter un système de classement (/top)

🎮 Quiz avec boutons (inline keyboard)

📲 PWA : transformer en appli mobile

🛡️ Protection admin avancée

##👤Auteur
Hālįl Kg
t.me/Kg4reall
Passionné de cybersécurité et IA 🤖⚔️

##🏁Licence
Code open-source – libre d’utilisation à but éducatif.

##⭐Donne de la force
Si tu aimes le projet, pense à mettre une étoile sur GitHub 🌟


