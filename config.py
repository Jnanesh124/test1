import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6008504043:AAHtEwk0fbPZF2dXfYkuXh5y6PPt-9jlwXU")
    API_ID = int(os.environ.get("API_ID", "11615722")
    API_HASH = os.environ.get("API_HASH", "c992746520e8886d3330de2ec9a1a3a7")
    DB_URL = os.environ.get("DATABASE_URL", "mongodb+srv://auto:auto@cluster0.xikol9h.mongodb.net/?retryWrites=true&w=majority")
