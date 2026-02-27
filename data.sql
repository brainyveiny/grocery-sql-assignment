INSERT INTO customers (customer_name, phone) VALUES
('Ram', '9876543210'),
('Sita', '9876500000'),
('Arjun', '9999999999');

INSERT INTO products (product_name, price_per_unit, stock) VALUES
('Rice', 50.00, 100),
('Milk', 25.00, 200),
('Oil', 120.00, 50),
('Sugar', 40.00, 150);

INSERT INTO sales (customer_id, product_id, units_bought, bill_date) VALUES
(1, 1, 2, '2024-02-01'),
(1, 2, 5, '2024-02-01'),
(2, 3, 1, '2024-02-02'),
(3, 1, 3, '2024-02-03'),
(2, 4, 4, '2024-02-03');