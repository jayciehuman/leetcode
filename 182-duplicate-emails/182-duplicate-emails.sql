# Write your MySQL query statement below

SELECT DISTINCT email FROM
(SELECT email, COUNT(email) as num FROM Person 
GROUP BY email) as temp
WHERE num > 1