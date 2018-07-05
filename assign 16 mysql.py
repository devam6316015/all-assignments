# Q.1- Create a database. Create the following tables:
# 1. Book
# 2. Titles
# 3. Publishers
# 4. Zipcodes
# 5. AuthorsTitles
# 6. Authors

import pymysql as py

db=py.connect("localhost","root","root","acadview")
cursor=db.cursor()
qr="create table book(name char(20),book_id int(20),tilte char(20),genre int(20))"
cursor.execute(qr)
qr="create table title(title_id int(20),title_name char(20),isbn int(20),publisher_id int(20),publisation_year int(5))"
cursor.execute(qr)
qr="create table publishers(publisher_id int(20),name char(20),address char(20),suite_no int(20),zip_code int(20))"
cursor.execute(qr)
qr="create table zipcodes(zip_code int(20),city char(20),state char(20))"
cursor.execute(qr)
qr="create table author(name char(20),auther_id int(20),tilte_id int(20))"
cursor.execute(qr)

db.close()




#Q.2- Insert values in the tables.

import pymysql as py

db=py.connect("localhost","root","root","acadview")
cursor=db.cursor()

try:
	cursor.execute("insert into book values('abc',120,'def',340)")
	db.commit()
	
except:
	db.rollback()
	
qr="insert into publishers values(324,'abc','def',97,98)"
try:
	cursor.execute(qr)
	db.commit()
except:
	db.rollback()
	
qr="insert into title values(345,'acr',567,340,456)"
try:
	cursor.execute(qr)
	db.commit()
except:
	db.rollback()
	
qr="insert into zip_code values(876,'pqr','def')"
try:
	cursor.execute(qr)
	db.commit()
except:
	db.rollback()

qr="insert into author values('abc',120,340)"
try:
	cursor.execute(qr)
	db.commit()
except:
	db.rollback()
	
db.close()





#Q.3- Update any values in any of the tables. Print the original and updated values.

import pymysql as py

db=py.connect("localhost","root","root","acadview")
cursor=db.cursor()
cursor.execute("select * from book")
print(cursor.fetchall())

try:
	cursor.execute("update book set book_id=420 where name='abc'")
	db.commit()
except:
	db.rollback()
	
cursor.execute("select * from book")
print(cursor.fetchall())
db.close()

