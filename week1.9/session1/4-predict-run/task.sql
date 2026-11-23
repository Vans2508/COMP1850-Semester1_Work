.headers on
.mode column

-- Write your sql for each task here - you can use comment (start with --) to add notes or number them. Remember your ; at the end of each query!
-- with multiple queries in the file, sql will run then one after the other and print them all out, so I recommend testing after each one.

-- Returns the names of the restaurants which have hygiene rating 5
SELECT name FROM restaurants WHERE hygiene_rating = 5; 

-- Returns the restaurants whose postcode starts with LS6
SELECT name FROM restaurants WHERE postcode LIKE 'LS6%';

-- Returns the names of the Italian cuisine restaurants
SELECT name FROM restaurants WHERE cuisine = 'Italian';

-- Returns the names of the restaurants which have either Italian or Thai cuisine and also have hygiene rating 5
SELECT name FROM restaurants WHERE (cuisine = 'Italian' OR cuisine = 'Thai') AND hygiene_rating = 5;
