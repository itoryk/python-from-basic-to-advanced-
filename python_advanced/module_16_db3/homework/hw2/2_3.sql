'''выводим номер заказа, имена покупателей и продавцов, где место жительства не совпадает'''

select order_no, manager.full_name, customer.full_name
from "order"
inner join customer on customer.customer_id = "order".customer_id
inner join manager on manager.manager_id = "order".manager_id
where manager.city != customer.city