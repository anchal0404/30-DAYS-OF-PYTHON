import sqlite3
connection= sqlite3.connect("marvel.db")
cursor=connection.cursor()


cursor.execute("create table marvel(release_year integer, release_name text)")

marvel_release = [
    (1942,"The First Avenger Captain America"),
    (1995,"Captain Marvel"),
    (2010,"Iron Man "),
    (2011, "Iron Man 2"),
    (2011,"The Incrdible Hulk"),
    (2011,"Thor"),
    (2012, "The Avenger"),
    (2012,"Iron Man 3"),
    (2013,"Thor:The Dark World"),
    (2014,"Captian America:The Winter Soldier"),
    (2014,"Guardians of Galaxy"),
    (2014,"Guardians of Galaxy 2"),
    (2015,"Avengers:Age of Ultron"),
    (2015,"Ant-Man"),
    (2016,"Captain America:Civil War"),
    (2016,"Spider-Man"),
    (2017,"Doctor Srange"),
    (2017,"Black Widow"),
    (2017,"Black Panther"),
    (2017,"Thor Ragnoarok"),
    (2024,"Eternals"),
]
cursor.executemany("insert into marvel values (?,?)",marvel_release)
for row in cursor.execute("select * from marvel"):
    print (row)


connection.close()