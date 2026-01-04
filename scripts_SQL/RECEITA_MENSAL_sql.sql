SELECT DATE_FORMAT(order_date, '%Y-%m') AS mes, SUM(sales) AS receita
FROM superstore
GROUP BY mes
ORDER BY mes;