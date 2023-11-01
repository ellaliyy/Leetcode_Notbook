# Write your MySQL query statement below
SELECT product_name, s.year, price
FROM Sales as s, Product as p
WHERE s.product_id = p.product_id
GROUP BY s.sale_id
