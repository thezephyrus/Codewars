select name, sum(won) as won, sum(lost) as lost
from fighters
where
move_id not in (select id from winning_moves where move in ('Hadoken','Shouoken','Kikoken'))
group by name
order by 2 desc
limit 6;