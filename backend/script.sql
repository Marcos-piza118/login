CREATE DATABASE IF NOT EXISTS estudionet_db;
USE estudionet_db;

CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    full_name VARCHAR(100),
    role ENUM('admin', 'user') DEFAULT 'user',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insertar usuario admin (password: admin123)
INSERT INTO users (username, email, password, full_name, role) 
VALUES ('admin', 'admin@estudionet.com', '$2b$12$Lk3VU7l/7jR6p6p6p6p6p.EY5jJ5Z5Z5Z5Z5Z5Z5Z5Z5Z5Z5Z5Z5Z5Z', 'Administrador Principal', 'admin');

-- Insertar usuario normal (password: user123)
INSERT INTO users (username, email, password, full_name) 
VALUES ('juanperez', 'juan@email.com', '$2b$12$Lk3VU7l/7jR6p6p6p6p6p.EY5jJ5Z5Z5Z5Z5Z5Z5Z5Z5Z5Z5Z5Z5Z5Z', 'Juan Pérez', 'user');