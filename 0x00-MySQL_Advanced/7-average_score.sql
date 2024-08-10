-- a SQL script that creates a stored procedure ComputeAverageScoreForUser that computes
-- and store the average score for a student. Note: An average score can be a decimal
DELIMITER $$;
CREATE  PROCEDURE ComputeAverageScoreForUser(user_id int)
BEGIN
    UPDATE users
    SELECT AVG(scores) AS average_score
    FROM scores
    WHERE user_id = user_id
END;$$
DELIMITER ;
-- poiuytrewq321#@