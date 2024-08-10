-- a SQL script that creates a stored procedure ComputeAverageScoreForUser that computes
-- and store the average score for a student. Note: An average score can be a decimal
DELIMITER $$;
CREATE IF NOT EXISTS PROCEDURE ComputeAverageScoreForUser(user_id int)
BEGIN
    SELECT AVG(scores)
    FROM scores
    WHERE user_id = user_id
END;$$
DELIMITER ;
-- poiuytrewq321#@