DELIMITER $$

CREATE PROCEDURE AddBonus (
    IN user_id INT,
    IN project_name VARCHAR(255),
    IN score INT
)
BEGIN
    DECLARE project_id INT;

    -- Check if the project exists
    IF NOT EXISTS (SELECT 1 FROM projects WHERE name = project_name) THEN
        -- Insert the new project
        INSERT INTO projects (name) VALUES (project_name);
    END IF;

    -- Get the project id (it should be there now)
    SELECT id INTO project_id FROM projects WHERE name = project_name;

    -- Insert the correction
    INSERT INTO corrections (user_id, project_id, score)
    VALUES (user_id, project_id, score);
END$$

DELIMITER ;

-- -- a SQL script that creates a stored procedure AddBonus that adds a new correction for a student.
-- DELIMITER $$;
-- CREATE PROCEDURE AddBonus (user_id int, project_name varchar(255), score int)
-- BEGIN
--     IF NOT EXISTS (SELECT name FROM projects WHERE name = project_name) THEN
--         INSERT INTO projects (name) VALUES (project_name);
--     END IF;
--     INSERT INTO corrections (user_id, project_name, score)
--     VALUES (user_id, (SELECT id from projects WHERE name=project_name), score);
-- END$$
-- DELIMITER ;
-- poiuytrewq321#@
