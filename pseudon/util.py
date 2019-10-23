import secrets
import csv
import random
import logging
import string

logger = logging.getLogger(__name__)


# Return byte string containing nbytes number of bytes.
def generate_token_bytes(nbytes = 16):
    return secrets.token_bytes(nbytes)
# Return a random text string, in hexadecimal. The string has nbytes random bytes, 
# each byte converted to two hex digits. 
def generate_token_hex(nbytes = 16):
    return secrets.token_hex(nbytes)
# Return a random URL-safe text string, containing nbytes random bytes.
# The text is Base64 encoded, so on average each byte results in approximately 1.3 characters. 
def generate_token_urlsafe(nbytes = 16):
    return secrets.token_urlsafe(nbytes)

# Generate lower case ascii strings without a few consonants (z, q etc.)
def generate_random_limited_ascii(length = 10):
    #letters = string.ascii_lowercase
    letters = 'abcdefghijklmnoprstuv'
    # using list comprehension: 
    return ( ''.join(random.choice(letters) for i in range(length)))

# Generate random printable character text string (see string.printable)
def generate_random_printable(length = 10):
    return ( ''.join(random.choice(string.printable) for i in range(length)))

# Generate limited random printable character text string, for test purposes 
def generate_random_limited_printable(length = 10):
    chars = string.ascii_letters + string.digits + ' ' + '!@#$%&()=?+[]{}*;:.'
    return ( ''.join(random.choice(chars) for i in range(length)))
       
# Generate test data: 
# CSV file with columns: full name, email, phone
# phone unique

def gen_test_data(filename, rows=10, header=False, usedelimiter=','):
    # Filename can be a text string or LocalPath or maybe something else
    logging.info('Generate %s rows of testdata in file: ' + str(filename), rows)
    phonelist = random.sample(range(100000000,999999999), rows)
    with open (filename, 'w', newline='') as outfile:
        csv_file_writer = csv.writer(outfile, delimiter=usedelimiter, quotechar='"', quoting=csv.QUOTE_MINIMAL)
        if header:
            csv_file_writer.writerow(['Full name', 'Email', 'Phone', 'Random'])
        for phone in phonelist:
            firstname = generate_random_limited_ascii(random.randint(3,5))
            lastname = generate_random_limited_ascii(random.randint(5,8))
            
            csv_file_writer.writerow([firstname.capitalize() + ' ' + lastname.capitalize(),
                lastname + '@example.com', '0' + str(phone),
                generate_random_limited_printable(15)])


