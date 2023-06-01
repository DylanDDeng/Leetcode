/* 
方法二： 使用union 
*/  
SELECT t.name, t.population, t.area 
FROM world t 
WHERE t.area >= 3000000 

UNION  

SELECT t.name, t.population, t.area 
FROM world t 
WHERE t.population >= 25000000