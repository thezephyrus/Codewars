select initcap(firstname || ' ' || lastname)  as shortlist 
from elves 
where firstname like ('%tegil%') OR lastname like('%astar%');