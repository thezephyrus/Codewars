select * from students
where
quality1 in ('evil','cunning') and quality2 in ('evil','cunning')
OR quality1 ='brave' and quality2!='evil'
OR quality1 in ('studious','intelligent') OR quality2 in ('studious','intelligent')
OR quality1 in ('hufflepuff') OR quality2 in ('hufflepuff')
order by id asc;