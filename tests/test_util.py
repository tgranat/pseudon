from pseudon.util import \
generate_token_bytes, \
generate_token_hex,\
generate_token_urlsafe,\
gen_test_data,\
generate_random_limited_ascii

class TestToken():
    def test_generate_token_bytes(self):
        bytes_token = generate_token_bytes()
        assert(type(bytes_token) == bytes)
        assert(len(bytes_token) == 16)
    
    def test_generate_token_hex(self):
        length = 8
        hex_token = generate_token_hex(length)
        assert(type(hex_token) == str)
        assert(len(hex_token) == length*2)
    
    def test_generate_token_urlsafe(self):
        urlsafe_token = generate_token_urlsafe(32)
        assert(type(urlsafe_token) == str)
        # can't test length since each byte results in approximately 1.3 characters
        # can decode and encode and compare perhaps
    
    
class TestTestData():
    def test_gen_data(self, tmpdir):
        rows  = 3
        outfile = tmpdir.mkdir("test_gen_data").join("testdata.csv")
        gen_test_data(outfile, rows)
        x = 0
        with open (outfile, 'r') as f:
            for line in f:
                print(line)
                x += 1
        assert(x == rows)
  
    def test_gen_data_header(self, tmpdir):
        rows = 3
        outfile = tmpdir.mkdir("test_gen_data").join("testdata1.csv")
        gen_test_data(outfile, rows, header=True, usedelimiter=';')
        x = 0
        with open (outfile, 'r') as f:
            for line in f:
                x += 1
        assert(x == rows + 1)      
        
    def test_gen_ascii(self):
        assert(len(generate_random_limited_ascii(7)) == 7)
        