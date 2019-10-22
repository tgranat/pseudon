from pseudon.pseudonymizer import Pseudonymizer

def test_create_pseudonymizer():
    p = Pseudonymizer('qwerty')
    assert(p.get_secret_key == 'qwerty')
    
