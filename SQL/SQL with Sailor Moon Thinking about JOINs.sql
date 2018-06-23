select
senshi_name as sailor_senshi,
real_name_jpn as real_name,
c.name as cat,
sc.school as school
from sailorsenshi s
left join cats c on
c.id=s.cat_id
left join schools sc on 
s.school_id= sc.id;