import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6885232721:AAGkYm_7SW1IUdwJYTJ8eZwC4PX39rU3_uk")
    API_ID = int(os.environ.get("API_ID", "20846870"))
    API_HASH = os.environ.get("API_HASH", "a864594cb1752ff03948066e529fcf0a")
    DB_URL = os.environ.get("DATABASE_URL", "mongodb+srv://jnanesh:jnanesh@cluster0.8pzxa6s.mongodb.net/?retryWrites=true&w=majority")
