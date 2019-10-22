from pseudon.pseudonymizer import Pseudonymizer
from pseudon.util import generate_token_hex, gen_test_data
from _pytest.tmpdir import tmpdir

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
    assert(result_row[1] != '12345678')
    assert(result_row[2] == 'cdefg')

def test_update_row_asc():
    p = Pseudonymizer()
    row = ['abcde', '12345678', 'cdefGHIJ%& -.!']
    result_row = p.update_row(3, 'asc', row)
    assert(result_row[0] == 'abcde')
    assert(result_row[1] == '12345678')
    assert(result_row[2] != 'cdefGHIJ%& -.!')
    
def test_run_job(tmpdir):
        origdatafile = tmpdir.join("origdata.csv")
        gen_test_data(origdatafile, 5)
        resultdatafile = tmpdir.join("resultdata.csv")
        p = Pseudonymizer()
        p.run_job(origdatafile, resultdatafile, 2, 'num', False)
 
        x = 0
        with open (resultdatafile, 'r') as f:
            for line in f:
                print(line)
                x += 1
        assert(x == 5)

    
    
    
#def test_pyffx():
#    p = Pseudonymizer()
#    e = pyffx.Integer(p.secret_key_bytes, 4)
#    print('encrypted: {:d}'.format(e.encrypt('1234')))