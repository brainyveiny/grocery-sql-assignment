SELECT customer_id, SUM(units_bought) AS total_units
FROM sales
GROUP BY customer_id;