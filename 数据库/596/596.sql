SELECT t.class 
FROM (SELECT class, COUNT(student) as num 
      FROM Courses 
      GROUP BY class) t 
WHERE t.num >=5;  
