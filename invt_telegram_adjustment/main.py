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
    bot.reply_to(
        msg,
        f"""
        Commands:
        /start - Start the bot
        /products - List of all product
        /product + product ID - Show product information
        /adj + product ID + Actual Quantity - Inventory adjustment
        """,
    )


@bot.message_handler(commands=["products"])
def products(msg):
    connection = set_connection()
    bot.reply_to(msg, connection.list_products(), parse_mode="Markdown")


@bot.message_handler(commands=["product"])
def product(msg):
    connection = set_connection()
    product_id = msg.text.replace("/product ", "")
    bot.send_photo(msg.chat.id, connection.get_image(product_id))
    bot.reply_to(msg, connection.product_details(product_id))


@bot.message_handler(commands=["adj"])
def product(msg):
    connection = set_connection()
    product_id = msg.text.replace("/adj ", "")
    bot.reply_to(msg, connection.adjust_inventory(product_id))


bot.polling(timeout=120)
