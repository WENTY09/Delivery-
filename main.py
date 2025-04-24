import sys
from app import create_app
from telegram_bot.bot import start_bot

app = create_app()

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "bot":
        start_bot()
    else:
        # Web service entry point
        app.run(host="0.0.0.0", port=5000)
