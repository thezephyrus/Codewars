
select count(name) as unique_products, producer
from products
group by producer
order by unique_products desc, producer;