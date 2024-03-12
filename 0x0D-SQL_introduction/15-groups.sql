-- list the number of records that has the same score
SELECT score,COUNT(score) as number FROM `second_table` GROUP BY score;
