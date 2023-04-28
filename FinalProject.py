#UNWSP Final Project
#Gold Group

import sqlite3

connection = sqlite3.connect("info.db")
cursor = connection.cursor()
cursor.execute("create table student (student_id integer, student_name text, number_of_credits integer, "
               "major text, high_school text, email text, username text, password text)")
student_info_list = [
    (63858707, "Jedd Fehr", 8, "Computer Science", "Maple Grove Senior High", "jdfehr@students.unwsp.edu",
     "jdfehr", "145678*!"),
    (14973774, "Advait Deepak", 16, "Communications", "Maple Grove Senior High", "jesus4life@gmail.com",
     "adeepak", "1034869*%"),
    (48396873, "Richard Haeder", 10, "Communications", "Maple Grove Senior High", "bobejoans@gmail.com",
     "rhaeder", "0484928($@"),
    #Create the rest of the lines of the database. I've created the fields, you guys just need to create some rows
    #to get the total rows up to 10. Follow the format I created.
    (11707329, "Jacob Cisewski", 10, "Undecided", "Cisewski Homeschool", "jccisewski@students.unwsp.edu",
     "Jccisewski", "129493!@"),
    (93723740, "Joe Banks", 9, "Business", "Armstrong High School", "jumpingjehosaphat@gmail.com",
     "jumpinjoe", "823749%&"),
    (46284249, "Liam Nelson", 12, "Engineering", "Wayzata High School", "nelson.liam.12@gmail.com",
     "lnelson12", "6478446$%"),
    (98757248, "Jeffrey Bummer", 7, "Psychology", "Hopkins High School", "jkbummer13@gmail.com",
     "jeffbum30", "8236342!*"),
    (94378594, "Blake Anderson", 11, "Engineering", "Parnassus Preparatory", "banderson3@students.unwsp.edu",
     "banderson", "520398^$"),
    (66546707, "Henry Smith", 12, "Undecided", "Legacy Christian Academy", "fastrunner404@gmail.com",
     "zoom1232", "654265*!"),
    (59597245, "Peter Mitchell", 8, "Aviation", "SFTI program", "f14flier@outlook.com",
     "Maveric", "320923@#"),
    ]

cursor.executemany("insert into student values (?,?,?,?,?,?,?,?)", student_info_list)

for row in cursor.execute("select * from student"):
    print(row)

connection.close()