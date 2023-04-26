# Write your MySQL query statement below
# Trying to complete lc sql study plans for the badges & warmups.

select employee_id,
     IF(
         SUBSTRING(name, 1, 1)='M',
         salary, 0) bonus
order by employee_id


select v.customer_id, count(v.visit_id) as count_no_trans 
from Visits v
left join
Transactions t 
on (t.visit_id = v.visit_id)
where t.visit_id is NULL
group by v.customer_id



select customer_id, count(visit_id) as count_no_trans 
from Visits
where visit_id not in 
    (select visit_id from Transactions)
group by customer_id



select 
w1.id
from Weather w1
right join Weather w0
on w0.id+1 = w1.id
and w0.temperature < w1.temperature
where w1.id is not null


####

with w0 as
(select
*,
ROW_NUMBER()
        over (partition by true order by recordDate asc) as rn
    from Weather)

, w1 as
(select
*,
ROW_NUMBER()
        over (partition by true order by recordDate asc) as rn
    from Weather)

select w1.id from 
w1 right join w0
on w0.rn+1 = w1.rn
and w0.temperature < w1.temperature
where w1.id is not null and w0.id is not null


select sell_date,
count(distinct(product)) as num_sold,
group_concat(distinct product order by product) as products
from Activities
group by sell_date