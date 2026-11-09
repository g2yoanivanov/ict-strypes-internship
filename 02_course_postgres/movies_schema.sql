--- Actor Table
--- function: CREATE TABLE

CREATE TABLE actors (
	actor_id SERIAL PRIMARY KEY,
	first_name VARCHAR(150),
	last_name VARCHAR(150) NOT NULL,
	gender CHAR(1),
	date_of_birth DATE,
	add_date DATE,
	update_date DATE
);

--- Director Table
--- function: CREATE TABLE

CREATE TABLE directors (
	director_id SERIAL PRIMARY KEY,
	first_name VARCHAR(150),
	last_name VARCHAR(150) NOT NULL,
	date_of_birth DATE,
	nationality VARCHAR(20),
	add_date DATE,
	update_date DATE
);

--- Movies Table
--- function: CREATE TABLE

CREATE TABLE movies (
	movie_id SERIAL PRIMARY KEY,
	movie_name VARCHAR(100) NOT NULL,
	movie_lenght INT,
	movie_lang VARCHAR(20),
	age_certifacate VARCHAR(10),
	release_date DATE,
	director_id INT REFERENCES directors(director_id)
);

--- Movie Revenue Table
--- function: CREATE TABLE

CREATE TABLE movies_revenues (
	revenue_id SERIAL PRIMARY KEY,
	movie_id INT REFERENCES movies(movie_id),
	revenues_domestic NUMERIC(10, 2),
	revenues_international NUMERIC(10, 2)
);

--- JUNCTION TABLE (Many-to-many relationship)

CREATE TABLE movies_actors (
	movie_id INT REFERENCES movies(movie_id),
	actor_id INT REFERENCES actors(actor_id),
	PRIMARY KEY (movie_id, actor_id)
);












