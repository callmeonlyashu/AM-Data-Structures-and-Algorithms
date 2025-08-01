-- You have a table named customers with columns id, name, country and currency.
-- I need a SQL query to get all columns ordered by USA appears at top followed by customers without UNION.

SELECT * FROM customers
ORDER BY
CASE WHEN country = 'USA' THEN 1 ELSE 2, customers