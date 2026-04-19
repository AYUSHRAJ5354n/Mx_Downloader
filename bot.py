import asyncio
import threading
from flask import Flask
from hydrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
import os

# ------------------ BOT ------------------
app = Client(
    "dsrbotz_mx_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    workers=999,  # ⚠️ reduce from 999 (too high, can crash VPS/Koyeb)
    plugins=dict(root="plugins"),
)

# ------------------ WEB SERVER ------------------
web_app = Flask(__name__)

@web_app.route("/")
def home():
    return "Bot is running ✅"

def run_web():
    port = int(os.environ.get("PORT", 8000))
    web_app.run(host="0.0.0.0", port=port)

# ------------------ MAIN ------------------
if __name__ == "__main__":
    print("🚀 DsrBotz MX Player Bot Starting...")

    # Run Flask in separate thread
    t = threading.Thread(target=run_web)
    t.start()

    # Run Telegram bot
    app.run()
