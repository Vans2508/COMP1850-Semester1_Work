.headers on
.mode column

-- Write your sql for each task here - you can use comment (start with --) to add notes or number them. Remember your ; at the end of each query!
-- with multiple queries in the file, sql will run then one after the other and print them all out, so I recommend testing after each one.


--BRONZE--
--1
--SELECT * 
--FROM drivers;

--2
--SELECT name,price 
--FROM menu_items 
--WHERE restaurant_id = 
--(SELECT restaurant_id 
--FROM restaurants 
--WHERE name = 'Bangkok Garden');

--3
--SELECT name 
--FROM restaurants 
--WHERE cuisine = 'Indian';

--4
--SELECT count(customer_id) 
--FROM customers;

--SILVER REQUESTS--
--5
--SELECT name,price 
--FROM menu_items 
--WHERE (is_vegetarian = 1 AND price < 8) --ORDER by price;

--6
--SELECT name 
--FROM restaurants 
--WHERE hygiene_rating < 4 
--Order BY hygiene_rating ASC;

--7 
--A matching postcode district does not guarantee proximity: postcodes cover areas rather than exact locations. An LS6 restaurant could be several miles away, while a nearby restaurant in LS7 or LS1 could be excluded. The postcode data may also be missing or incorrect, and a full postcode would give a much more precise comparison ideally using real distance coordinates.--
--SELECT name, hygiene_rating, postcode
--FROM restaurants
--WHERE postcode LIKE 'LS6%'
--ORDER BY hygiene_rating DESC;

--8
-- Leeds Eats should not automatically send this marketing email. Having a University of Leeds email does not prove the customer has consented to marketing, and this query only identifies likely university users. The team should use an opt-in list and provide an unsubscribe option instead.
--SELECT name, email, joined_date
--FROM customers
--WHERE email LIKE '%@leeds.ac.uk'
--ORDER BY joined_date DESC;

--9
SELECT order_id, customer_id, restaurant_id, order_time
FROM orders
WHERE status = 'cancelled'
ORDER BY order_time DESC
LIMIT 10;

--10
