#!/bin/bash

test -e ssshtest || wget https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run code_style pycodestyle hash_functions.py
assert_no_stdout
run code_style pycodestyle test_hash_functions.py
assert_no_stdout
run code_style pycodestyle hash_tables.py
assert_no_stdout
run code_style pycodestyle test_hash_table.py
assert_no_stdout
run code_style pycodestyle scatter.py
assert_no_stdout


run test_hash_function python hash_functions.py --input rand_words.txt --hash_method ascii --hash_table_size 1000
assert_exit_code 0

run test_hash_function python hash_functions.py --input non_rand_words.txt --hash_method ascii --hash_table_size 1000
assert_exit_code 0

run test_hash_function python hash_functions.py --input rand_words.txt --hash_method rolling --hash_table_size 1000
assert_exit_code 0

run test_hash_function python hash_functions.py --input non_rand_words.txt --hash_method rolling --hash_table_size 1000
assert_exit_code 0

run test_hash_function python hash_functions.py --input rand_words.txt --hash_method h_python --hash_table_size 1000
assert_exit_code 0

run test_hash_function python hash_functions.py --input non_rand_words.txt --hash_method h_python --hash_table_size 1000
assert_exit_code 0


run test_hash_function python hash_functions.py --input rand_words.txt --hash_method ascii_sum --hash_table_size 1000
assert_exit_code 1

run test_hash_function python hash_functions.py --input words.txt --hash_method ascii --hash_table_size 1000
assert_exit_code 1

run test_hash_table python hash_tables.py --input rand_words.txt --table_size 10000 --hash_method ascii --collision linear --keys_to_add 100 --times_to_search 100
assert_exit_code 0

run test_hash_table python hash_tables.py --input words.txt --table_size 10000 --hash_method ascii --collision linear --keys_to_add 100 --times_to_search 100
assert_exit_code 1

run test_hash_table python hash_tables.py --input rand_words.txt --table_size 10000 --hash_method ascii_sum --collision linear --keys_to_add 100 --times_to_search 100
assert_exit_code 1

run test_hash_table python hash_tables.py --input rand_words.txt --table_size 10000 --hash_method ascii --collision nocoli --keys_to_add 100 --times_to_search 100
assert_exit_code 1


