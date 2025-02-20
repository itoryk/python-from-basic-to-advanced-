'''имена покупателей, которые не сделали ни одного заказа'''

select customer.full_name
from customer
left join "order" on customer.customer_id = "order".customer_id
where "order".customer_id isnull
order by full_name