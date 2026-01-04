SELECT state, SUM(profit) AS lucro_total
FROM superstore
GROUP BY state
ORDER BY lucro_total DESC
LIMIT 5;