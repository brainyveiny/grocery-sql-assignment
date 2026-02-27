SELECT SUM(p.price_per_unit * s.units_bought) AS total_revenue
FROM sales s
JOIN products p ON s.product_id = p.product_id;