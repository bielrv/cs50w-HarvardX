CREATE TABLE reviews(
 review_id serial PRIMARY KEY,
 book_id integer NOT NULL,
 user_id integer NOT NULL,
 review_text varchar (355) NOT NULL,
 created_on TIMESTAMP NOT NULL
);
