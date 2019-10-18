# Hash tables
Implement different hash functions and test for insert time

## Continuous Integration status


## Installation
To use this package, you need to install [Python3](https://www.python.org/downloads/release/python-373/) in your environment.
Other used packages are listed below.

### Used packages
* os
* sys
* time
* random
* argparse
* matplotlib
* pycodestyle
## Unit test
```bash
python test_hash_functions.py
python test_hash_table.py
```
## functional test
```bash
bash functional_test.sh
```

## Usage
### Plots for hash functions
#### Arguments for hash functions
* --input: 		input file name, e.g. rand_words.txt
* --hash_method:	selection of hash method, e.g. ascii/rolling/h_python
* --hash_table_size: 	the size of hash table, e.g. 1000
#### Arguments for scatter function
* --out_file:		name of output file, e.g. ascii_hash_function_rand.png
* --x_label:		x axis label
* --y_label: 		y axis label 
##### ascii plot for random words
```bash
python hash_functions.py --input rand_words.txt --hash_method ascii --hash_table_size 1000 | python scatter.py --out_file ascii_hash_function_rand.png --x_label 'Hashed word' --y_label 'Hashed value'
```
![](https://github.com/cu-swe4s-fall-2019/hash-tables-chzh1418/blob/master/ascii_hash_function_rand.png)

##### ascii plot for non random words
```bash
python hash_functions.py --input non_rand_words.txt --hash_method ascii --hash_table_size 1000 | python scatter.py --out_file ascii_hash_function_nonrand.png --x_label 'Hashed word' --y_label 'Hashed value'
```
![](https://github.com/cu-swe4s-fall-2019/hash-tables-chzh1418/blob/master/ascii_hash_function_nonrand.png)

##### rolling plot for random words
```bash
python hash_functions.py --input rand_words.txt --hash_method rolling --hash_table_size 1000 | python scatter.py --out_file rolling_hash_function_rand.png --x_label 'Hashed word' --y_label 'Hashed value'
```
![](https://github.com/cu-swe4s-fall-2019/hash-tables-chzh1418/blob/master/rolling_hash_function_rand.png)

##### rolling plot for non random words
```bash
python hash_functions.py --input non_rand_words.txt --hash_method rolling --hash_table_size 1000 | python scatter.py --out_file rolling_hash_function_nonrand.png --x_label 'Hashed word' --y_label 'Hashed value'
```
![](https://github.com/cu-swe4s-fall-2019/hash-tables-chzh1418/blob/master/rolling_hash_function_nonrand.png)

##### python hash for randon words
```bash
python hash_functions.py --input rand_words.txt --hash_method h_python --hash_table_size 1000 | python scatter.py --out_file python_hash_function_rand.png --x_label 'Hashed word' --y_label 'Hashed value'
```
![](https://github.com/cu-swe4s-fall-2019/hash-tables-chzh1418/blob/master/python_hash_function_rand.png)

##### python hash for non random words
```bash
python hash_functions.py --input non_rand_words.txt --hash_method h_python --hash_table_size 1000 | python scatter.py --out_file python_hash_function_nonrand.png --x_label 'Hashed word' --y_label 'Hashed value'
```
![](https://github.com/cu-swe4s-fall-2019/hash-tables-chzh1418/blob/master/python_hash_function_nonrand.png)


#### Arguments for hash table_table.py
* --input:		input file name
* -- table_size:	size of hash table, e.g. 1000
* --hash_method:	name of hash methods, e.g. ascii/rolling/python
* --collision:		collision strategy, e.g. linear/chained
* -- keys_to_add:	number of keys to add, e.g. 100
* --times_to_search: 	number of searching times

##### ascii hashing of random words with linear probing
``` bash
for M in $( seq  1000 1000 10000 ); do
    python hash_tables.py --table_size 10000 --hash_method ascii --collision linear --input rand_words.txt --keys_to_add $M --times_to_search 1000 >  ascii_linear_rand.$M.txt
done
grep add ascii_linear_rand.*.txt | cut -d " " -f4,5 | python scatter.py --out_file figures/ascii_linear_rand_insert_time.png --x_label "Load factor" --y_label "Insert time"
```
![](https://github.com/cu-swe4s-fall-2019/hash-tables-chzh1418/blob/master/figures/ascii_linear_rand_insert_time.png)

##### rolling hashing of random words with linear probing
```bash
for M in $( seq  1000 1000 10000 ); do
    python hash_tables.py --table_size 10000 --hash_method rolling --collision linear --input rand_words.txt --keys_to_add $M --times_to_search 1000 >  rolling_linear_rand.$M.txt
done
grep add rolling_linear_rand.*.txt | cut -d " " -f4,5 | python scatter.py --out_file figures/rolling_linear_rand_insert_time.png --x_label "Load factor" --y_label "Insert time"
```
![](https://github.com/cu-swe4s-fall-2019/hash-tables-chzh1418/blob/master/figures/rolling_linear_rand_insert_time.png)

##### python hashing of random words with linear probing
``` bash
for M in $( seq  1000 1000 10000 ); do
    python hash_tables.py --table_size 10000 --hash_method python --collision linear --input rand_words.txt --keys_to_add $M --times_to_search 1000 >  python_linear_rand.$M.txt
done
grep add python_linear_rand.*.txt | cut -d " " -f4,5 | python scatter.py --out_file figures/python_linear_rand_insert_time.png --x_label "Load factor" --y_label "Insert time"
```
![](https://github.com/cu-swe4s-fall-2019/hash-tables-chzh1418/blob/master/figures/python_linear_rand_insert_time.png)

###### hashing of random words with chained hash
```bash
for M in $( seq  1000 1000 10000 ); do
    python hash_tables.py --table_size 10000 --hash_method ascii --collision chained --input rand_words.txt --keys_to_add $M --times_to_search 1000 >  ascii_chained_rand.$M.txt
    python hash_tables.py --table_size 10000 --hash_method rolling --collision chained --input rand_words.txt --keys_to_add $M --times_to_search 1000 >  rolling_chained_rand.$M.txt
    python hash_tables.py --table_size 10000 --hash_method python --collision chained --input rand_words.txt --keys_to_add $M --times_to_search 1000 >  python_chained_rand.$M.txt
done
grep add ascii_chained_rand.*.txt | cut -d " " -f4,5 | python scatter.py --out_file figures/ascii_chained_rand_insert_time.png --x_label "Load factor" --y_label "Insert time"
grep add rolling_chained_rand.*.txt | cut -d " " -f4,5 | python scatter.py --out_file figures/rolling_chained_rand_insert_time.png --x_label "Load factor" --y_label "Insert time"
grep add python_chained_rand.*.txt | cut -d " " -f4,5 | python scatter.py --out_file figures/python_chained_rand_insert_time.png --x_label "Load factor" --y_label "Insert time"
```
![](https://github.com/cu-swe4s-fall-2019/hash-tables-chzh1418/blob/master/figures/ascii_chained_rand_insert_time.png)
![](https://github.com/cu-swe4s-fall-2019/hash-tables-chzh1418/blob/master/figures/python_chained_rand_insert_time.png)
![](https://github.com/cu-swe4s-fall-2019/hash-tables-chzh1418/blob/master/figures/rolling_chained_rand_insert_time.png)

###### hashing of non random words]
```bash
for M in $( seq  1000 1000 10000 ); do
    python hash_tables.py --table_size 10000 --hash_method ascii --collision linear --input non_rand_words.txt --keys_to_add $M --times_to_search 1000 >  ascii_linear_non_rand.$M.txt
    python hash_tables.py --table_size 10000 --hash_method rolling --collision linear --input non_rand_words.txt --keys_to_add $M --times_to_search 1000 >  rolling_linear_non_rand.$M.txt
    python hash_tables.py --table_size 10000 --hash_method python --collision linear --input non_rand_words.txt --keys_to_add $M --times_to_search 1000 >  python_linear_non_rand.$M.txt
    python hash_tables.py --table_size 10000 --hash_method ascii --collision chained --input non_rand_words.txt --keys_to_add $M --times_to_search 1000 >  ascii_chained_non_rand.$M.txt
    python hash_tables.py --table_size 10000 --hash_method rolling --collision chained --input non_rand_words.txt --keys_to_add $M --times_to_search 1000 >  rolling_chained_non_rand.$M.txt
    python hash_tables.py --table_size 10000 --hash_method python --collision chained --input non_rand_words.txt --keys_to_add $M --times_to_search 1000 >  python_chained_non_rand.$M.txt
done

grep add ascii_linear_non_rand.*.txt | cut -d " " -f4,5 | python scatter.py --out_file figures/ascii_linear_non_rand_insert_time.png --x_label "Load factor" --y_label "Insert time"
grep add rolling_linear_non_rand.*.txt | cut -d " " -f4,5 | python scatter.py --out_file figures/rolling_linear_non_rand_insert_time.png --x_label "Load factor" --y_label "Insert time"
grep add python_linear_non_rand.*.txt | cut -d " " -f4,5 | python scatter.py --out_file figures/python_linear_non_rand_insert_time.png --x_label "Load factor" --y_label "Insert time"
grep add ascii_chained_non_rand.*.txt | cut -d " " -f4,5 | python scatter.py --out_file figures/ascii_chained_non_rand_insert_time.png --x_label "Load factor" --y_label "Insert time"
grep add rolling_chained_non_rand.*.txt | cut -d " " -f4,5 | python scatter.py --out_file figures/rolling_chained_non_rand_insert_time.png --x_label "Load factor" --y_label "Insert time"
grep add python_chained_non_rand.*.txt | cut -d " " -f4,5 | python scatter.py --out_file figures/python_chained_non_rand_insert_time.png --x_label "Load factor" --y_label "Insert time"
```
![](https://github.com/cu-swe4s-fall-2019/hash-tables-chzh1418/blob/master/figures/ascii_linear_non_rand_insert_time.png)
![](https://github.com/cu-swe4s-fall-2019/hash-tables-chzh1418/blob/master/figures/rolling_linear_non_rand_insert_time.png)
![](https://github.com/cu-swe4s-fall-2019/hash-tables-chzh1418/blob/master/figures/python_linear_non_rand_insert_time.png)
![](https://github.com/cu-swe4s-fall-2019/hash-tables-chzh1418/blob/master/figures/ascii_chained_non_rand_insert_time.png)
![](https://github.com/cu-swe4s-fall-2019/hash-tables-chzh1418/blob/master/figures/rolling_chained_non_rand_insert_time.png)
![](https://github.com/cu-swe4s-fall-2019/hash-tables-chzh1418/blob/master/figures/python_chained_non_rand_insert_time.png)
