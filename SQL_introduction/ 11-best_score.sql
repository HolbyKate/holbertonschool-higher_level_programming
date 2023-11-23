-- list all records with a score >= 10 (ordered first by score, then by name)
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC, name DESC;