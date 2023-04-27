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