-- a SQL script that creates a stored procedure AddBonus that adds a new correction for a student.
DELIMITER $$ ;
CREATE PROCEDURE AddBonus (user_id INT, project_name VARCHAR(255), score INT)
BEGIN
IF NOT EXISTS (SELECT 1 FROM projects WHERE name = project_name) THEN
    INSERT INTO projects (name) VALUES (project_name);
END IF;
INSERT INTO corrections (user_id, project_name, score)
VALUES (user_id, project_id, score);
END$$
DELIMITER ;
-- poiuytrewq321#@