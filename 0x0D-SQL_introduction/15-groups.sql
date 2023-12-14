-- this script counts duplicats
SELECT score, COUNT(score) AS number
FROM second_table
GROUP BY score 
HAVING number > 1;
