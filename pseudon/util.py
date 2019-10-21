import secrets
import csv
import random

def generate_token_bytes(nbytes = 16):
    return secrets.token_bytes(nbytes)
    
def generate_token_hex(nbytes = 16):
    return secrets.token_hex(nbytes)

def generate_token_urlsafe(nbytes = 16):
    return secrets.token_urlsafe(nbytes)

def generate_random_ascii(length = 10):
    #letters = string.ascii_lowercase
    letters = 'abcdefghijklmnoprstuv'
    # using list comprehension: 
    return ( ''.join(random.choice(letters) for i in range(length)))

    
# Generate test data: 
# CSV file with columns: full name, email, phone
# phone unique

def gen_test_data(filename, rows=100, header=False):
    phonelist = random.sample(range(100000000,999999999), rows)
    with open (filename, 'w', newline='') as outfile:
        csv_file_writer = csv.writer(outfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        if header:
            csv_file_writer.writerow(['Full name', 'Email', 'Phone'])
        for phone in phonelist:
            firstname = generate_random_ascii(random.randint(3,5))
            lastname = generate_random_ascii(random.randint(5,8))
            
            csv_file_writer.writerow([firstname.capitalize() + \
                ' ' + lastname.capitalize(), lastname + '@example.com', '0' + str(phone)])


