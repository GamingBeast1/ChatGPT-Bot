import re
from os import getenv, environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

API_ID = int(environ.get("API_ID", "25705219"))
API_HASH = environ.get("API_HASH", "6590905e28c61bca1ad5e83de9853cf8")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002082396915"))
ADMINS = int(environ.get("ADMINS", "5022283560"))
DB_URI = environ.get("DB_URI", "mongodb+srv://CHATGPTBOT:CHATGPTBOT@cluster0.zasqjzy.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = environ.get("DB_NAME", "Galaxychatgptbot")
OPENAI_API = environ.get("OPENAI_API", "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")
AI = is_enabled((environ.get("AI","True")), False)
