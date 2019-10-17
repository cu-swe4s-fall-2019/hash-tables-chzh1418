import unittest
import os
import hash_tables
import hash_functions


class TestHashTables(unittest.TestCase):
    def test_reservoir_sampling(self):
        A = [1, 2, 3, 4, 5]
        self.assertEqual('val' in A, False)
        self.assertEqual(5 in A, True)
        hash_tables.reservoir_sampling('val', 6, A)
        self.assertEqual('val' in A, True)
        self.assertEqual(5 in A, True)

    def test_linear_probing(self):
        test1 = hash_tables.LinearProbe(1000, hash_functions.h_ascii)
        test1.add('keya', 'valuea')
        test1.add('keyb', 'valueb')
        self.assertEqual(test1.search('keya'), 'valuea')
        self.assertNotEqual(test1.search('keya'), 'keya')
        self.assertEqual(test1.search('keyb'), 'valueb')
        self.assertNotEqual(test1.search('keyb'), 'keyb')

        test2 = hash_tables.LinearProbe(1000, hash_functions.h_rolling)
        test2.add('keya', 'valuea')
        test2.add('keyb', 'valueb')
        self.assertEqual(test2.search('keya'), 'valuea')
        self.assertNotEqual(test2.search('keya'), 'keya')
        self.assertEqual(test2.search('keyb'), 'valueb')
        self.assertNotEqual(test2.search('keyb'), 'keyb')

        test3 = hash_tables.LinearProbe(1000, hash_functions.h_python)
        test3.add('keya', 'valuea')
        test3.add('keyb', 'valueb')
        self.assertEqual(test3.search('keya'), 'valuea')
        self.assertNotEqual(test3.search('keya'), 'keya')
        self.assertEqual(test3.search('keyb'), 'valueb')
        self.assertNotEqual(test3.search('keyb'), 'keyb')

    def test_chained_hash(self):
        test1 = hash_tables.ChainedHash(1000, hash_functions.h_ascii)
        test1.add('keya', 'valuea')
        test1.add('keyb', 'valueb')
        self.assertEqual(test1.search('keya'), 'valuea')
        self.assertNotEqual(test1.search('keya'), 'keya')
        self.assertEqual(test1.search('keyb'), 'valueb')
        self.assertNotEqual(test1.search('keyb'), 'keyb')

        test2 = hash_tables.ChainedHash(1000, hash_functions.h_rolling)
        test2.add('keya', 'valuea')
        test2.add('keyb', 'valueb')
        self.assertEqual(test2.search('keya'), 'valuea')
        self.assertNotEqual(test2.search('keya'), 'keya')
        self.assertEqual(test2.search('keyb'), 'valueb')
        self.assertNotEqual(test2.search('keyb'), 'keyb')

        test3 = hash_tables.ChainedHash(1000, hash_functions.h_python)
        test3.add('keya', 'valuea')
        test3.add('keyb', 'valueb')
        self.assertEqual(test3.search('keya'), 'valuea')
        self.assertNotEqual(test3.search('keya'), 'keya')
        self.assertEqual(test3.search('keyb'), 'valueb')
        self.assertNotEqual(test3.search('keyb'), 'keyb')


if __name__ == '__main__':
    unittest.main()
