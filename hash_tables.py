import sys
import hash_functions
import time
import random
import argparse
import os


def reservoir_sampling(new_val, size, V):
    """
    Create list V
    Arguments
    --------
        new_val: new value to add
        size: maximum length of list V
        V: list to change
    """
    if len(V) < size:
        V.append(new_val)
    else:
        j = random.randint(0, len(V))
        if j < len(V):
            V[j] = new_val


class LinearProbe:
    """
    A Class used to take table size and hash function \n
    then insert and search key, value paires.
    Apply appropriate strategy for collision.
    '''
    Attributes
    --------
        N: Integer of table size
        hash_function: Selected hash function
        A: Array to hold (key, value) pairs
        M: Number of keys,value inserted into array
    """
    def __init__(self, N, hash_function):
        """
        Initialize hash function
        """
        self.hash_function = hash_function
        self.N = N
        self.T = [None for i in range(N)]
        self.M = 0

    def add(self, key, value):
        """
        Add (key, value) pairs to index using hash function
        Arguments
        --------
            key: key to search for
            value: value coresponding to key
        Return
        --------
            True: hash table added successfully
            False: collision
        """
        hash_slot = self.hash_function(key, self.N)
        for i in range(self.N):
            test_slot = (hash_slot + i) % self.N
            if self.T[test_slot] is None:
                self.T[test_slot] = (key, value)
                self.M += 1
                return True
            else:
                return False

    def search(self, key):
        """
        Search for value through key
        Arguments
        --------
            key
        Return
        --------
            value: if key found
            None: if key not found
        """
        hash_slot = self.hash_function(key, self.N)
        for i in range(self.N):
            test_slot = (hash_slot + i) % self.N
            if self.T[test_slot] is None:
                return None
            elif self.T[test_slot][0] == key:
                return self.T[test_slot][1]
        return None


class ChainedHash:
    """
    A class used to take in table size and hash function\n
    to insert and search key, value pairs
    Attributes:
    --------
    hash_function: hash function of choice
    N: table size
    A: tuple array to hold key,values
    M: number of key,values inserted
    """

    def __init__(self, N, hash_function):
        self.hash_function = hash_function
        self.N = N
        self.T = [[] for i in range(N)]
        self.M = 0

    def add(self, key, value):
        """
        Add (key, value) pairs to index using hash function
        Arguments
        --------
            key: key to search for
            value: value coresponding to key
        Return
        --------
            True: hash table added successfully
        """
        hash_slot = self.hash_function(key, self.N)
        self.T[hash_slot].append((key, value))
        self.M += 1
        return True

    def search(self, key):
        """
        Search for value through key
        Arguments
        --------
            key
        Return
        --------
            value: if key found
            None: if key not found
        """
        hash_slot = self.hash_function(key, self.N)
        for i, j in self.T[hash_slot]:
            if (key == i):
                return j
        return None


if __name__ == '__main__':
    # parse arguments
    parser = argparse.ArgumentParser(description='Hash function test',
                                     prog='hash_function')
    parser.add_argument('--input', type=str, help='Input filename',
                        required=True)
    parser.add_argument('--table_size', type=int, help='Size of hash table',
                        required=True)
    parser.add_argument('--hash_method', type=str, help='ascii/rolling/python',
                        required=True)
    parser.add_argument('--collision', type=str, help='linear/chained',
                        required=True)
    parser.add_argument('--keys_to_add', type=int, help='keys to add',
                        required=True)
    parser.add_argument('--times_to_search', type=int, help='Times to search',
                        required=True)

    args = parser.parse_args()

    if not os.path.exists(args.input):
        print('No input file')
        sys.exit(1)

    hash_table = None
    collisions = ['linear', 'chained']
    if args.collision not in collisions:
        print('Hash collision not supported')
        sys.exit(1)

    if args.hash_method == 'ascii':
        if args.collision == 'linear':
            hash_table = LinearProbe(args.table_size, hash_functions.h_ascii)
        elif args.collision == 'chained':
            hash_table = ChainedHash(args.table_size, hash_functions.h_ascii)

    elif args.hash_method == 'rolling':
        if args.collision == 'linear':
            hash_table = LinearProbe(args.table_size, hash_functions.h_rolling)
        elif args.collision == 'chained':
            hash_table = ChainedHash(args.table_size, hash_functions.h_rolling)

    elif args.hash_method == 'python':
        if args.collision == 'linear':
            hash_table = LinearProbe(args.table_size, hash_functions.h_python)
        elif args.collision == 'chained':
            hash_table = ChainedHash(args.table_size, hash_functions.h_python)
    else:
        print('Hash functions not supported')
        sys.exit(1)

    V = []

    for line in open(args.input):
        reservoir_sampling(line, args.times_to_search, V)
        t0 = time.time()
        hash_table.add(line, line)
        t1 = time.time()
        print('add key value: ' + str(t1 - t0))
        if hash_table.M == args.keys_to_add:
            break

    for value in V:
        t0 = time.time()
        hit = hash_table.search(value)
        t1 = time.time()
        print('search: ', t1 - t0)

    sys.exit(0)
