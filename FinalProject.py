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

check = str(input("Would you like to make any changes? (y or n)"))
if check == "y":
    row_ask = str(input("What student would you like to make changes for? (Please type full name, first and last)"))
    col_ask = int(input("What column do you want to make changes for? (1-8)"))
    if col_ask == 1:
        data = int(input(f"What is {row_ask}'s new ID number?"))
        cursor.execute(f'UPDATE student SET student_id = {data} WHERE student_name == "{row_ask}"')
    if col_ask == 2:
        data = str(input(f"What is {row_ask}'s new name?"))
        cursor.execute(f'UPDATE student SET student_name = {data} WHERE student_name == "{row_ask}"')
    if col_ask == 3:
        data = int(input(f"How many credits does {row_ask} now have?"))
        cursor.execute(f'UPDATE student SET number_of_credits = {data} WHERE student_name == "{row_ask}"')
       #Fill in the rest of the data. It is really easy if you just copy and paste. 
      #Also, one of you two will need to add a loop that loops wether the user wants the table edited.
    if col_ask == 4:
        data = str(input(f"What is {row_ask}'s new major?"))
        cursor.execute(f'UPDATE student SET major = {data} WHERE student_name == "{row_ask}"')
    if col_ask == 5:
            data = str(input(f"What is {row_ask}'s new high school?"))
            cursor.execute(f'UPDATE student SET high_school = {data} WHERE student_name == "{row_ask}"')
    if col_ask == 6:
            data = str(input(f"What is {row_ask}'s new email?"))
            cursor.execute(f'UPDATE student SET email = {data} WHERE student_name == "{row_ask}"')
    if col_ask == 7:
            data = str(input(f"What is {row_ask}'s new username?"))
            cursor.execute(f'UPDATE student SET username = {data} WHERE student_name == "{row_ask}"')
    if col_ask == 8:
            data = str(input(f"What is {row_ask}'s new password?"))
            cursor.execute(f'UPDATE student SET password = {data} WHERE student_name == "{row_ask}"')
connection.close()
