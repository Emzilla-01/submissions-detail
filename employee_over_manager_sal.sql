-- 181. Employees Earning More Than Their Managers
-- mysql
select a.name as Employee from 

Employee as a,
Employee as b

where 
a.managerId=b.id
and a.salary>b.salary
