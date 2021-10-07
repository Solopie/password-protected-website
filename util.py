from secrets import token_bytes
from db import access_db
import hashlib

# ----- ACCESS HELPER FUNCTIONS -----
def generate_hash(content):
    salt = token_bytes(32)
    key = hashlib.pbkdf2_hmac('sha256', content.encode('utf-8'), salt, 100000)

    return (key,salt)

def verify_access(token):
    rows = access_db.query("SELECT token_hash,salt FROM tokens")

    for r in rows:
        curSalt = r["salt"]
        temp_key = hashlib.pbkdf2_hmac('sha256', token.encode('utf-8'), curSalt, 100000)
        if temp_key == r["token_hash"]:
            return True 
    
    return False
# ----- ---------------------- -----
