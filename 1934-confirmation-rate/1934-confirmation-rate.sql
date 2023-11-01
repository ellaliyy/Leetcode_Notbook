# Write your MySQL query statement below


-- first get total number of confirmed
-- The LEFT JOIN ensures that even if a user has no confirmations, they will still appear in the results with a count of 0
WITH Confirmed AS (
    SELECT s.user_id, COUNT(c.action) as confirmed
    FROM Signups as s
    LEFT JOIN Confirmations as c ON s.user_id = c.user_id AND c.action = 'confirmed'
    GROUP BY s.user_id
),
-- then get the total number of action
-- LFFT JOIN here: even though the user didn't request confirmation, it will still in the table
Total AS (
    SELECT s.user_id, COUNT(c.action) as total
    FROM Signups as s
    LEFT JOIN Confirmations as c ON s.user_id = c.user_id
    GROUP BY s.user_id
)

SELECT Confirmed.user_id, 
       CASE 
           WHEN Total.total = 0 THEN 0 
           ELSE ROUND(Confirmed.confirmed * 1.0 / Total.total, 2)
       END as confirmation_rate
FROM Confirmed
JOIN Total ON Confirmed.user_id = Total.user_id
