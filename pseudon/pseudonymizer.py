# Simple tool to pseudonymize data in specified column in CSV file
# 
# This version handles one column at a time.  
#
# Will probably need some tweaking to suit your needs

import logging
import string
import pyffx
import csv

from .util import generate_token_bytes

logger = logging.getLogger(__name__)

NOT_ALLOWED_CHARS=',"'

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
# Throws ValueError and perhaps other exceptions
    
    def _update_row(self, column_num, column_type, row, not_allowed_chars=NOT_ALLOWED_CHARS):
        logging.debug('Pseudonymize {}'.format(row[column_num-1]))
        if column_type == 'num':
            encrypter = pyffx.Integer(self.secret_key_bytes, len(row[column_num-1]))
            row[column_num-1] = encrypter.encrypt(row[column_num-1])
        elif column_type == 'asc':
            # Using string.printable to specify valid alphabet. Remove any not allowed characters (for example delimiter char)
            alphabetstring = string.printable
            alphabetstring = alphabetstring.translate(str.maketrans(dict.fromkeys(not_allowed_chars))) 
            encrypter = pyffx.String(self.secret_key_bytes, alphabet = alphabetstring, length = len(row[column_num-1]))
            row[column_num-1] = encrypter.encrypt(row[column_num-1])
        return row
   
# Run job:
#  
# column_num starts with 1 (first column)
# column type can be: num, asc (ascii characters with som limitations)
# TODO: "name": 1) make lower case 2) encrypt using string.ascii_lowercase 3) capitalize first letter
#       "fullname": 1) lower case 2) split on space 3) encrypt each name 4) capitalize first letter(s)
#       "email": 1) lower case 2) split on @ 3) split on '.', '_', '-' (there are other cases) 4) encrypt each 5)join together again
#       Not possible to make it cover all cases. Need to add code to cover special cases when necessary
# In and out files
    def run_job(self, infilename, outfilename, column_num=1, column_type='num', header_present=False, usedelimiter=','):
        logging.info('Pseudonymize column {:d} (type: {}) from file: {}, write to file: {}'.format(column_num, column_type, infilename, outfilename))
        with open (outfilename, 'w', newline='') as outfile:
            csv_file_writer = csv.writer(outfile, delimiter=usedelimiter, quotechar='"', quoting=csv.QUOTE_MINIMAL)
            with open (infilename, 'r') as infile:
                csv_reader = csv.reader(infile, delimiter=usedelimiter)
                line_count = 0
                for row in csv_reader:             
                    if header_present and line_count == 0:
                        csv_file_writer.writerow(row)
                    else:
                        csv_file_writer.writerow(self._update_row(column_num, column_type, row))
                    line_count += 1
        logging.info('Done. {:d} lines processed'.format(line_count))
        return