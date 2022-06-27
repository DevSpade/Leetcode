# Write your MySQL query statement below

select firstName,lastName,city,state from Person a LEFT JOIN Address b ON a.personId = b.personId;