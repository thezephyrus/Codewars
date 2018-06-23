select length(name) as id, length(legs::text) as name,
  length(arms::text) as legs, length(characteristics)as arms,
  length(id::text) as characteristics
from monsters;