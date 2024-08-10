-- a SQL script that creates a trigger that resets the attribute valid_email only
-- when the email has been changed.
DELIMITER $$ ;
CREATE TRIGGER resets_attribute_valid_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.valid_email != NEW.valid_email THEN
        SET NEW.valid_email = FALSE;
    END IF;
END$$
DELIMITER ;
-- poiuytrewq321#@