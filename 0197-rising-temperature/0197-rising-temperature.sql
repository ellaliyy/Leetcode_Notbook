# Write your MySQL query statement below
SELECT t.id
FROM Weather as t, Weather as y
WHERE DATEDIFF(t.recordDate, y.recordDate) = 1 AND t.temperature > y.temperature
