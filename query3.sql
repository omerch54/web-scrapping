WITH abs_diff AS(
    SELECT symbol, price, ABS(price - avg_price) as abs
    FROM quotes
    WHERE abs<10
)

SELECT ad.symbol, c.name
FROM abs_diff ad
JOIN companies c
ON ad.symbol = c.symbol
WHERE ad.price>30
ORDER BY ad.abs ASC