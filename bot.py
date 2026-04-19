import threading
from flask import Flask
from hydrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
import os

# Telegram Bot
app = Client(
    "dsrbotz_mx_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    workers=50
)

# Dummy Web Server (for Koyeb)
web_app = Flask(__name__)

@web_app.route("/")
def home():
    return "OK"

def run_web():
    port = int(os.environ.get("PORT", 8000))
    web_app.run(host="0.0.0.0", port=port)

# Run both
if __name__ == "__main__":
    print("🚀 Bot Starting...")

    threading.Thread(target=run_web).start()
    app.run()
