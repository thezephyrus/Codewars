select id, name, split_part(m.characteristics,',',1) as characteristic
from monsters m
order by id;

select
  id,
  name,
  (string_to_array(characteristics, ', '))[1] characteristic
from monsters
order by id, name;


select id, name,   substring(characteristics from '^[^,]+') as characteristic from monsters order by id;


SELECT
  id,
  name,
  CASE WHEN characteristics like '%,%' 
  THEN left(characteristics,position(',' in characteristics)-1)
  ELSE characteristics END as characteristic
FROM monsters
ORDER BY id;

