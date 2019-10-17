python hash_functions.py --input rand_words.txt --hash_method ascii --hash_table_size 1000 | python scatter.py --out_file ascii_hash_function_rand.png --x_label 'Hashed word' --y_label 'Hashed value'

python hash_functions.py --input non_rand_words.txt --hash_method ascii --hash_table_size 1000 | python scatter.py --out_file ascii_hash_function_nonrand.png --x_label 'Hashed word' --y_label 'Hashed value'

python hash_functions.py --input rand_words.txt --hash_method rolling --hash_table_size 1000 | python scatter.py --out_file rolling_hash_function_rand.png --x_label 'Hashed word' --y_label 'Hashed value'

python hash_functions.py --input non_rand_words.txt --hash_method rolling --hash_table_size 1000 | python scatter.py --out_file rolling_hash_function_nonrand.png --x_label 'Hashed word' --y_label 'Hashed value'

python hash_functions.py --input rand_words.txt --hash_method h_python --hash_table_size 1000 | python scatter.py --out_file python_hash_function_rand.png --x_label 'Hashed word' --y_label 'Hashed value'

python hash_functions.py --input non_rand_words.txt --hash_method h_python --hash_table_size 1000 | python scatter.py --out_file python_hash_function_nonrand.png --x_label 'Hashed word' --y_label 'Hashed value'


for M in $( seq  1000 1000 10000 ); do
    python hash_tables.py --table_size 10000 --hash_method ascii --collision linear --input rand_words.txt --keys_to_add $M --times_to_search 1000 >  ascii_linear_rand.$M.txt
    python hash_tables.py --table_size 10000 --hash_method rolling --collision linear --input rand_words.txt --keys_to_add $M --times_to_search 1000 >  rolling_linear_rand.$M.txt
    python hash_tables.py --table_size 10000 --hash_method python --collision linear --input rand_words.txt --keys_to_add $M --times_to_search 1000 >  python_linear_rand.$M.txt
    python hash_tables.py --table_size 10000 --hash_method ascii --collision chained --input rand_words.txt --keys_to_add $M --times_to_search 1000 >  ascii_chained_rand.$M.txt
    python hash_tables.py --table_size 10000 --hash_method rolling --collision chained --input rand_words.txt --keys_to_add $M --times_to_search 1000 >  rolling_chained_rand.$M.txt
    python hash_tables.py --table_size 10000 --hash_method python --collision chained --input rand_words.txt --keys_to_add $M --times_to_search 1000 >  python_chained_rand.$M.txt
done

grep add ascii_linear_rand.*.txt | cut -d " " -f4,5 | python scatter.py --out_file figures/ascii_linear_rand_insert_time.png --x_label "Load factor" --y_label "Insert time"
grep add rolling_linear_rand.*.txt | cut -d " " -f4,5 | python scatter.py --out_file figures/rolling_linear_rand_insert_time.png --x_label "Load factor" --y_label "Insert time"
grep add python_linear_rand.*.txt | cut -d " " -f4,5 | python scatter.py --out_file figures/python_linear_rand_insert_time.png --x_label "Load factor" --y_label "Insert time"
grep add ascii_chained_rand.*.txt | cut -d " " -f4,5 | python scatter.py --out_file figures/ascii_chained_rand_insert_time.png --x_label "Load factor" --y_label "Insert time"
grep add rolling_chained_rand.*.txt | cut -d " " -f4,5 | python scatter.py --out_file figures/rolling_chained_rand_insert_time.png --x_label "Load factor" --y_label "Insert time"
grep add python_chained_rand.*.txt | cut -d " " -f4,5 | python scatter.py --out_file figures/python_chained_rand_insert_time.png --x_label "Load factor" --y_label "Insert time"



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

rm *00.txt
