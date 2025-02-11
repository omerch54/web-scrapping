WITH biggest_gain AS(
    SELECT symbol, (price/avg_price) as percent_gain
    FROM quotes
)

SELECT bg.symbol, c.name
FROM biggest_gain bg
JOIN companies c
ON bg.symbol = c.symbol
ORDER BY bg.percent_gain DESC
LIMIT 1