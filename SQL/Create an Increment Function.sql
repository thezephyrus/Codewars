create or replace function increment(age int) 
returns int as $$
  begin  
    return age+1;
  end;
  $$ LANGUAGE plpgsql;

 CREATE FUNCTION increment(i integer) RETURNS integer
AS 'select $1 + 1;'
LANGUAGE sql;

CREATE FUNCTION increment (IN age integer, OUT integer) 
AS 'SELECT age + 1'
LANGUAGE SQL;

CREATE FUNCTION increment(@age INT) {
returns INT as
Begin
  return @age + 1;
end;

CREATE OR REPLACE FUNCTION increment(i integer) RETURNS integer
AS $$ BEGIN RETURN i + 1; END; $$
LANGUAGE plpgsql;

