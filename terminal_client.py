#!/usr/bin/env python3
"""
Terminal Client for Django ChatterBot Application.
Assignment: College Terminal Chat Client using Django and ChatterBot.

Usage:
    python terminal_client.py
    (or via virtual environment: python3 terminal_client.py)
"""

import os
import sys

# Configure Django environment settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatterbot_project.settings')

try:
    import django
    django.setup()
except Exception as e:
    print(f"Error setting up Django environment: {e}")
    sys.exit(1)

from chatbot_app.bot import get_chatbot, train_bot


def main():
    """
    Main interactive terminal chat loop.
    Implements standard user: / bot: format as specified in assignment requirements.
    """
    print("=" * 60)
    print("        WELCOME TO DJANGO CHATTERBOT TERMINAL CLIENT        ")
    print("=" * 60)
    print("Initializing conversational engine & loading training data...")

    # Initialize bot instance
    bot = get_chatbot("CollegeTerminalBot")

    # Automatically train bot on start
    train_bot(bot)

    print("\nChatbot is ready! Type 'exit', 'quit', or 'bye' to end the session.")
    print("-" * 60)

    # Interactive Loop
    while True:
        try:
            # Prompt user input with format 'user: '
            user_input = input("user: ").strip()

            # Check for empty input
            if not user_input:
                continue

            # Exit condition check
            if user_input.lower() in ['exit', 'quit', 'bye']:
                print("bot: Goodbye! It was nice chatting with you.")
                print("-" * 60)
                break

            # Generate response from ChatterBot engine
            response = bot.get_response(user_input)

            # Display response with format 'bot: '
            print(f"bot: {response}")

        except (KeyboardInterrupt, EOFError):
            print("\nbot: Chat session terminated by user. Goodbye!")
            print("-" * 60)
            break
        except Exception as err:
            print(f"bot: An error occurred: {err}")


if __name__ == '__main__':
    main()
