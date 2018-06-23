select regexp_split_to_table('2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97', ',')::integer as prime ;
select unnest(string_to_array('2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97', ','))::integer as prime ;


select a.n as prime
from generate_series(2, 100) as a(n)
where not exists ( 
  select 1 
    from generate_series(2, a.n-1) as b(n)
   where a.n% b.n=0 );


SELECT * from (values (2),(3),(5),(7),(11),(13),(17),(19),(23),(29),(31),(37),(41),(43),(47),(53),(59),(61),(67),(71),(73),(79),(83),(89),(97)) as tbl(prime)

SELECT
    number AS prime
FROM
    generate_series(1, 100) AS number
WHERE
    NOT REPEAT('1', number) ~ '^1?$|^(11+?)\1+$'
;


SELECT a.n prime
  FROM generate_series(1, 100) as a(n)
 WHERE a.n > 1
   AND (a.n%2 <> 0 or a.n = 2)
   AND (a.n%3 <> 0 or a.n = 3)
   AND (a.n%5 <> 0 or a.n = 5)
   AND (a.n%7 <> 0 or a.n = 7);

 with ser as (
select generate_series as n
from generate_series(2,100))
select s.n prime
  from ser s 
 where not exists (select s2.n from ser s2
                     where s2.n < s.n
                       and s.n % s2.n = 0)

SELECT unnest( ARRAY[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97] ) as prime;

