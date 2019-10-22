import logging
import pyffx

from .util import generate_token_bytes

logger = logging.getLogger(__name__)

# Pseudonymize data in a CSV file

class Pseudonymizer():
    
    def __init__(self, secret_key_hex = ''):
        logging.info('Init Pseudonymizer')
        if secret_key_hex:
            self.secret_key_bytes = bytes.fromhex(secret_key_hex)
            logging.debug('Use secret key received: {}'.format(secret_key_hex))
        else:
            self.secret_key_bytes = generate_token_bytes(16)
            logging.debug('Generated secret key: {}'.format(self.secret_key_bytes))

# Local:
# In: CSV row (a list)
# Out: updates CSV row (a list)

    def update_row(self, column_num, column_type, row):
        if column_type == 'num':
            logging.debug('Pseudonymize {}'.format(row[column_num-1]))
            encrypter = pyffx.Integer(self.secret_key_bytes, len(row[column_num-1]))
            row[column_num-1] = encrypter.encrypt(row[column_num-1])
        return row
   
# Run job:
#  specify file info:
#  column_num, column_type, header_present=False,
# column_num starts with 1 (first column)
#  column type can be: num, asc, (email, full name etc. maybe not implement)
#  In and out files
    def run_job(self, infile, outfile, column_num=1, column_type='num', header_present=False):
        return