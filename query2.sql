SELECT c.name
FROM quotes q
JOIN companies c
ON q.symbol = c.symbol
WHERE q.close> q.avg_price
ORDER BY q.price DESC
LIMIT 1