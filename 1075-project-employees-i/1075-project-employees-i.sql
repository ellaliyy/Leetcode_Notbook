# Write your MySQL query statement below
WITH 
Total_years AS(
SELECT 
    p.project_id, 
    SUM(e.experience_years) as total_years,
    COUNT(e.employee_id) as total_people
FROM Project p
JOIN Employee e
ON p.employee_id = e.employee_id
GROUP BY p.project_id
)

SELECT project_id, ROUND((total_years / total_people), 2) as average_years
FROM Total_years;