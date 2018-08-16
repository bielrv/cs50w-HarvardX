CREATE TABLE books(
 book_id serial PRIMARY KEY,
 isbn VARCHAR (50) UNIQUE NOT NULL,
 title VARCHAR (355) NOT NULL,
 author VARCHAR (355) NOT NULL,
 year integer NOT NULL,
 created_on TIMESTAMP NOT NULL
);
