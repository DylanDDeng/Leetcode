SELECT b.Id 
FROM Weather a, Weather b 
WHERE b.Temperature > a.Temperature and DATEDIFF(b.recordDate, a.recordDate) = 1; 