import telebot
from dotenv import load_dotenv
import os
from odoo_connection import Connection

load_dotenv()

def set_connection():
    connection = Connection()
    connection.start()
    return connection

bot = telebot.TeleBot(os.environ.get("TELEGRAM_API_TOKEN"))
@bot.message_handler(commands=["start"])
def start(msg):
    bot.reply_to(msg, "Hi")

@bot.message_handler(commands=["products"])
def products(msg):
    connection = set_connection()
    bot.reply_to(msg, f"{connection.list_products()}")

@bot.message_handler(commands=["product"])
def product(msg):
    connection = set_connection()
    product_id = msg.text.replace("/product ", "")
    bot.reply_to(msg, f"{connection.product_details(product_id)}")


bot.polling(timeout=120) 