SELECT a.card_number, a.card_family, SUM(b.value), COUNT(b.id)
FROM
    cards as a
LEFT JOIN transactions as b ON a.card_number=b.card_number
GROUP BY a.card_number, a.card_family;
