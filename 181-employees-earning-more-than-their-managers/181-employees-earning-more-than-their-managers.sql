# Write your MySQL query statement below

SELECT a.name AS Employee FROM Employee AS a
LEFT JOIN Employee AS b on a.managerID = b.id
WHERE a.salary > b.salary