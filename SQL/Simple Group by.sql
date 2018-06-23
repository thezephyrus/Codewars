select age, count(id) as people_count
from people
group by age;