import sys
import os
import argparse


def check_integer(N):
    """
    Check the passed value
    Argument
    --------
        N: integer
    Return
    --------
        True: if it is integer
        False: no integer
    """
    try:
        N = int(N)
        if N <= 0:
            raise ValueError('Integer is negative')
        else:
            return True
    except ValueError:
        print('N is not integer')
        return False


def h_ascii(key, N):
    """ ASCII hash function
    Arguments
    --------
        key: string key
        N: hash table size
    Return
    --------
        hash: based on the sum of the ASCII \n
              values for the characters in key
    """
    s = 0
    for i in range(len(key)):
        s += ord(key[i])
    return s % N


def h_rolling(key, N, p=53, m=2**64):
    """ Polynomial rolling hash function
    Arguments
    --------
        key: string key
        N: hash table size
    Return
    --------
        hash: based on the polynomial rolling \n
              returns hash
    """
    s = 0
    for i in range(len(key)):
        s += ord(key[i]) * p**i
    s = s % m
    return s % N


def h_python(key, N):
    """ Python builtin hash function
    Arguments
    --------
        key: string key
        N: hash table size
    Return
    --------
        Hash value
    """
    return hash(key) % N


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Hash function',
                                     prog='hash_functions')
    parser.add_argument('--input', type=str, help='input filename',
                        required=True)
    parser.add_argument('--hash_method', type=str, help='function name',
                        required=True)
    parser.add_argument('--hash_table_size', type=int, help='hash table size',
                        required=True)

    args = parser.parse_args()

    if check_integer(args.hash_table_size) is not True:
        print('Not integer')
        sys.exit(1)

    if (os.path.exists(args.input)):
        for l in open(args.input):
            if (args.hash_method == 'ascii'):
                print(h_ascii(l, args.hash_table_size))
            elif (args.hash_method == 'rolling'):
                print(h_rolling(l, args.hash_table_size))
            elif (args.hash_method == 'h_python'):
                print(h_python(l, args.hash_table_size))
            else:
                print('Hash function not found')
                sys.exit(1)
    else:
        print('Input file not found')
        sys.exit(1)
