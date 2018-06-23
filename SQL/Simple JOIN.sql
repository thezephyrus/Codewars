select 
p.id, p.name, p.isbn, p.company_id,p.price,c.name as company_name
from products p, companies c where p.company_id=c.id;