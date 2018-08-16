# Project 1: Books

CS50W - Web Programming with Python and JavaScript

## 1. Objectives

-   Become more comfortable with **Python 3**.
-   Gain experience with **Flask**.
-   Learn to use **SQL** to interact with databases.

## 2. Overview

In this project, you’ll build a book review website. Users will be able to register for your website and then log in using their username and password. Once they log in, they will be able to search for books, leave reviews for individual books, and see the reviews made by other people. You’ll also use the a third-party API by Goodreads, another book review website, to pull in ratings from a broader audience. Finally, users will be able to query for book details and book reviews programmatically via your website’s API.

## 3. Getting Started

1.  Move to project 1 directory  
    `cd project1`  
2.  For the flask script to work, the application needs to be discovered.  
    `export FLASK_APP=application.py`  
3.  In order to use Heroku database, the data base url also need to be discovered.  
    `export DATABASE_URL=postgres://ficpljxencvllu:f3ece79580b1452c6f01aaccbe5120703ac6bf59652b3871ef2b7f76ed443d1e@ec2-54-247-79-32.eu-west-1.compute.amazonaws.com:5432/dftm1idkv20mvc`  
4.  Enable Flask debug mode  
    `export FLASK_DEBUG=1`
5.  `flask run`

### PostgreSQL

For this project, you’ll need to set up a PostgreSQL database to use with our application. It’s possible to set up PostgreSQL locally on your own computer, but for this project, we’ll use a database hosted by Heroku, an online web hosting service.

1.  Navigate to <https://www.heroku.com/>, and create an account if you don’t already have one.
2.  On Heroku’s Dashboard, click “New” and choose “Create new app.”
3.  Give your app a name, and click “Create app.”
4.  On your app’s “Overview” page, click the “Configure Add-ons” button.
5.  In the “Add-ons” section of the page, type in and select “Heroku Postgres.”
6.  Choose the “Hobby Dev - Free” plan, which will give you access to a free PostgreSQL database that will support up to 10,000 rows of data. Click “Provision.”
7.  Now, click the “Heroku Postgres :: Database” link.
8.  You should now be on your database’s overview page. Click on “Settings”, and then “View Credentials.” This is the information you’ll need to log into your database. You can access the database via Adminer, filling in the server (the “Host” in the credentials list), your username (the “User”), your password, and the name of the database, all of which you can find on the Heroku credentials page.
    Alternatively, if you install PostgreSQL on your own computer, you should be able to run psql URI on the command line, where the URI is the link provided in the Heroku credentials list.

## Requirements

Alright, it’s time to actually build your web application! Here are the requirements:

1.  Registration: Users should be able to register for your website, providing (at minimum) a username and password.
2.  Login: Users, once registered, should be able to log in to your website with their username and password.
3.  Logout: Logged in users should be able to log out of the site.
4.  Import: Provided for you in this project is a file called books.csv, which is a spreadsheet in CSV format of 5000 different books. Each one has an ISBN nubmer, a title, an author, and a publication year. In a Python file called import.py separate from your web application, write a program that will take the books and import them into your PostgreSQL database. You will first need to decide what table(s) to create, what columns those tables should have, and how they should relate to one another. Run this program by running python3 import.py to import the books into your database, and submit this program with the rest of your project code.
5.  Search: Once a user has logged in, they should be taken to a page where they can search for a book. Users should be able to type in the ISBN number of a book, the title of a book, or the author of a book. After performing the search, your website should display a list of possible matching results, or some sort of message if there were no matches. If the user typed in only part of a title, ISBN, or author name, your search page should find matches for those as well!
6.  Book Page: When users click on a book from the results of the search page, they should be taken to a book page, with details about the book: its title, author, publication year, ISBN number, and any reviews that users have left for the book on your website.
7.  Review Submission: On the book page, users should be able to submit a review: consisting of a rating on a scale of 1 to 5, as well as a text component to the review where the user can write their opinion about a book. Users should not be able to submit multiple reviews for the same book.
8.  Goodreads Review Data: On your book page, you should also display (if available) the average rating and number of ratings the work has received from Goodreads.
    API Access: If users make a GET request to your website’s /api/<isbn> route, where <isbn> is an ISBN number, your website should return a JSON response containing the book’s title, author, publication date, ISBN number, review count, and average score.  

    `pip install jupyter`  

    `ipython kernel install --user --name "cs50_Porject1"`

## Hints

-   At minimum, you’ll probably want at least:

    -   one table to keep track of users  
    -   one table to keep track of books  
    -   one table to keep track of reviews  

-   In terms of how to “log a user in,” recall that you can store information inside of the session, which can store different values for different users. In particular, if each user has an id, then you could store that id in the session (e.g., in session["user_id"]) to keep track of which user is currently logged in.

## [Flask](http://flask.pocoo.org/)

Flask is a microframework for Python based on Werkzeug, Jinja 2 and good intentions.

Required directories structure:

    /app
        - application.py
        /services
            - app.py
        /templates
            - mainpage.html
        /static
            /styles
                - styles.css

In order to set .css styles with flask when rendering websites insert the following code in the .html file to be styled:  

`<link rel= "stylesheet" type= "text/css" href= "{{ url_for('static',filename='styles/styles.css') }}">`  

## [Jinja2](http://jinja.pocoo.org/)

Jinja2 is a full featured template engine for Python. It has full unicode support, an optional integrated sandboxed execution environment, widely used and BSD licensed.

## PostgreSQL

### [Heroku](https://data.heroku.com/)

Heroku is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.  

### [Postgresql-client](postgresql.org)

To **install** in a linux computer:  

    sudo apt-get install postgresql-client

To **connect**, call psql with the -h option to specify the server’s hostname, -U to specify the username, and then the database name:

    psql -h ec2-54-247-79-32.eu-west-1.compute.amazonaws.com -U ficpljxencvllu dftm1idkv20mvc

To **create accounts table** run:

    CREATE TABLE accounts(
     user_id serial PRIMARY KEY,
     username VARCHAR (50) UNIQUE NOT NULL,
     password VARCHAR (50) NOT NULL,
     email VARCHAR (355) UNIQUE NOT NULL,
     created_on TIMESTAMP NOT NULL,
     last_login TIMESTAMP
    );

* * *

Useful python commands:  

`pip freeze > requirements.txt`
