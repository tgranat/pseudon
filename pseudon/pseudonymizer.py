import logging

from .util import generate_token_urlsafe

logger = logging.getLogger(__name__)

# Pseudonymize data in a CSV file

class Pseudonymizer():
    logging.info('Create Pseudonymizer')
    
    #secret_key_base64 = ''
    
    def __init__(self, secret_key_base64 = ''):
        if secret_key_base64:
            self.secret_key_base64 = secret_key_base64
        else:
            self.secret_key_base64 = generate_token_urlsafe(16)
            

    def get_secret_key(self):
        return self.secret_key_base64
# Local:
# In: CSV row (a list)
# Out: updates CSV row (a list)

    def update_row(self, row):
        return
   
# Run job:
#  specify file info:
#  column_num, column_type, header_present=False,
#  column type can be: num, asc, (email, full name etc. maybe not implement)
#  In and out files
    def run_job(self, infile, outfile, column_num=1, column_type='num', header_present=False):
        return