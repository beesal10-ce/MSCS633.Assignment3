"""
Unit tests for Chatbot App.
Tests ChatBot instance setup, training pipeline, and dialog generation.
"""

from django.test import TestCase
from chatbot_app.bot import get_chatbot, train_bot

class ChatBotTestCase(TestCase):
    def setUp(self):
        """Set up test ChatBot instance and train it."""
        self.bot = get_chatbot("TestBot")
        train_bot(self.bot)

    def test_chatbot_initialization(self):
        """Verify chatbot instance is created with correct name."""
        self.assertIsNotNone(self.bot)
        self.assertEqual(self.bot.name, "TestBot")

    def test_sample_dialog_response_1(self):
        """Test response to 'Good morning! How are you doing?'"""
        response = self.bot.get_response("Good morning! How are you doing?")
        self.assertIsNotNone(response)
        self.assertTrue(len(str(response)) > 0)

    def test_sample_dialog_response_2(self):
        """Test response to 'You're welcome.' yields 'Do you like hats?' or valid reply."""
        response = self.bot.get_response("You're welcome.")
        self.assertIsNotNone(response)
        self.assertIn("hats", str(response).lower())
