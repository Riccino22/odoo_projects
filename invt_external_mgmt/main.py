import telebot
from dotenv import load_dotenv
import os

load_dotenv()

bot = telebot.TeleBot(os.environ.get("TELEGRAM_API_TOKEN"))
@bot.message_handler(commands=["start"])
def start(msg):
    bot.reply_to(msg, f"Hola")
    
bot.polling(timeout=120) 