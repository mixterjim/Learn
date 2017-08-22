import logging
logging.basicConfig(level=logging.INFO)
# Output INFO(debug，info，warning，error)
import pdb


def foo(s):
    n = int(s)
    print('>>> n = %d' % n)
    assert n != 0, 'n is zero!'
    # python -O "27 Debug.py"
    # Stop assert
    logging.info('n = %d' % n)
    # Commented assert
    return 10 / n


def main():
    foo('0')
pdb.set_trace()  # will stop here,use 'c' to continue
main()
# python -m pdb "27 Debug.py"
# Debug with pdb
# input '1' to see code
# input 'n' to run next line code
# input 'p function' to see the funciton
# input 'q' to exit
