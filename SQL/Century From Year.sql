select
 (case
  when mod(yr,100)=0 then yr/100
  else (yr/100)+1

end) as century
from years