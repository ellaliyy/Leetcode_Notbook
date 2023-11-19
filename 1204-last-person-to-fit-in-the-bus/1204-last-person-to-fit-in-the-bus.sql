# Write your MySQL query statement below
WITH Q as(
SELECT *
FROM Queue
ORDER BY turn
)


SELECT q1.person_name
FROM Q q1
JOIN Q q2 ON q1.turn >= q2.turn
GROUP BY q1.turn
HAVING SUM(q2.weight) <= 1000
ORDER BY SUM(q2.weight) DESC
LIMIT 1;
