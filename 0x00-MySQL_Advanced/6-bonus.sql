-- a SQL script that creates a stored procedure AddBonus that adds a new correction for a student.
-- DELIMITER $$ ;
-- CREATE PROCEDURE AddBonus (user_id int, project_name varchar(255), score int)
-- BEGIN
DELIMITER $$;
CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT )
BEGIN
    IF NOT EXISTS (SELECT name FROM projects WHERE name = project_name) THEN
        INSERT INTO projects (name) VALUES (project_name);
    END IF;
    INSERT INTO corrections (user_id, project_name, score)
    -- VALUES (user_id, project_id, score);
    VALUES (user_id, (SELECT id from projects WHERE name=project_name), score);
END $$
DELIMITER ;
-- poiuytrewq321#@
