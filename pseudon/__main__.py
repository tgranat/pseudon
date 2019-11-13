# Simple tool to pseudonymize data in specified column in CSV file
# 
# This version handles one column at a time.  
#
# Will probably need some tweaking to suit your needs

# TODO: test out using 'click' to create CLI

import sys
import getopt
import logging
from pathlib import Path

from pseudon.util import gen_test_data 
from pseudon.pseudonymizer import Pseudonymizer

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)-15s %(levelname)-5s %(module)s.%(funcName)s() %(message)s')

COLTYPES = ['num', 'asc']
UNIXOPTS = 'hi:o:c:t:d:g:q:'
GNUOPTS = ['help', 'infile=', 'outfile=', 'colnum=', 'coltype=', 'header', 'delimiter=', 'gen_test_data=', 'rows=']
    
HELP = '-i infile -o outfile -c column_num -t column_type [-r -d delimiter_char]' +\
    '\n-i infile\tMandatory' +\
    '\n-o outfile\tMandatory' +\
    '\n-c colnum\tColumn number, first column = 1. Mandatory' +\
    '\n-t coltype\tColumn type: num, asc. Mandatory' +\
    '\n-r\t\tFirst row in file is a header (default: no header)'  +\
    '\n-d delimiter\tDelimiter between columns (default is comma: \',\')' +\
    '\n-h\t\tHelp'

def main():
    logging.debug( __name__)
    
    # for test you can use this to create a test data file: -g test_data_file -q rows -h)
    #' -g file   Generate test data file
    #' -r rows   Number of rows in test data file
    
    argv = sys.argv[1:]
    gen_data_file = ''
    gen_data_file_rows = 0
    
    infile = ''
    outfile = ''
    colnum = 0
    coltype = ''
    header = False
    delimiter = ','
    
    try:
        opts, args = getopt.getopt(argv, UNIXOPTS, GNUOPTS)
        logging.debug('Opts: %s', opts)
        logging.debug('Args: %s', args)
        for opt, value in opts:
            if opt in ('-h', '--help'):
                print('usage: %s' % sys.argv[0], HELP)
                sys.exit(0)
            if opt in ('-i', '--infile'):
                infile = value
            if opt in ('-o', '--outfile'):
                outfile = value
            if opt in ('-c', '--colnum'):
                colnum = int(value)
            if opt in ('-t', '--coltype'):
                coltype = value
            if opt in ('-r', '--header'):
                header = True
            if opt in ('-d', '--delimiter'):
                delimiter = value
            if opt in ('-g', '--gen_test_data'):
                gen_data_file = value
            if opt in ('-q', 'rows'):
                gen_data_file_rows = int(value)
                
            
    except (getopt.GetoptError, ValueError) as err:
        print(err)  
        _print_usage()
        sys.exit(2)
        
    # Gen test data
    if gen_data_file:
        if Path(gen_data_file).exists():
            print('File {} already exists. Nothing done.'.format(outfile))
            sys.exit(1)

        if gen_data_file_rows <= 0:
            gen_test_data(gen_data_file)
        else:
            gen_test_data(gen_data_file, gen_data_file_rows)
        sys.exit(0)
    
    # Validate input
    if not infile or not outfile or not colnum or not coltype:
        print('Mandatory parameter(s) missing.')
        _print_usage()
        sys.exit(2)
        
    if not coltype in (COLTYPES):
        print('Only following column types allowed: {}'.format(COLTYPES))
        
    if not Path(infile).is_file():
        print('Infile {} does not exist'.format(infile))
        sys.exit(1)
        
    if Path(outfile).exists():
        print('Outfile {} already exists'.format(outfile))
        sys.exit(1)
    
    # Run stuff
    p = Pseudonymizer()
    p.run_job(infile, outfile, colnum, coltype, header, delimiter)
    
   

def _print_usage():
    print('usage: %s' % sys.argv[0], HELP)  
    
if __name__ == "__main__":
    main()