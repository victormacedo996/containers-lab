CREATE TABLE IF NOT EXISTS employees (
	id SERIAL PRIMARY KEY,
	name varchar(255) NOT NULL,
	age int

);

INSERT INTO employees (name, age) VALUES ('victor', 27), ('isadora', 30), ('Marcelo', 40);