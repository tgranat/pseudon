from pseudon.pseudonymizer import Pseudonymizer

def test_create_pseudonymizer():
    p = Pseudonymizer('fesf')
    p.update_row()
