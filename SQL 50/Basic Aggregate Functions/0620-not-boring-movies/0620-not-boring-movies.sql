# Write your MySQL query statement below
SELECT *
FROM Cinema
WHERE description != 'boring' AND id IN (1,3,5,7,9)
ORDER BY rating DESC;