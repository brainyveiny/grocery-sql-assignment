SELECT c.customer_name, s.bill_id
FROM customers c
LEFT JOIN sales s ON c.customer_id = s.customer_id;