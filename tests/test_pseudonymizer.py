from pseudon.pseudonymizer import Pseudonymizer
from pseudon.util import generate_token_hex

#import pyffx

def test_create_pseudonymizer():
    h = generate_token_hex(4)
    q = Pseudonymizer(h)
    assert(q.secret_key_bytes.hex() == h)
    
    
def test_update_row_num():
    p = Pseudonymizer()
    row = ['abcde', '12345678', 'cdefg']
    result_row = p.update_row(2, 'num', row)
    assert(result_row[0] == 'abcde')
    assert(result_row[1] != '123455678')
    assert(result_row[2] == 'cdefg')
    
#def test_pyffx():
#    p = Pseudonymizer()
#    e = pyffx.Integer(p.secret_key_bytes, 4)
#    print('encrypted: {:d}'.format(e.encrypt('1234')))