from .Database import Database
import config

# List of databases (you can create your own here!)
access_db = Database(config.ACCESS_DB_PATH)
# my_db = Database("database.db")