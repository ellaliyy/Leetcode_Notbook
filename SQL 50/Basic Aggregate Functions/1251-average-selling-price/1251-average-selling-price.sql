# Write your MySQL query statement below
WITH 
Total_sales AS(
SELECT
    p.product_id, 
    SUM(p.price * u.units) as total_revenue,
    SUM(u.units) as total_units
FROM Prices p
LEFT JOIN UnitsSold u 
ON p.product_id = u.product_id AND u.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY p.product_id
)

SELECT product_id, IFNULL(ROUND((total_revenue / total_units), 2), 0) as average_price
FROM Total_sales;