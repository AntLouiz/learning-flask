CREATE TABLE cities (id SERIAL PRIMARY KEY, city VARCHAR(50), uf VARCHAR(50));
CREATE TABLE person (
	id SERIAL PRIMARY KEY, 
	city_id INT REFERENCES cities(id),
	name VARCHAR(50),
	age INT,
	created TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
);
INSERT INTO cities (city, uf) VALUES ('Parnaíba', 'PI');
INSERT INTO cities (city, uf) VALUES ('Teresina', 'PI');
INSERT INTO cities (city, uf) VALUES ('Fortaleza', 'CE');
INSERT INTO cities (city, uf) VALUES ('Sao Paulo', 'SP');
SELECT * FROM cities;
DROP TABLE cities;
