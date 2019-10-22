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
            

# Local:
# In: CSV row (a list)
# Out: updates CSV row (a list)

    def update_row(self):
        print('Key = ' + self.secret_key_base64)
   
# Run job:
#  specify file info:
#  column_num, column_type, header_present=False,
#  In and out files