# Write your MySQL query statement below

select name as Customers 
from Customers as a 
LEFT JOIn Orders as o ON a.id = o.CustomerId
Where o.id IS NULL