import unittest
import os
import hash_functions


class TestHashFunctions(unittest.TestCase):
    def test_hash_integer(self):
        self.assertEqual(hash_functions.check_integer('a'), False)

    def test_hash_integer2(self):
        self.assertEqual(hash_functions.check_integer(1), True)

    def test_hash_integer3(self):
        self.assertEqual(hash_functions.check_integer(-1), False)

    def test_h_ascii(self):
        keya = hash_functions.h_ascii('keya', 1000)
        keyb = hash_functions.h_ascii('keyb', 1000)
        self.assertNotEqual(keya, keyb)
        keay = hash_functions.h_ascii('keay', 1000)
        self.assertEqual(keya, keay)

    def test_h_rolling(self):
        keya = hash_functions.h_rolling('keya', 1000)
        keyb = hash_functions.h_rolling('keyb', 1000)
        self.assertNotEqual(keya, keyb)

    def test_h_python(self):
        keya = hash_functions.h_python('keya', 1000)
        keyb = hash_functions.h_python('keyb', 1000)
        self.assertNotEqual(keya, keyb)

    def test_random_check(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
