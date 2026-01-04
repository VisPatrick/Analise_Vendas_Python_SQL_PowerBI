SELECT category, SUM(sales) AS receita, SUM(profit) AS lucro
FROM superstore
GROUP BY category
ORDER BY receita DESC;