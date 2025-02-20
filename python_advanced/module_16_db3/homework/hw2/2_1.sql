'''выводим имя покупателя, продавца, сумму, дату'''


select customer.full_name, manager.full_name, purchase_amount, "date"
from "order"
inner join customer on customer.customer_id = "order".customer_id
inner join manager on manager.manager_id = "order".manager_id
