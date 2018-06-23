select 
a.pokemon_name,
(a.str * b.multiplier)as modifiedStrength,
b.element
from pokemon a, multipliers b
where
a.element_id= b.id
and (a.str * b.multiplier) >=40
order by 2 desc;