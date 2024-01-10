import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6885232721:AAGkYm_7SW1IUdwJYTJ8eZwC4PX39rU3_uk")
    API_ID = int(os.environ.get("API_ID", "22231458"))
    API_HASH = os.environ.get("API_HASH", "ad92f01e4a90cddebbea0ad16fa23026")
    DB_URL = os.environ.get("DATABASE_URL", "mongodb+srv://jnanesh:jnanesh@cluster0.8pzxa6s.mongodb.net/?retryWrites=true&w=majority")
