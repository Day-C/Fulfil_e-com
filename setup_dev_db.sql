-- Create a database and a user and grant it privileges to that data base
CREATE DATABASE IF NOT EXISTS fufil_dev_db;
CREATE USER IF NOT EXISTS 'fufil_dev'@'localhost' IDENTIFIED BY 'fufil_dev_psword';
GRANT ALL PRIVILEGES ON `fufil_dev_db`.* TO 'fufil_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'fufil_dev'@'localhost';
FLUSH PRIVILEGES;
