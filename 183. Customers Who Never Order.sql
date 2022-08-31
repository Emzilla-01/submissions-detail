-- # Write your MySQL query statement below
-- 619 ms, 437 ms, 551 ms, faster than 55.67%
select name as Customers
from Customers
where id not in
    (select customerId 
    from Orders
    group by customerId)

-- anti-join 1045 ms, 678 ms, 624 ms
select name as Customers
from Customers
left join Orders
on Customers.id = Orders.customerId
where Orders.customerId is null 