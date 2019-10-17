from pseudon.util import generate_token_bytes, generate_token_hex, generate_token_urlsafe

def test_generate_token_bytes():
    bytes_token = generate_token_bytes()
    assert(type(bytes_token) == bytes)
    assert(len(bytes_token) == 16)
    
def test_generate_token_hex():
    length = 8
    hex_token = generate_token_hex(length)
    assert(type(hex_token) == str)
    assert(len(hex_token) == length*2)
    
def test_generate_token_urlsafe():
    urlsafe_token = generate_token_urlsafe(32)
    assert(type(urlsafe_token) == str)
    # can't test length since each byte results in approximately 1.3 characters
    # can decode and encode and compare perhaps
    
    