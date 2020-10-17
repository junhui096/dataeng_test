CREATE TABLE car (
	id SERIAL PRIMARY KEY,
	manufacturer TEXT NOT NULL,
	model_name TEXT NOT NULL,
	model_variant TEXT NOT NULL,
	serial_number VARCHAR(32) NOT NULL,
	weight NUMERIC NOT NULL,
	engine_cubic_capacity NUMERIC NOT NULL,
	price NUMERIC NOT NULL,

	UNIQUE(manufacturer, serial_number)
);

CREATE TABLE customer (
	id SERIAL PRIMARY KEY,
	name TEXT NOT NULL,
	phone VARCHAR(10)
);

CREATE TABLE transaction (
	customer INTEGER REFERENCES customer(id),
	car INTEGER REFERENCES car(id),
	salesperson_id VARCHAR(32) NOT NULL,
	date_time_of_transaction TIMESTAMP
);