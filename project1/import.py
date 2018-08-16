import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import csv
from datetime import datetime

engine = create_engine('postgres://ficpljxencvllu:f3ece79580b1452c6f01aaccbe5120703ac6bf59652b3871ef2b7f76ed443d1e@ec2-54-247-79-32.eu-west-1.compute.amazonaws.com:5432/dftm1idkv20mvc')
db = scoped_session(sessionmaker(bind=engine))

os.getcwd()
f = open("project1/books.csv")
reader = csv.reader(f)
next(reader, None)
for isbn,title,author,year in reader:
    print (isbn +" "+ title+" "+author+" "+year)
    dt = datetime.now()
    db.execute("Insert into books (isbn,title,author,year,created_on) values (:isbn,:title,:author,:year,:created_on)",
    {"isbn":isbn,"title":title,"author":author,"year":int(year),"created_on":dt})

db.commit()
