.headers on
.mode column

-- add tasks below
-- sqlite3 database_file.db to open the database
-- .read sql_file.sql to run the queries

 --1
 SELECT count(name)
 FROM drivers;

--2
SELECT count(name) 
FROM menu_items
WHERE price > 10;

--3
SELECT count(postcode) 
FROM restaurants
WHERE postcode LIKE 'LS2%';

SELECT count(postcode)
FROM customers
WHERE postcode LIke'LS2%';

--4
SELECT name
FROM restaurants
WHERE cuisine = 'Thai'
ORDER BY name LIMIT 3;

--5
.schema customers