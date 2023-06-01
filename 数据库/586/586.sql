SELECT t. customer_number 
FROM (SELECT customer_number, COUNT(order_number) as num 
      FROM Orders 
      GROUP BY customer_number
      ) t 
ORDER BY t.num DESC 
LIMIT 1 