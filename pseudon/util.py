
# create new key from key + tweak (salt)

import secrets

def generate_token_bytes(nbytes = 16):
    return secrets.token_bytes(nbytes)
    
def generate_token_hex(nbytes = 16):
    return secrets.token_hex(nbytes)

def generate_token_urlsafe(nbytes = 16):
    return secrets.token_urlsafe(nbytes)
