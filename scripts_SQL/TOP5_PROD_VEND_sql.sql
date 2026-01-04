SELECT product_name, SUM(sales) AS total_vendas
FROM superstore
GROUP BY product_name
ORDER BY total_vendas DESC
LIMIT 5;