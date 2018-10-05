#azrael - Jason Tung and Zane Wang
#SoftDev1 pd8
#K16 -- No Trouble
#2018-10-04

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

def CSV_to_dictionary(filename):
    with open(filename) as fillet:
        x = csv.DictReader(fillet)
    print(x);
    return x 

CSV_to_dictionary("peeps.csv");
CSV_to_dictionary("courses.csv");



'''
command = """
CREATE TABLE students_info  (name TEXT, age NUMBER, id NUMBER, code TEXT, mark NUMBER, id NUMBER);
INSERT INTO students_info (""" + name + ", " + age + ", " + number



#build SQL stmt, save as string
c.execute(command)    #run SQL statement
'''

#==========================================================

db.commit() #save changes
db.close() #close database
