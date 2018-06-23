select regexp_split_to_table(a.text,'[aeiouu]') as results
from random_string a;