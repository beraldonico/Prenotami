from telegram import Bot
import os
import asyncio

class TelegramBot():
    def __init__(self):
        self.bot = Bot(token=os.getenv("TELEGRAM_BOT_TOKEN"))
        self.chat_id = os.getenv("CHAT_ID")

    def send_message(self, text: str):
        asyncio.run(self.bot.send_message(text=text, chat_id=self.chat_id))
        
if __name__ == "__main__":
    from datetime import datetime

    bot = TelegramBot()
    bot.send_message(f"Teste as {datetime.now()}")
