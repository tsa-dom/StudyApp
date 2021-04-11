CREATE TABLE users (id SERIAL PRIMARY KEY, username VARCHAR ( 20 ) UNIQUE, password TEXT);
CREATE TABLE materials (id SERIAL PRIMARY KEY, name VARCHAR ( 50 ) NOT NULL, description VARCHAR ( 300 ), content_raw TEXT, owner_id INTEGER, category_name VARCHAR ( 20 ));
CREATE TABLE chapters (id SERIAL PRIMARY KEY, name VARCHAR ( 50 ) NOT NULL, material_id INTEGER, content_raw TEXT);