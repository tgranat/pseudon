import sys
import getopt
import logging

from pseudon.util import gen_test_data 

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)-15s %(levelname)-5s %(module)s.%(funcName)s() %(message)s')

def main():
    print("main() in __main__.py %s", __name__)
    
    UNIXOPTS = 'hg:r:'
    GNUOPTS = ['help', 'gen_test_data=', 'rows=']
    HELP = '[-g file -r rows -h]' +\
    '\n-g file\tGenerate test data file' +\
    '\n-r rows\tNumber of rows in test data file' +\
    '\n-h\tHelp'
            
    argv = sys.argv[1:]
    gen_data_file = ''
    gen_data_file_rows = 0
    try:
        opts, args = getopt.getopt(argv, UNIXOPTS, GNUOPTS)
        print(opts)
        print(args)
        for opt, value in opts:
            if opt in ('-h', '--help'):
                print('usage: %s' % sys.argv[0], HELP)
            if opt in ('-g', '--gen_test_data'):
                gen_data_file = value
            if opt in ('-r', 'rows'):
                gen_data_file_rows = int(value)
                
                
    except (getopt.GetoptError, ValueError) as err:
        print(err)  
        print('usage: %s' % sys.argv[0], HELP)     
        sys.exit(2)

# Generate test data file

    if gen_data_file:
        if gen_data_file_rows <= 0:
            gen_test_data(gen_data_file)
        else:
            gen_test_data(gen_data_file, gen_data_file_rows)


if __name__ == "__main__":
    main()