from dotenv import load_dotenv 
from secrets import token_bytes
from os import getenv

load_dotenv()

APP_KEY = getenv("DEV_APP_KEY") or token_bytes(24)
ENABLE_TOKEN = True if getenv("ENABLE_TOKEN").lower() == "true" else False
ACCESS_DB_PATH = getenv("ACCESS_DB_PATH")
SETUP_REQUIRED = True 

# Write your environment variables here!