select player_name, games, round(hits*1.000/at_bats*1.000,3)::text as batting_average
from yankees
where at_bats>99
order by batting_average desc;