-- Check if user 'user_0d_1' exists and list privileges
SELECT COUNT(*) FROM mysql.user WHERE user = 'user_0d_1';
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Check if user 'user_0d_2' exists and list privileges
SELECT COUNT(*) FROM mysql.user WHERE user = 'user_0d_2';
SHOW GRANTS FOR 'user_0d_2'@'localhost';

