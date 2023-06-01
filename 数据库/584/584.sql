/*
sql 里的不等于 不包含null， null 要另外筛选 
*/  

SELECT name 
FROM customer 
WHERE referee_id != 2 OR referee_id IS NULL ; 