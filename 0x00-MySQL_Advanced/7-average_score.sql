-- a stored procedure that computes and store the average score for a student
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
	DECLARE avg_score FLOAT;

	-- get the avg score for the student
	SELECT AVG(score) INTO avg_score FROM corrections WHERE corrections.user_id = user_id;

	-- Update the user's average score in the users table
	UPDATE users SET average_score = avg_score WHERE users.id = user_id;
END //

DELIMITER ;
