CREATE DATABASE sdg_ai;
USE sdg_ai;

CREATE TABLE prompts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_prompt TEXT NOT NULL,
    ai_reply TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE USER 'meal_user'@'localhost' IDENTIFIED BY '50064516jcG@';
GRANT ALL PRIVILEGES ON sdg_ai.* TO 'meal_user'@'localhost';
FLUSH PRIVILEGES;

-- Optional: Insert a sample prompt and reply                   