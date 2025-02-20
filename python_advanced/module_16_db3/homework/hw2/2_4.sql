'''имена и номера заказов, которые покупатели сделали напрямую'''

select order_no, customer.full_name
from "order"
inner join customer on customer.customer_id = "order".customer_id
where  "order".manager_id isnull