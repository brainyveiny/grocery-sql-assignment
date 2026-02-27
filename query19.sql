SELECT p.product_name, s.units_bought
FROM sales s
RIGHT JOIN products p ON s.product_id = p.product_id;