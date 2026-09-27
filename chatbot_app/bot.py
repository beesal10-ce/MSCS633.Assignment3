"""
Chatbot Initialization and Training Service.
Integrates ChatterBot with Django environment to create a machine-learning based dialog engine.
"""

from pathlib import Path
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Define Base directory for SQLite database storage
BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "db.sqlite3"

def get_chatbot(name="CollegeChatBot"):
    """
    Instantiate and return a configured ChatBot instance.
    Uses SQLStorageAdapter to persist conversations in SQLite.
    """
    bot = ChatBot(
        name,
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        database_uri=f'sqlite:///{DB_PATH}',
        logic_adapters=[
            {
                'import_path': 'chatterbot.logic.BestMatch',
                'default_response': 'I am not sure I understand. Could you rephrase?',
                'maximum_similarity_threshold': 0.65
            },
            'chatterbot.logic.MathematicalEvaluation',
            'chatterbot.logic.TimeLogicAdapter'
        ],
        read_only=False
    )
    return bot

def train_bot(bot, force_retrain=False):
    """
    Train the ChatBot using ListTrainer for required conversational dialogs.
    """
    list_trainer = ListTrainer(bot)
    
    # 1. Primary assignment dialog sequence
    list_trainer.train([
        "Good morning! How are you doing?",
        "I am doing very well, thank you for asking.",
        "You're welcome.",
        "Do you like hats?"
    ])
    
    # 2. Common greeting pairs
    list_trainer.train(["hi", "Hello"])
    list_trainer.train(["hello", "Hi there!"])
    list_trainer.train(["how are you", "Good"])
