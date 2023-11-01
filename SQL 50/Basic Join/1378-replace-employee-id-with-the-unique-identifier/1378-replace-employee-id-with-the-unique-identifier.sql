# Write your MySQL query statement below

SELECT unique_id, e.name
FROM Employees as e
LEFT OUTER JOIN EmployeeUNI as u on e.id = u.id
