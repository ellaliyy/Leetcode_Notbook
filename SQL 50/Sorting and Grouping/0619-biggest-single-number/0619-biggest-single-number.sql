# Write your MySQL query statement below
WITH single AS(
SELECT num
FROM MyNumbers
GROUP BY num
HAVING COUNT(num) = 1
)

SELECT Max(num) as num
FROM single
